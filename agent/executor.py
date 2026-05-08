"""Trade executor — demo simulation and live CLOB execution."""
import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path


def _load_trades(filepath: str) -> list:
    p = Path(filepath)
    if p.exists():
        return json.loads(p.read_text())
    return []


def _save_trades(trades: list, filepath: str):
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    Path(filepath).write_text(json.dumps(trades, indent=2))


def _get_token_id(market: dict, side: str, clob_client=None) -> str:
    """Get token_id for order. Tries market dict first, falls back to CLOB API."""
    # Try from market dict (Gamma API format)
    ids = market.get("token_id", [])
    if isinstance(ids, str):
        try:
            import json as _json
            ids = _json.loads(ids)
        except Exception:
            ids = []

    token = ids[0] if side == "YES" else ids[1] if len(ids) > 1 else ""

    # Validate: CLOB token IDs are very long integers (>50 chars)
    if token and len(str(token)) > 50:
        return str(token)

    # Fallback: fetch from CLOB API using condition_id
    if clob_client:
        try:
            condition_id = market.get("id", "")
            if condition_id:
                clob_market = clob_client.get_market(condition_id)
                tokens = clob_market.get("tokens", [])
                for t in tokens:
                    outcome = t.get("outcome", "").upper()
                    if side == "YES" and outcome in ("YES", "TRUE", "1"):
                        return t["token_id"]
                    if side == "NO" and outcome in ("NO", "FALSE", "0"):
                        return t["token_id"]
                # fallback: index-based
                if side == "YES" and tokens:
                    return tokens[0]["token_id"]
                if side == "NO" and len(tokens) > 1:
                    return tokens[1]["token_id"]
        except Exception:
            pass

    return str(token) if token else ""


def execute_trade(market: dict, side: str, size: float, mode: str, clob_client=None) -> dict:
    """Execute a trade and append to trade log with full audit fields.

    In demo mode: simulates execution, logs trade with timestamp.
    In live mode: submits order via Polymarket CLOB API.

    Args:
        market: Market dict (id, question, price, category, token_id).
        side: 'YES' or 'NO'.
        size: Position size in USDC.
        mode: 'demo' or 'live'.
        clob_client: Initialized ClobClient (required for live mode).

    Returns:
        dict: Trade record with trade_id, timestamp, price_at_entry, size_usd.
    """
    trade = {
        "trade_id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
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

                token_id = _get_token_id(market, side, clob_client)
                if not token_id:
                    raise ValueError(f"No token_id for {side} side")

                order_args = MarketOrderArgs(
                    token_id=token_id,
                    amount=size,
                    side=BUY,
                )
                signed_order = clob_client.create_market_order(order_args)
                resp = clob_client.post_order(signed_order, OrderType.FOK)
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
