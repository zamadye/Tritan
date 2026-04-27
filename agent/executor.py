"""Trade executor — demo simulation and live CLOB execution."""
import json
import os
import uuid
from datetime import datetime
from pathlib import Path


def _load_trades(filepath: str) -> list:
    p = Path(filepath)
    if p.exists():
        return json.loads(p.read_text())
    return []


def _save_trades(trades: list, filepath: str):
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    Path(filepath).write_text(json.dumps(trades, indent=2))


def _get_token_id(market: dict, side: str) -> str:
    try:
        ids = json.loads(market.get("token_id", "[]"))
        return ids[0] if side == "YES" else ids[1]
    except Exception:
        return ""


def execute_trade(market: dict, side: str, size: float, mode: str, clob_client=None) -> dict:
    trade = {
        "trade_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "mode": mode,
        "market_id": market.get("id", ""),
        "market_numeric_id": market.get("numeric_id", ""),
        "market_question": market["question"],
        "end_date": market.get("end_date", ""),
        "category": market.get("category", "unknown"),
        "side": side,
        "size_usd": size,
        "price_at_entry": market["price"],
        "status": None,
        "actual_outcome": None,
        "pnl": None,
    }

    if mode == "demo":
        trade["status"] = "DEMO_FILLED"
        print(f"[DEMO] 📝 Simulated {side} bet: ${size:.2f} on '{market['question'][:60]}'")

    elif mode == "live":
        if os.getenv("DRY_RUN", "false").lower() == "true":
            trade["status"] = "DRY_RUN"
            print(f"[DRY_RUN] Would execute {side} ${size:.2f} on '{market['question'][:60]}'")
        else:
            try:
                from py_clob_client.clob_types import MarketOrderArgs, OrderType
                from py_clob_client.order_builder.constants import BUY

                token_id = _get_token_id(market, side)
                order_args = MarketOrderArgs(
                    token_id=token_id,
                    amount=size,
                    side=BUY,
                    order_type=OrderType.FOK,
                )
                resp = clob_client.post_order(
                    clob_client.create_market_order(order_args), OrderType.FOK
                )
                trade["status"] = "LIVE_FILLED"
                trade["tx_hash"] = resp.get("transactionHash", "")
                print(f"[LIVE] 💰 Executed {side} ${size:.2f} | TX: {trade['tx_hash'][:20]}...")
            except Exception as e:
                trade["status"] = f"ERROR: {e}"
                print(f"[LIVE] ❌ Execution failed: {e}")

    log_file = os.getenv(
        "DEMO_TRADES_FILE" if mode == "demo" else "LIVE_TRADES_FILE",
        f"./data/{mode}_trades.json",
    )
    trades = _load_trades(log_file)
    trades.append(trade)
    _save_trades(trades, log_file)
    return trade
