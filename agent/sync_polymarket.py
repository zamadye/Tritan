"""
Sync all Polymarket account data to JSON files for dashboard.
Fetches: balance, trade history, open positions, calculates P&L/stats.
Uses CLOB API for trades + market resolution, Data API for positions + portfolio value.
"""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env", override=True)


def build_clob_client():
    """Build CLOB client from env credentials."""
    try:
        from py_clob_client_v2.client import ClobClient
        host = os.getenv("POLYMARKET_CLOB_HOST", "https://clob.polymarket.com")
        key = os.getenv("POLYGON_PRIVATE_KEY", "")
        funder = os.getenv("POLYGON_WALLET_ADDRESS", "")
        sig_type = int(os.getenv("SIGNATURE_TYPE", 0))
        client = ClobClient(
            host, key=key, chain_id=int(os.getenv("CHAIN_ID", 137)),
            signature_type=sig_type,
            funder=funder if sig_type in (1, 2, 3) else None,
        )
        client.set_api_creds(client.create_or_derive_api_key())
        return client
    except Exception as e:
        print(f"[SYNC] CLOB client error: {e}")
        return None


def fetch_balance(clob_client):
    """Fetch USDC balance from CLOB API."""
    try:
        from py_clob_client_v2.clob_types import BalanceAllowanceParams, AssetType
        result = clob_client.get_balance_allowance(
            BalanceAllowanceParams(asset_type=AssetType.COLLATERAL)
        )
        return round(float(result.get('balance', 0)) / 1e6, 2)
    except Exception as e:
        print(f"[SYNC] Balance fetch error: {e}")
        return 0.0


def fetch_clob_trades(clob_client):
    """Fetch trade history from CLOB API."""
    try:
        return clob_client.get_trades() or []
    except Exception as e:
        print(f"[SYNC] CLOB trades error: {e}")
        return []


