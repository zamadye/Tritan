"""
Auto-exit monitor — P&L-based exit conditions (works correctly for both YES and NO bets).

All SL/TP/Trail calculations use P&L % of capital, NOT price levels.
This avoids the bug where NO bets at high YES prices trigger SL immediately.
"""
import os
import json
import requests
from datetime import datetime, timezone
from pathlib import Path
from agent.bankroll import update_streak
from agent.learner import _generate_evolution_lessons


def _load_trades(mode: str) -> list:
    f = os.getenv("DEMO_TRADES_FILE" if mode=="demo" else "LIVE_TRADES_FILE",
                  f"./data/{mode}_trades.json")
    p = Path(f)
    return json.loads(p.read_text()) if p.exists() else []


def _save_trades(trades: list, mode: str):
    f = os.getenv("DEMO_TRADES_FILE" if mode=="demo" else "LIVE_TRADES_FILE",
                  f"./data/{mode}_trades.json")
    Path(f).write_text(json.dumps(trades, indent=2))


def _get_current_price(numeric_id: str) -> tuple:
    """Returns (yes_price, no_price) or (None, None)"""
    if not numeric_id:
        return None, None
    try:
        base = os.getenv("POLYMARKET_GAMMA_API", "https://gamma-api.polymarket.com")
        m = requests.get(f"{base}/markets/{numeric_id}", timeout=6).json()
        op_raw = m.get("outcomePrices", "[]")
        op = op_raw if isinstance(op_raw, list) else json.loads(str(op_raw))
        return float(op[0]), float(op[1]) if len(op) > 1 else 0.0
    except Exception:
        return None, None


def _simulate_exit(trade: dict, yes_price: float, reason: str) -> dict:
    """Calculate P&L and mark trade as exited. yes_price is always the YES side price."""
    entry = trade["price_at_entry"]
    size  = trade["size_usd"]
    side  = trade["side"]

    # P&L: use correct shares for each side
    if side == "YES":
        shares = size / entry
        current_value = shares * yes_price
    else:
        no_entry = 1 - entry  # NO price at entry
        no_shares = size / no_entry if no_entry > 0 else size / entry
        current_value = no_shares * (1 - yes_price)
    pnl = round(current_value - size, 2)

    trade["actual_outcome"]     = "EXIT"
    trade["exit_price"]         = yes_price
    trade["exit_reason"]        = reason
    trade["pnl"]                = pnl
    trade["prediction_correct"] = pnl > 0
    trade["resolved_at"]        = datetime.now(timezone.utc).isoformat()
    p_est = trade.get("p_true_estimated", entry if side == "YES" else 1 - entry)
    trade["brier_score"] = round((p_est - (1 if pnl > 0 else 0)) ** 2, 4)
    return trade


def _dynamic_tp(trade: dict) -> float:
    """Dynamic TP ceiling based on edge at entry. Bigger edge = higher TP allowed."""
    edge = abs(trade.get("edge_at_bet") or 0)
    if edge >= 0.20: return 0.50
    if edge >= 0.15: return 0.35
    if edge >= 0.08: return 0.25
    return 0.20


def _get_event_deadline(trade: dict) -> float:
    """Sports: wait for resolved (no time limit). Others: max 24h or end_date."""
    from agent.learner import _infer_category
    cat = _infer_category(trade)

    # Sports resolve naturally within 24h — let resolver handle it, no forced exit
    if cat == "sports":
        return 999.0  # effectively no time limit

    end_date = trade.get("end_date", "")
    if end_date:
        try:
            end_dt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
            hours_to_end = (end_dt - datetime.now(timezone.utc)).total_seconds() / 3600
            if hours_to_end > 0:
                return min(hours_to_end + 2.0, 24.0)
        except Exception:
            pass

    if cat == "crypto":    return 24.0
    if cat in ("geopolitik", "politics"): return 24.0
    return float(os.getenv("EXIT_MAX_HOURS", 24))


def _is_new_sdk(client) -> bool:
    return hasattr(client, "place_limit_order")


def _get_token_from_market(clob_client, cid: str, side: str) -> str:
    """Return token_id for side from get_market(), handling both SDK formats."""
    market = clob_client.get_market(cid)
    tokens = getattr(market, "tokens", None) or market.get("tokens", [])
    for t_info in tokens:
        outcome = (getattr(t_info, "outcome", None) or t_info.get("outcome", "")).upper()
        target = ("YES", "TRUE") if side == "YES" else ("NO", "FALSE")
        if outcome in target:
            return getattr(t_info, "token_id", None) or t_info.get("token_id", "")
    return ""


