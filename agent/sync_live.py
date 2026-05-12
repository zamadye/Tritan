"""Sync live trades from Polymarket CLOB API to live_trades.json."""
import json
import os
from pathlib import Path
from datetime import datetime, timezone


def _check_resolution(market_info):
    """Check if market is resolved. Returns (is_resolved, winning_outcome, winning_price)."""
    if not market_info:
        return False, None, None
    tokens = market_info.get("tokens", [])
    closed = market_info.get("closed", False)
    if not closed or not tokens:
        return False, None, None
    for token in tokens:
        if token.get("winner", False):
            return True, token.get("outcome", ""), float(token.get("price", 0))
    for token in tokens:
        price = float(token.get("price", 0))
        if price >= 0.95:
            return True, token.get("outcome", ""), price
    return False, None, None


def sync_live_trades(clob_client=None):
    """Pull trade history from Polymarket CLOB API and sync to live_trades.json.

    Only syncs trades that are still OPEN (not resolved). Resolved trades
    are handled by sync_polymarket.py which writes to live_sync.json.

    Returns number of trades synced.
    """
    if not clob_client:
        from agent.core import _build_clob_client
        clob_client = _build_clob_client()
        if not clob_client:
            print("[SYNC] Cannot build CLOB client")
            return 0

    live_file = os.getenv("LIVE_TRADES_FILE", "./data/live_trades.json")
    existing = []
    if Path(live_file).exists():
        existing = json.loads(Path(live_file).read_text())

    # Index existing by order_id for dedup
    existing_by_oid = {}
    for t in existing:
        oid = t.get("order_id", "")
        if oid:
            existing_by_oid[oid] = t

    # Fetch from CLOB API
    try:
        resp = clob_client.get_trades()
        clob_trades = resp.get("data", []) if isinstance(resp, dict) else resp
    except Exception as e:
        print(f"[SYNC] Failed to fetch trades: {e}")
        return 0

    # Fetch market info for condition_ids
    market_cache = {}
    condition_ids = set(t.get("market", "") for t in clob_trades if t.get("market"))
    for cid in condition_ids:
        if cid and cid not in market_cache:
            try:
                m = clob_client.get_market(cid)
                market_cache[cid] = m
            except Exception:
                market_cache[cid] = {"question": cid[:20] + "..."}

    synced = 0
    for ct in clob_trades:
        oid = ct.get("id", "")
        if oid in existing_by_oid:
            continue  # already synced

        cid = ct.get("market", "")
        market_info = market_cache.get(cid, {})
        question = market_info.get("question", cid[:20] + "...")

        # Check if market is resolved — skip resolved trades (handled by sync_polymarket.py)
        is_resolved, winning_outcome, _ = _check_resolution(market_info)
        if is_resolved:
            continue

        # Determine side and outcome from tokens
        side = ct.get("side", "BUY")
        outcome = ct.get("outcome", "")

        trade = {
            "trade_id": oid,
            "timestamp": ct.get("timestamp", datetime.now(timezone.utc).isoformat()),
            "mode": "live",
            "market_id": cid,
            "market_question": question,
            "side": "YES" if side == "BUY" else "NO",
            "size_usd": float(ct.get("size", 0)) * float(ct.get("price", 0)),
            "price_at_entry": float(ct.get("price", 0)),
            "status": "LIVE_FILLED",
            "order_id": oid,
            "fill_status": ct.get("status", ""),
            "actual_outcome": None,
            "pnl": None,
            "category": _guess_category(question),
        }
        existing.append(trade)
        synced += 1

    # Save
    Path(live_file).parent.mkdir(parents=True, exist_ok=True)
    Path(live_file).write_text(json.dumps(existing, indent=2))
    open_count = len([t for t in existing if not t.get("actual_outcome")])
    print(f"[SYNC] Synced {synced} new trades (total: {len(existing)}, open: {open_count})")
    return synced


def _guess_category(question: str) -> str:
    q = question.lower()
    if any(k in q for k in ["btc", "bitcoin", "eth", "crypto", "solana", "token"]):
        return "crypto"
    if any(k in q for k in ["war", "peace", "iran", "ukraine", "russia", "china", "nato", "diplomatic"]):
        return "geopolitik"
    if any(k in q for k in ["trump", "biden", "election", "president", "congress", "vote"]):
        return "politics"
    if any(k in q for k in ["nba", "nfl", "soccer", "football", "tennis", "ufc", "match", "win"]):
        return "sports"
    if any(k in q for k in ["eurovision", "oscar", "grammy"]):
        return "entertainment"
    return "other"


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"), override=True)
    sync_live_trades()
