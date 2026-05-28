"""Trade executor — demo simulation and live CLOB execution."""
import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path

# Detect new polymarket-client SDK
_NEW_SDK = False
try:
    from polymarket.client import SecureClient  # noqa: F401
    _NEW_SDK = True
except ImportError:
    pass


def _is_new_sdk(clob_client) -> bool:
    return hasattr(clob_client, "place_market_order")


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
                # Handle both dict (old SDK) and object (new SDK) formats
                tokens = getattr(clob_market, "tokens", None) or clob_market.get("tokens", [])
                for t in tokens:
                    outcome = (getattr(t, "outcome", None) or t.get("outcome", "")).upper()
                    if side == "YES" and outcome in ("YES", "TRUE", "1"):
                        return getattr(t, "token_id", None) or t.get("token_id", "")
                    if side == "NO" and outcome in ("NO", "FALSE", "0"):
                        return getattr(t, "token_id", None) or t.get("token_id", "")
                # fallback: index-based
                if side == "YES" and tokens:
                    t = tokens[0]
                    return getattr(t, "token_id", None) or t.get("token_id", "")
                if side == "NO" and len(tokens) > 1:
                    t = tokens[1]
                    return getattr(t, "token_id", None) or t.get("token_id", "")
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
                token_id = _get_token_id(market, side, clob_client)
                if not token_id or len(str(token_id)) < 10:
                    raise ValueError(f"Invalid token_id for {side} side: '{token_id}'")

                if _is_new_sdk(clob_client):
                    # New polymarket-client SDK
                    resp = clob_client.place_market_order(
                        token_id=token_id, side="BUY", amount=size, order_type="FOK"
                    )
                    if hasattr(resp, "order_id") and getattr(resp, "status", "") not in ("REJECTED", "FAILED"):
                        trade["status"] = "LIVE_FILLED"
                        trade["order_id"] = getattr(resp, "order_id", "")
                        making = float(getattr(resp, "making_amount", 0) or 0)
                        taking = float(getattr(resp, "taking_amount", 0) or 0)
                        tx_hashes = getattr(resp, "transactions_hashes", ()) or ()
                        trade["tx_hash"] = str(tx_hashes[0]) if tx_hashes else ""
                        if making > 0 and taking > 0:
                            trade["price_at_entry"] = round(making / taking, 4)
                            trade["size_usd"] = round(making, 2)
                        else:
                            trade["size_usd"] = size
                        trade["fill_status"] = getattr(resp, "status", "")
                        print(f"[LIVE] Filled {side} ${trade['size_usd']:.2f} @ {trade['price_at_entry']:.4f} | TX: {trade['tx_hash'][:20]}...")
                    else:
                        msg = getattr(resp, "message", "") or str(resp)
                        trade["status"] = f"REJECTED: {msg}"
                        print(f"[LIVE] Order rejected: {msg}")
                else:
                    # Legacy py-clob-client SDK
                    from py_clob_client_v2.clob_types import MarketOrderArgs, OrderType
                    from py_clob_client_v2.order_builder.constants import BUY

                    order_args = MarketOrderArgs(token_id=token_id, amount=size, side=BUY)
                    signed_order = clob_client.create_market_order(order_args)
                    resp = clob_client.post_order(signed_order, OrderType.FOK)

                    if resp.get("success"):
                        trade["status"] = "LIVE_FILLED"
                        trade["order_id"] = resp.get("orderID", "")
                        trade["tx_hash"] = (resp.get("transactionsHashes") or [""])[0]
                        making = float(resp.get("makingAmount", 0))
                        taking = float(resp.get("takingAmount", 0))
                        if making > 0 and taking > 0:
                            trade["price_at_entry"] = round(making / taking, 4)
                            trade["size_usd"] = round(making, 2)
                        else:
                            trade["size_usd"] = size
                        trade["fill_status"] = resp.get("status", "")
                        print(f"[LIVE] Filled {side} ${trade['size_usd']:.2f} @ {trade['price_at_entry']:.4f} | TX: {trade['tx_hash'][:20]}...")
                    else:
                        trade["status"] = f"REJECTED: {resp.get('errorMsg', 'unknown')}"
                        print(f"[LIVE] Order rejected: {resp.get('errorMsg', resp)}")
            except Exception as e:
                trade["status"] = f"ERROR: {e}"
                print(f"[LIVE] Execution failed: {e}")

    log_file = os.getenv(
        "DEMO_TRADES_FILE" if mode == "demo" else "LIVE_TRADES_FILE",
        f"./data/{mode}_trades.json",
    )
    trades = _load_trades(log_file)
    trades.append(trade)
    _save_trades(trades, log_file)
    return trade