def _execute_sell_order(trade: dict, yes_p: float, clob_client, retries: int = 3) -> bool:
    """Submit sell order with retry. Sets pending_sell=True on failure for next cycle retry."""
    import time as _time

    side = trade["side"]
    entry = trade["price_at_entry"]
    size = trade["size_usd"]

    # Get token_id
    token_ids = trade.get("token_id", [])
    if isinstance(token_ids, str):
        import json as _j
        try: token_ids = _j.loads(token_ids)
        except: token_ids = []
    token_id = token_ids[0] if side == "YES" else (token_ids[1] if len(token_ids) > 1 else "")

    # Fallback: fetch from CLOB
    if not token_id or len(str(token_id)) < 10:
        cid = trade.get("market_id", "")
        if cid:
            try:
                token_id = _get_token_from_market(clob_client, cid, side)
            except Exception:
                pass

    if not token_id:
        print(f"[SELL] No token_id — pending_sell set for retry")
        trade["pending_sell"] = True
        return False

    entry_price = entry if side == "YES" else 1 - entry
    current_price = yes_p if side == "YES" else (1 - yes_p)
    shares_held = round(size / entry_price, 4) if entry_price > 0 else 1.0
    sell_size = max(shares_held, 1.0)

    for attempt in range(retries):
        try:
            if _is_new_sdk(clob_client):
                resp = clob_client.place_limit_order(
                    token_id=str(token_id), price=round(current_price, 2),
                    size=sell_size, side="SELL"
                )
                order_id = getattr(resp, "order_id", "") or str(resp)
            else:
                from py_clob_client_v2.clob_types import OrderArgs, PartialCreateOrderOptions, OrderType
                from py_clob_client_v2.order_builder.constants import SELL
                tick = "0.01"
                try:
                    m = clob_client.get_market(trade.get("market_id", ""))
                    tick = str(m.get("minimum_tick_size", "0.01"))
                except: pass
                resp = clob_client.create_and_post_order(
                    OrderArgs(token_id=str(token_id), price=round(current_price, 2), size=sell_size, side=SELL),
                    PartialCreateOrderOptions(tick_size=tick, neg_risk=False),
                    OrderType.GTC
                )
                order_id = resp.get("orderID", "") if isinstance(resp, dict) else str(resp)

            print(f"[SELL] Sold (attempt {attempt+1}): {order_id}")
            trade["pending_sell"] = False
            trade["sell_order_id"] = order_id
            return True
        except Exception as e:
            print(f"[SELL] Attempt {attempt+1}/{retries}: {e}")
            if attempt < retries - 1: _time.sleep(2)

    trade["pending_sell"] = True
    print(f"[SELL] All attempts failed — will retry next cycle")
    return False


