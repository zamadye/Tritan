"""Reconcile phantom P&L — fix trades that were marked EXIT without sell order.

For each EXIT trade without sell_order_id:
1. Check if market is now resolved (YES/NO)
2. If resolved: recalculate actual P&L based on resolution
3. If still open: leave as-is (estimated)
"""
import json
import os
import requests
from pathlib import Path
from datetime import datetime, timezone


def reconcile_phantom_pnl(mode: str = "live") -> int:
    """Fix P&L for EXIT trades without sell orders. Returns count of fixed trades."""
    trades_file = Path(os.getenv(
        "DEMO_TRADES_FILE" if mode == "demo" else "LIVE_TRADES_FILE",
        f"./data/{mode}_trades.json"
    ))
    if not trades_file.exists():
        return 0

    trades = json.loads(trades_file.read_text())
    fixed = 0

    for t in trades:
        # Only fix EXIT trades without sell order
        if t.get("actual_outcome") != "EXIT":
            continue
        if t.get("sell_order_id"):
            continue  # already has real sell

        nid = t.get("market_numeric_id", "")
        if not nid:
            continue

        try:
            r = requests.get(
                f"https://gamma-api.polymarket.com/markets/{nid}",
                timeout=6
            ).json()

            if not r.get("closed"):
                continue  # still open, can't reconcile yet

            op_raw = r.get("outcomePrices", "[]")
            op = op_raw if isinstance(op_raw, list) else json.loads(str(op_raw))
            if not op:
                continue

            yes_final = float(op[0])  # 1.0 if YES won, 0.0 if NO won

            side = t["side"]
            size = t["size_usd"]
            entry = t["price_at_entry"]

            # Calculate actual P&L from resolution
            if side == "YES":
                shares = size / entry if entry > 0 else 0
                actual_return = shares * yes_final
            else:
                no_entry = 1 - entry
                no_shares = size / no_entry if no_entry > 0 else 0
                actual_return = no_shares * (1 - yes_final)

            actual_pnl = round(actual_return - size, 2)
            old_pnl = t.get("pnl", 0) or 0

            if abs(actual_pnl - old_pnl) > 0.05:  # significant difference
                print(f"[RECONCILE] Fixed: {side} @{entry:.0%} ${size} | "
                      f"phantom=${old_pnl:+.2f} → actual=${actual_pnl:+.2f} | "
                      f"{t['market_question'][:45]}")
                t["pnl"] = actual_pnl
                t["pnl_estimated"] = False
                t["prediction_correct"] = actual_pnl > 0
                t["actual_outcome"] = "YES" if yes_final >= 0.99 else "NO"
                t["reconciled_at"] = datetime.now(timezone.utc).isoformat()
                fixed += 1

        except Exception as e:
            continue

    if fixed > 0:
        trades_file.write_text(json.dumps(trades, indent=2))
        print(f"[RECONCILE] Fixed {fixed} phantom P&L records")

    return fixed


if __name__ == "__main__":
    import sys
    sys.path.insert(0, ".")
    from dotenv import load_dotenv
    load_dotenv(".env", override=True)
    n = reconcile_phantom_pnl("live")
    print(f"Total fixed: {n}")
