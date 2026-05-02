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
    p = entry if side == "YES" else 1 - entry
    trade["brier_score"] = round((p - (1 if pnl > 0 else 0)) ** 2, 4)
    return trade


def _get_event_deadline(trade: dict) -> float:
    """Event-driven time limit per category."""
    from agent.learner import _infer_category
    cat = _infer_category(trade)
    end_date = trade.get("end_date", "")
    if cat == "sports":
        return 4.0
    if cat == "crypto":
        return 6.0
    if cat in ("geopolitik", "politics"):
        if end_date:
            try:
                end_dt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
                hours_to_end = (end_dt - datetime.now(timezone.utc)).total_seconds() / 3600
                if 0 < hours_to_end <= 48:
                    return hours_to_end
            except Exception:
                pass
        return 24.0
    return float(os.getenv("EXIT_MAX_HOURS", 4))


def check_and_exit(mode: str = "demo", clob_client=None) -> int:
    trades = _load_trades(mode)
    open_t = [t for t in trades if not t.get("actual_outcome")]
    now    = datetime.now(timezone.utc)

    tp_return  = float(os.getenv("EXIT_TAKE_PROFIT", 0.50))   # +50% return
    sl_pct     = float(os.getenv("EXIT_STOP_LOSS",   0.33))   # -33% return
    trail_pct  = float(os.getenv("TRAILING_STOP_PCT", 0.10))  # 10% from peak

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
            # Store display price
            trade["peak_price"] = yes_p if side == "YES" else (1 - yes_p)

        # Trailing SL: exit if pnl drops trail_pct below peak
        # But never worse than initial SL
        trail_sl = peak_pnl - trail_pct        # e.g. peak=+30%, trail=10% → SL at +20%
        effective_sl = max(trail_sl, -sl_pct)  # floor at -33%

        # Time held
        try:
            ts_str = trade["timestamp"]
            if "Z" in ts_str: ts_str = ts_str.replace("Z", "+00:00")
            elif "+" not in ts_str and "T" in ts_str: ts_str += "+00:00"
            hours_held = (now - datetime.fromisoformat(ts_str)).total_seconds() / 3600
        except Exception:
            hours_held = 0

        max_hours = _get_event_deadline(trade)

        exit_reason = None
        partial     = False

        if pnl_pct >= tp_return:
            exit_reason = f"TAKE_PROFIT (+{pnl_pct:.0%})"
        elif pnl_pct >= 0.20 and not trade.get("partial_exited"):
            exit_reason = f"PARTIAL_EXIT_50% (+{pnl_pct:.0%})"
            partial = True
        elif pnl_pct <= effective_sl:
            if peak_pnl > 0.05:  # only trailing stop if we had meaningful profit
                exit_reason = f"TRAILING_STOP (peak={peak_pnl:+.0%} sl={effective_sl:+.0%} now={pnl_pct:+.0%})"
            else:
                exit_reason = f"STOP_LOSS ({pnl_pct:.0%})"
        elif hours_held >= max_hours:
            from agent.learner import _infer_category
            cat = _infer_category(trade)
            exit_reason = f"EVENT_DEADLINE ({cat} {hours_held:.0f}h/{max_hours:.0f}h)"

        if exit_reason:
            if partial:
                half_size = size / 2
                half_shares = shares / 2
                partial_pnl = round(half_shares * (yes_p if side=="YES" else (1-yes_p)) - half_size, 2)
                trade["size_usd"]       = round(size / 2, 2)
                trade["partial_exited"] = True
                trade["partial_pnl"]    = partial_pnl
                trade["peak_pnl_pct"]   = peak_pnl
                icon = "✅"
                print(f"[EXIT] {icon} {exit_reason} | {side} partial P&L=${partial_pnl:+.2f} | {trade['market_question'][:50]}")
            else:
                _simulate_exit(trade, yes_p, exit_reason)
                icon = "✅" if trade["pnl"] > 0 else "❌"
                print(f"[EXIT] {icon} {exit_reason} | {side} P&L=${trade['pnl']:+.2f} | {trade['market_question'][:50]}")
                update_streak(trade["prediction_correct"])
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