def check_and_exit(mode: str = "demo", clob_client=None) -> int:
    """Check all open positions and exit those that hit TP/SL/trailing/deadline.

    Exit conditions (checked in order):
    - TAKE_PROFIT: P&L ≥ EXIT_TAKE_PROFIT (default +15%)
    - PARTIAL_EXIT: P&L ≥ 20% → exit half position
    - TRAILING_STOP: P&L drops TRAILING_STOP_PCT below peak
    - STOP_LOSS: P&L ≤ -EXIT_STOP_LOSS (default -12%)
    - EVENT_DEADLINE: held longer than category time limit

    Returns:
        int: Number of positions exited.
    """
    trades = _load_trades(mode)
    open_t = [t for t in trades if not t.get("actual_outcome")]
    now    = datetime.now(timezone.utc)

    # Retry pending sell orders from previous cycles
    if mode == "live" and clob_client:
        pending = [t for t in trades if t.get("pending_sell") and t.get("actual_outcome") == "EXIT"]
        for t in pending:
            nid = t.get("market_numeric_id", "")
            yes_p, _ = _get_current_price(nid)
            if yes_p:
                print(f"[SELL] 🔄 Retrying pending sell: {t['market_question'][:50]}")
                if _execute_sell_order(t, yes_p, clob_client, retries=2):
                    _save_trades(trades, mode)

    tp_return  = float(os.getenv("EXIT_TAKE_PROFIT", 0.15))   # floor TP (overridden per trade)
    sl_pct     = float(os.getenv("EXIT_STOP_LOSS",   0.12))   # -12% return base
    trail_pct  = float(os.getenv("TRAILING_STOP_PCT", 0.05))  # 5% from peak

    exited = 0

    for trade in open_t:
        nid   = trade.get("market_numeric_id", "")
        entry = trade["price_at_entry"]
        side  = trade["side"]
        size  = trade["size_usd"]

        yes_p, no_p = _get_current_price(nid)
        if yes_p is None:
            continue

        shares = size / entry

        # Current P&L % — works correctly for both YES and NO
        # shares = size / entry_YES, tapi untuk NO bet kita beli NO shares
        # NO shares = size / (1 - entry_YES) = size / no_price
        if side == "YES":
            current_value = shares * yes_p
        else:
            no_entry = 1 - entry  # NO price at entry
            no_shares = size / no_entry if no_entry > 0 else shares
            current_value = no_shares * (1 - yes_p)
        pnl_pct = (current_value - size) / size

        # Peak P&L tracking (for trailing stop)
        peak_pnl = trade.get("peak_pnl_pct", 0.0)
        if pnl_pct > peak_pnl:
            peak_pnl = pnl_pct
            trade["peak_pnl_pct"] = peak_pnl
            trade["peak_price"] = yes_p if side == "YES" else (1 - yes_p)

        # Dynamic SL: proportional to leverage (entry price of the side bet)
        # High leverage (low price) = need much looser SL
        entry_price_for_side = entry if side == "YES" else 1 - entry
        if entry_price_for_side < 0.20:
            effective_sl_pct = sl_pct * 5.0   # 125% SL — almost never trigger, hold for movement
        elif entry_price_for_side < 0.30:
            effective_sl_pct = sl_pct * 3.5   # 87.5% SL
        elif entry_price_for_side < 0.40:
            effective_sl_pct = sl_pct * 2.0   # 50% SL
        else:
            effective_sl_pct = sl_pct          # 25% SL for normal entries

        # Trailing SL: exit if pnl drops trail_pct below peak, floor at dynamic SL
        trail_sl     = peak_pnl - trail_pct
        effective_sl = max(trail_sl, -effective_sl_pct)

        max_hours = _get_event_deadline(trade)
        tp_return = _dynamic_tp(trade)

        # Calculate hours held for EVENT_DEADLINE check
        try:
            ts_str = trade["timestamp"]
            if "Z" in ts_str: ts_str = ts_str.replace("Z", "+00:00")
            elif "+" not in ts_str and "T" in ts_str: ts_str += "+00:00"
            hours_held = (now - datetime.fromisoformat(ts_str)).total_seconds() / 3600
        except Exception:
            hours_held = 0

        exit_reason = None

        # ── RIDE THE TREND STRATEGY ──────────────────────────────────────
        # No fixed TP — let price run as long as it keeps moving up
        # Only exit on:
        #   1. Trailing stop (reversal detected) — active after meaningful profit
        #   2. Stop loss (initial protection, very loose)
        #   3. Time deadline

        if pnl_pct <= effective_sl:
            if peak_pnl >= 0.15:
                # Trailing stop: only after 15% peak profit (meaningful move)
                exit_reason = f"TRAILING_STOP (peak={peak_pnl:+.0%} sl={effective_sl:+.0%} now={pnl_pct:+.0%})"
            else:
                # Initial SL: price moved against us without ever being profitable
                exit_reason = f"STOP_LOSS ({pnl_pct:.0%})"
        elif hours_held >= max_hours:
            from agent.learner import _infer_category
            cat = _infer_category(trade)
            exit_reason = f"EVENT_DEADLINE ({cat} {hours_held:.0f}h/{max_hours:.0f}h)"
        # ─────────────────────────────────────────────────────────────────

        if exit_reason:
            _simulate_exit(trade, yes_p, exit_reason)
            icon = "✅" if trade["pnl"] > 0 else "❌"
            print(f"[EXIT] {icon} {exit_reason} | {side} P&L=${trade['pnl']:+.2f} | {trade['market_question'][:50]}")

            # Live mode: submit sell order to close position on Polymarket
            if mode == "live" and clob_client:
                _execute_sell_order(trade, yes_p, clob_client)

            update_streak(trade["prediction_correct"], mode)
            exited += 1

    if exited > 0:
        _save_trades(trades, mode)
        _generate_evolution_lessons(trades, mode)
        resolved = [t for t in trades if t.get("actual_outcome")]
        wins = [t for t in resolved if t.get("prediction_correct")]
        pnl  = sum(t.get("pnl", 0) for t in resolved)
        print(f"[EXIT] 📊 {exited} exits | Win: {len(wins)/len(resolved):.0%} | P&L: ${pnl:+.2f}")
    else:
        _save_trades(trades, mode)  # persist peak_pnl_pct updates
        print(f"[EXIT] No exit conditions triggered ({len(open_t)} open)")

    return exited
