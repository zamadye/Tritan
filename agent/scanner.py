"""Market scanner — fetches candidate markets from Gamma API."""
import os
import requests
from datetime import datetime, timezone


def get_candidate_markets():
    """Fetch and filter active Polymarket markets via Gamma API.

    Applies filters: min volume, min liquidity, price range, days to resolve,
    category blacklist, and bet_no_signal flag for statistically overpriced markets.

    Returns:
        list[dict]: Sorted candidate markets. Fields include id, question, price,
                    volume_24h, liquidity, end_date, category, bet_no_signal.
    """
    min_volume = float(os.getenv("MIN_VOLUME_24H", 5000))
    min_liquidity = float(os.getenv("MIN_LIQUIDITY", 2000))
    min_price = float(os.getenv("MIN_MARKET_PRICE", 0.08))
    max_price = float(os.getenv("MAX_MARKET_PRICE", 0.92))
    max_markets = int(os.getenv("MAX_MARKETS_TO_SCAN", 50))
    min_days = int(os.getenv("MIN_DAYS_TO_RESOLVE", 1))
    max_days = int(os.getenv("MAX_DAYS_TO_RESOLVE", 7))  # default 7 hari = cepat resolve

    url = f"{os.getenv('POLYMARKET_GAMMA_API', 'https://gamma-api.polymarket.com')}/markets"
    params = {
        "active": "true",
        "closed": "false",
        "limit": max_markets,
        "order": "volume24hr",
        "ascending": "false",
    }

    try:
        resp = requests.get(url, params=params, timeout=20, verify=False)
        resp.raise_for_status()
        markets = resp.json()
    except Exception as e:
        print(f"[SCANNER] ❌ Gamma API error: {e}")
        return []

    raw_blacklist = os.getenv("BLACKLISTED_CATEGORIES", "")
    blacklisted = set(x.strip() for x in raw_blacklist.split(",") if x.strip())

    # Also blacklist sports by keyword if "sports" in blacklisted
    sports_keywords = set()
    if "sports" in blacklisted:
        sports_keywords = {"vs.","vs ","open:","grand prix","ipl","ufc","mma",
                           "nba","mlb","nhl","nfl","tennis","cricket","soccer",
                           "football","basketball","baseball","hockey"}
    preferred = set(os.getenv("PREFERRED_CATEGORIES", "crypto,economics").split(","))
    now = datetime.now(timezone.utc)

    candidates = []
    for m in markets:
        try:
            price = float(m.get("lastTradePrice") or 0.5)
            if price == 0.5 and m.get("outcomePrices"):
                op = m["outcomePrices"]
                price = float(op[0]) if isinstance(op, list) else float(str(op).strip("[]").split(",")[0].strip().strip('"'))

            volume = float(m.get("volume24hr", 0))
            liquidity = float(m.get("liquidity", 0))
            category = m.get("category", "").lower()

            # Days to resolution filter
            days_left = None
            hours_left = None
            end_date = m.get("endDate", "")
            if end_date:
                try:
                    end_dt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
                    days_left = (end_dt - now).days
                    hours_left = (end_dt - now).total_seconds() / 3600
                except Exception:
                    pass

            # Skip micro-markets (resolve in < 1 hour) — noise, not signal
            if hours_left is not None and hours_left < 1:
                continue

            if category in blacklisted:
                continue
            # Keyword-based sports blacklist
            if sports_keywords and any(kw in m.get("question","").lower() for kw in sports_keywords):
                continue
            if not (min_price <= price <= max_price):
                continue
            if volume < min_volume or liquidity < min_liquidity:
                continue
            # Only filter by days if endDate is available
            if days_left is not None and not (min_days <= days_left <= max_days):
                continue
            # Skip markets more than 3 days past deadline (unreliable resolution)
            if days_left is not None and days_left < -3:
                continue

            candidates.append({
                "id": m.get("conditionId", m.get("id", "")),
                "numeric_id": str(m.get("id", "")),
                "question": m.get("question", ""),
                "price": price,
                "volume_24h": volume,
                "liquidity": liquidity,
                "end_date": end_date,
                "days_left": days_left,
                "category": category,
                "token_id": m.get("clobTokenIds", []),
                "description": m.get("description", ""),
                "priority": category in preferred,
                # Statistical signal: market 50-60% overprices YES (actual rate 44.7% from 13,967 markets)
                "bet_no_signal": 0.50 <= price <= 0.60,
            })
        except (ValueError, KeyError):
            continue

    # Sort: bet_no_signal first (highest statistical edge), then priority, then soonest resolve
    candidates.sort(key=lambda x: (not x["bet_no_signal"], not x["priority"], x.get("days_left") or 99, -x["volume_24h"]))
    return candidates