def fetch_positions_from_api(wallet_address):
    """Fetch open positions from Polymarket Data API."""
    try:
        import urllib.request
        url = f"https://data-api.polymarket.com/positions?user={wallet_address}&sizeThreshold=.01&limit=100"
        req = urllib.request.Request(url, headers={"User-Agent": "Tritan/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"[SYNC] Positions fetch error: {e}")
        return []


def fetch_portfolio_value(wallet_address):
    """Fetch current portfolio value from Polymarket Data API."""
    try:
        import urllib.request
        url = f"https://data-api.polymarket.com/value?user={wallet_address}"
        req = urllib.request.Request(url, headers={"User-Agent": "Tritan/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            if data and len(data) > 0:
                return float(data[0].get('value', 0))
        return 0.0
    except Exception as e:
        print(f"[SYNC] Portfolio value fetch error: {e}")
        return 0.0


def fetch_market_info(condition_id, clob_client):
    """Fetch market info including resolution status from CLOB API."""
    try:
        return clob_client.get_market(condition_id)
    except Exception:
        return None


def guess_category(question: str) -> str:
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


def get_market_resolution(market_info):
    """Extract resolution info from market data.
    Returns (is_resolved, winning_outcome, winning_price).
    """
    if not market_info:
        return False, None, None

    tokens = market_info.get("tokens", [])
    closed = market_info.get("closed", False)

    if not closed or not tokens:
        return False, None, None

    # Find the winner
    for token in tokens:
        if token.get("winner", False):
            return True, token.get("outcome", ""), float(token.get("price", 0))

    # Closed but no winner = ambiguous, check prices
    for token in tokens:
        price = float(token.get("price", 0))
        if price >= 0.95:
            return True, token.get("outcome", ""), price

    return False, None, None


def sync_all():
    """Main sync function. Fetches all data and saves to JSON files."""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    wallet = os.getenv("POLYGON_WALLET_ADDRESS", "")
    print(f"[SYNC] Starting sync for wallet: {wallet[:10]}...")

    # Build CLOB client
    clob_client = build_clob_client()
    if not clob_client:
        print("[SYNC] Failed to build CLOB client")
        return False

    # 1. Fetch balance
    balance = fetch_balance(clob_client)
    print(f"[SYNC] Balance: ${balance:.2f}")

    # 2. Fetch portfolio value
    portfolio_value = fetch_portfolio_value(wallet)
    print(f"[SYNC] Portfolio value: ${portfolio_value:.2f}")

    # 3. Fetch CLOB trades (has market, side, size, price, outcome)
    clob_trades = fetch_clob_trades(clob_client)
    print(f"[SYNC] CLOB trades: {len(clob_trades)}")

    # 4. Fetch positions from Data API
    positions = fetch_positions_from_api(wallet)
    print(f"[SYNC] Positions from Data API: {len(positions)}")

    # 5. Get unique condition IDs and fetch market info
    condition_ids = set()
    for t in clob_trades:
        cid = t.get("market", "")
        if cid:
            condition_ids.add(cid)
    for p in positions:
        cid = p.get("conditionId", "")
        if cid:
            condition_ids.add(cid)

    market_cache = {}
    for cid in condition_ids:
        if cid:
            info = fetch_market_info(cid, clob_client)
            if info:
                market_cache[cid] = info
    print(f"[SYNC] Markets fetched: {len(market_cache)}")

    # 6. Group CLOB trades by condition_id
    trade_groups = {}
    for t in clob_trades:
        cid = t.get("market", "")
        if not cid:
            continue
        if cid not in trade_groups:
            trade_groups[cid] = {"buys": [], "sells": []}
        entry = {
            "size": float(t.get("size", 0)),
            "price": float(t.get("price", 0)),
            "outcome": t.get("outcome", ""),
            "side": t.get("side", ""),
            "status": t.get("status", ""),
        }
        if t.get("side") == "BUY":
            trade_groups[cid]["buys"].append(entry)
        elif t.get("side") == "SELL":
            trade_groups[cid]["sells"].append(entry)

    # 7. Build processed trades with P&L
    processed_trades = []
    open_position_market_ids = set()

    for cid, group in trade_groups.items():
        market = market_cache.get(cid, {})
        question = market.get("question", cid[:20] + "...")
        tokens = market.get("tokens", [])

        # Get outcome from first buy
        outcome = group["buys"][0]["outcome"] if group["buys"] else "Unknown"

        # Calculate totals
        total_buy_size = sum(b["size"] for b in group["buys"])
        total_buy_cost = sum(b["size"] * b["price"] for b in group["buys"])
        total_sell_size = sum(s["size"] for s in group["sells"])
        total_sell_value = sum(s["size"] * s["price"] for s in group["sells"])

        avg_entry = total_buy_cost / total_buy_size if total_buy_size > 0 else 0

        # Check if market is resolved
        is_resolved, winning_outcome, winning_price = get_market_resolution(market)

        if is_resolved:
            # Calculate P&L based on resolution
            # Shares held = buy_size - sell_size
            shares_held = total_buy_size - total_sell_size
            cost_basis = total_buy_cost - total_sell_value

            if winning_outcome and winning_outcome.lower() == outcome.lower():
                # Our outcome won: shares worth winning_price each
                resolution_value = shares_held * winning_price
                pnl = resolution_value - cost_basis
                actual_outcome = "WIN"
            else:
                # Our outcome lost: shares worth 0
                pnl = -cost_basis
                actual_outcome = "LOSS"

            processed_trades.append({
                "trade_id": f"clob-{cid[:12]}",
                "market_id": cid,
                "market_question": question,
                "side": outcome.upper(),
                "size_usd": round(total_buy_cost, 2),
                "price_at_entry": round(avg_entry, 4),
                "status": "RESOLVED",
                "category": guess_category(question),
                "actual_outcome": actual_outcome,
                "pnl": round(pnl, 2),
                "resolution_price": winning_price,
                "winning_outcome": winning_outcome,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            })
        else:
            # Still open
            open_position_market_ids.add(cid)
            # Get current market price for the outcome
            current_price = 0
            for token in tokens:
                if token.get("outcome", "").lower() == outcome.lower():
                    current_price = float(token.get("price", 0))
                    break

            # Unrealized P&L
            shares_held = total_buy_size - total_sell_size
            cost_basis = total_buy_cost - total_sell_value
            current_value = shares_held * current_price
            unrealized_pnl = current_value - cost_basis

            processed_trades.append({
                "trade_id": f"clob-{cid[:12]}",
                "market_id": cid,
                "market_question": question,
                "side": outcome.upper(),
                "size_usd": round(total_buy_cost, 2),
                "price_at_entry": round(avg_entry, 4),
                "status": "OPEN",
                "category": guess_category(question),
                "actual_outcome": None,
                "pnl": None,
                "unrealized_pnl": round(unrealized_pnl, 2),
                "current_price": current_price,
                "shares": round(total_buy_size - total_sell_size, 4),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            })

    # 8. Process positions from Data API
    processed_positions = []
    for pos in positions:
        cid = pos.get("conditionId", "")
        question = pos.get("question", market_cache.get(cid, {}).get("question", cid[:20] + "..."))
        outcome = pos.get("outcome", "YES").upper()
        size = float(pos.get("size", 0))
        avg_price = float(pos.get("avgPrice", 0))

        if size > 0.01:
            market = market_cache.get(cid, {})
            current_price = 0
            for token in market.get("tokens", []):
                if token.get("outcome", "").lower() == outcome.lower():
                    current_price = float(token.get("price", 0))
                    break

            # Check if market resolved
            is_resolved, winning_outcome, _ = get_market_resolution(market)
            if is_resolved:
                won = winning_outcome and winning_outcome.lower() == outcome.lower()
                pnl = size * (1 - avg_price) if won else -(size * avg_price)
                processed_positions.append({
                    "trade_id": pos.get("id", f"pos-{cid[:8]}"),
                    "market_id": cid,
                    "market_question": question,
                    "side": outcome,
                    "size_usd": round(size * avg_price, 2),
                    "price_at_entry": round(avg_price, 4),
                    "current_price": 1.0 if won else 0.0,
                    "status": "RESOLVED",
                    "category": guess_category(question),
                    "shares": size,
                    "pnl": round(pnl, 2),
                    "actual_outcome": "WIN" if won else "LOSS",
                })
            else:
                processed_positions.append({
                    "trade_id": pos.get("id", f"pos-{cid[:8]}"),
                    "market_id": cid,
                    "market_question": question,
                    "side": outcome,
                    "size_usd": round(size * avg_price, 2),
                    "price_at_entry": round(avg_price, 4),
                    "current_price": current_price,
                    "status": "OPEN",
                    "category": guess_category(question),
                    "shares": size,
                    "unrealized_pnl": round(size * (current_price - avg_price), 2),
                })

    # 9. Calculate stats
    resolved = [t for t in processed_trades if t.get("actual_outcome")]
    open_trades = [t for t in processed_trades if not t.get("actual_outcome")]

    wins = [t for t in resolved if t.get("actual_outcome") == "WIN"]
    losses = [t for t in resolved if t.get("actual_outcome") == "LOSS"]
    total_pnl = sum(t.get("pnl", 0) for t in resolved)
    unrealized_pnl = sum(t.get("unrealized_pnl", 0) for t in open_trades)
    deployed = sum(t.get("size_usd", 0) for t in open_trades)

    stats = {
        "balance": balance,
        "portfolio_value": portfolio_value,
        "total_trades": len(processed_trades),
        "resolved": len(resolved),
        "open": len(open_trades),
        "wins": len(wins),
        "losses": len(losses),
        "total_pnl": round(total_pnl, 2),
        "unrealized_pnl": round(unrealized_pnl, 2),
        "deployed": round(deployed, 2),
        "win_rate": round(len(wins) / len(resolved), 3) if resolved else 0,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    # 10. Merge with existing agent trades (don't overwrite agent-placed trades)
    existing_file = data_dir / "live_trades.json"
    existing_trades = []
    if existing_file.exists():
        try:
            existing_trades = json.loads(existing_file.read_text())
        except Exception:
            pass

    # Keep agent-placed trades (UUID format trade_id, not clob- prefix)
    agent_trades = [t for t in existing_trades
                    if not t.get("trade_id", "").startswith("clob-")
                    and not t.get("trade_id", "").startswith("pos-")]

    # Build lookup of synced market_ids to avoid duplicates
    synced_market_ids = {t.get("market_id") for t in processed_trades}

    # Add agent trades that aren't already in synced data
    for at in agent_trades:
        mid = at.get("market_id", "")
        if mid not in synced_market_ids:
            processed_trades.append(at)

    # 11. Save to JSON files — sync data goes to live_sync.json (dashboard reads both)
    (data_dir / "live_sync.json").write_text(json.dumps(processed_trades, indent=2))
    (data_dir / "live_positions.json").write_text(json.dumps(processed_positions, indent=2))
    (data_dir / "live_stats.json").write_text(json.dumps(stats, indent=2))
    (data_dir / "live_balance.json").write_text(json.dumps({
        "balance": balance,
        "portfolio_value": portfolio_value,
        "wallet": wallet,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }, indent=2))

    print(f"[SYNC] Complete!")
    print(f"  - Total trades: {len(processed_trades)}")
    print(f"  - Resolved: {len(resolved)} (W:{len(wins)} / L:{len(losses)})")
    print(f"  - Open: {len(open_trades)}")
    print(f"  - Positions: {len(processed_positions)}")
    print(f"  - Balance: ${balance:.2f}")
    print(f"  - Portfolio value: ${portfolio_value:.2f}")
    print(f"  - Deployed: ${deployed:.2f}")
    print(f"  - Realized P&L: ${total_pnl:.2f}")
    print(f"  - Unrealized P&L: ${unrealized_pnl:.2f}")
    print(f"  - Win Rate: {stats['win_rate']*100:.1f}%")

    return True


if __name__ == "__main__":
    sync_all()
