"""
Auto-exit monitor — checks open positions every cycle and exits on:
- TRAILING_STOP: harga turun dari peak melewati trailing distance
- TAKE_PROFIT: nilai posisi mencapai 2x modal
- STOP_LOSS: nilai posisi turun -33% dari modal (hanya jika belum ada profit)
- TIME_LIMIT: held >48h
"""
import os
import json
import requests
from datetime import datetime, timezone, timedelta
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
        base = os.getenv("POLYMARKET_GAMMA_API","https://gamma-api.polymarket.com")
        m = requests.get(f"{base}/markets/{numeric_id}", timeout=6).json()
        op_raw = m.get("outcomePrices","[]")
        op = op_raw if isinstance(op_raw, list) else json.loads(str(op_raw))
        return float(op[0]), float(op[1]) if len(op)>1 else 0.0
    except Exception:
        return None, None


def _simulate_exit(trade: dict, exit_price: float, reason: str) -> dict:
    """
    Simulate selling the position at exit_price.
    In demo: calculate P&L from price movement (not resolution).
    In live: would call CLOB sell order.
    """
    entry = trade["price_at_entry"]
    size  = trade["size_usd"]
    side  = trade["side"]

    # Shares bought = size / entry_price
    shares = size / entry

    # Current value of shares
    current_value = shares * exit_price if side == "YES" else shares * (1 - exit_price)
    pnl = round(current_value - size, 2)

    trade["actual_outcome"]      = "EXIT"  # not resolved, but exited
    trade["exit_price"]          = exit_price
    trade["exit_reason"]         = reason
    trade["pnl"]                 = pnl
    trade["prediction_correct"]  = pnl > 0  # profitable exit = "correct"
    trade["resolved_at"]         = datetime.now(timezone.utc).isoformat()

    # Brier score approximation
    p = entry if side == "YES" else 1 - entry
    trade["brier_score"] = round((p - (1 if pnl > 0 else 0)) ** 2, 4)

    return trade


def check_and_exit(mode: str = "demo", clob_client=None) -> int:
    """
    Check all open positions for exit conditions.
    Trailing stop: SL level naik mengikuti peak price, mengunci profit.
    Returns number of positions exited.
    """
    trades    = _load_trades(mode)
    open_t    = [t for t in trades if not t.get("actual_outcome")]
    now       = datetime.now(timezone.utc)

    # Trailing distance: SL selalu X% di bawah peak price
    trail_pct  = float(os.getenv("TRAILING_STOP_PCT",  0.25))  # 25% dari peak
    tp_return  = float(os.getenv("EXIT_TAKE_PROFIT",   1.00))  # +100% return = 2x modal
    max_hours  = float(os.getenv("EXIT_MAX_HOURS",     48))

    exited = 0

    for trade in open_t:
        nid   = trade.get("market_numeric_id", "")
        entry = trade["price_at_entry"]
        side  = trade["side"]
        size  = trade["size_usd"]

        yes_p, no_p = _get_current_price(nid)
        if yes_p is None:
            continue

        now_p   = yes_p if side == "YES" else no_p
        shares  = size / entry

        # Update peak price (high watermark) — persist ke disk setiap cycle
        peak = trade.get("peak_price", entry)
        if now_p > peak:
            peak = now_p
            trade["peak_price"] = peak

        # Trailing stop level = peak × (1 - trail_pct)
        # Tapi tidak boleh lebih rendah dari initial SL (entry × 0.67)
        initial_sl  = entry * (1 - float(os.getenv("EXIT_STOP_LOSS", 0.33)))
        trailing_sl = peak * (1 - trail_pct)
        effective_sl = max(trailing_sl, initial_sl)

        # Current return
        now_value  = shares * now_p
        pnl_pct    = (now_value - size) / size

        # Time held
        try:
            ts_str = trade["timestamp"]
            if "Z" in ts_str: ts_str = ts_str.replace("Z", "+00:00")
            elif "+" not in ts_str and "T" in ts_str: ts_str += "+00:00"
            hours_held = (now - datetime.fromisoformat(ts_str)).total_seconds() / 3600
        except Exception:
            hours_held = 0

        exit_reason = None
        exit_price  = now_p
        partial     = False

        if pnl_pct >= tp_return:
            exit_reason = f"TAKE_PROFIT_2X (+{pnl_pct:.0%})"
        elif pnl_pct >= 0.50 and not trade.get("partial_exited"):
            # Partial exit: jual 50% posisi saat +50% return, biarkan sisanya trailing
            exit_reason = f"PARTIAL_EXIT_50% (+{pnl_pct:.0%})"
            partial = True
        elif now_p <= effective_sl:
            if peak > entry:
                locked_pnl = shares * effective_sl - size
                exit_reason = f"TRAILING_STOP (peak={peak:.2f}→sl={effective_sl:.2f}, locked ${locked_pnl:+.2f})"
            else:
                exit_reason = f"STOP_LOSS ({pnl_pct:.0%})"
            exit_price = effective_sl
        elif hours_held >= max_hours:
            exit_reason = f"TIME_LIMIT ({hours_held:.0f}h)"

        if exit_reason:
            if partial:
                # Partial: hanya exit 50%, update size_usd sisanya
                half_size   = size / 2
                half_shares = shares / 2
                partial_pnl = round(half_shares * now_p - half_size, 2)
                trade["size_usd"]       = round(size / 2, 2)   # sisa 50%
                trade["partial_exited"] = True
                trade["partial_pnl"]    = partial_pnl
                trade["peak_price"]     = peak  # reset peak untuk trailing sisa
                icon = "✅"
                print(f"[EXIT] {icon} {exit_reason} | {side} partial P&L=${partial_pnl:+.2f} | {trade['market_question'][:50]}")
                # Tidak update streak untuk partial exit
            else:
                _simulate_exit(trade, exit_price, exit_reason)
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
        # Tetap save untuk persist peak_price updates
        _save_trades(trades, mode)
        print(f"[EXIT] No exit conditions triggered ({len(open_t)} open)")

    return exited
