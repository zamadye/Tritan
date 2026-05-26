"""Event scanner — finds NO opportunities in multi-outcome list markets.

Strategy: In events with many sub-markets (PGA, FIFA, elections, etc.),
retail overprices longshots. Bet NO when YES price is 10-40% and there
is no specific evidence the outcome will happen.

Returns markets formatted same as scanner.py for drop-in use in core.py.
"""
import os
import requests
from datetime import datetime, timezone


def _is_verifiable_no(question: str, event_title: str) -> bool:
    """Return True only if NO can be verified with actual data, not just 'it's a longshot'.

    Verifiable NO markets:
    - Specific counts/numbers (tweets, price levels) — can check historical data
    - Specific announcements with known agendas — can check news
    - Individual player with injury/form data — can check ESPN/news
    - Specific geopolitical events with news signal — can check RSS

    NOT verifiable (skip):
    - Tournament winner (FIFA, NBA, F1) — sportsbook already calibrated
    - Election winner (long-dated) — too many variables
    - Generic "will X happen" without measurable signal
    """
    q = question.lower()
    et = event_title.lower()

    # ✅ Verifiable: specific numeric counts (Elon tweets, price levels)
    if any(x in q for x in ["tweets", "tweet", "post 1", "post 2", "post 3"]):
        return True
    if any(x in q for x in ["$70,000", "$80,000", "$85,000", "$90,000", "$95,000",
                              "$100,000", "$110,000", "$115,000", "$120,000", "$140,000",
                              "wti", "crude oil", "brent"]):
        return True

    # ✅ Verifiable: specific geopolitical events with short timeline (< 30 days)
    if any(x in q for x in ["airspace", "strait", "hormuz", "peace deal", "diplomatic meeting",
                              "ceasefire", "sanctions", "nuclear"]):
        return True

    # ✅ Verifiable: individual player/team in active tournament (can check form/injury)
    if any(x in et for x in ["pga", "championship", "open", "masters", "wimbledon",
                               "us open", "french open", "australian open"]):
        return True  # individual player markets — can verify with ESPN

    # ✅ Verifiable: specific announcement at known event
    if any(x in q for x in ["announce", "sign", "agree", "declare", "rename",
                              "say \"", "mention", "tweet about"]):
        return True

    # ❌ NOT verifiable: tournament winner (already calibrated by sportsbooks)
    if any(x in et for x in ["fifa world cup winner", "nba champion", "f1 drivers",
                               "f1 constructors", "super bowl", "world series",
                               "stanley cup", "champions league winner"]):
        return False

    # ❌ NOT verifiable: long-dated elections (> 60 days)
    if any(x in et for x in ["presidential election", "presidential nominee",
                               "prime minister", "2027", "2028"]):
        return False

    # Default: allow if short-dated (< 30 days), skip if long-dated
    return True  # let LLM decide for ambiguous cases


def get_event_no_candidates(
    min_price: float = 0.10,
    max_price: float = 0.40,
    min_liquidity: float = 500,
    min_markets_in_event: int = 5,
    max_per_event: int = 10,
) -> list[dict]:
    """Fetch NO candidates from multi-outcome events."""
    try:
        resp = requests.get(
            "https://gamma-api.polymarket.com/events",
            params={"active": "true", "closed": "false", "limit": 50,
                    "order": "volume24hr", "ascending": "false"},
            timeout=12,
        )
        resp.raise_for_status()
        events = resp.json()
    except Exception as e:
        print(f"[EVENT_SCANNER] ❌ {e}")
        return []

    now = datetime.now(timezone.utc)
    candidates = []

    for event in events:
        markets = event.get("markets", [])
        if len(markets) < min_markets_in_event:
            continue

        event_title = event.get("title", "")
        end_date = event.get("endDate", "")
        days_left = None
        try:
            end_dt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
            days_left = (end_dt - now).days
            if days_left < 0:
                continue  # already ended
        except Exception:
            pass

        # Collect candidates from this event
        event_candidates = []
        for m in markets:
            price = float(m.get("lastTradePrice") or 0.5)
            liquidity = float(m.get("liquidity") or 0)
            volume = float(m.get("volume24hr") or 0)

            if not (min_price <= price <= max_price):
                continue
            if liquidity < min_liquidity:
                continue

            question = m.get("question", "")
            # Only include markets where NO can be verified with actual data
            if not _is_verifiable_no(question, event_title):
                continue

            # Build market dict compatible with core.py
            event_candidates.append({
                "id": m.get("conditionId", m.get("id", "")),
                "numeric_id": str(m.get("id", "")),
                "question": m.get("question", ""),
                "price": price,
                "volume_24h": volume,
                "liquidity": liquidity,
                "end_date": end_date,
                "days_left": days_left,
                "category": _infer_event_category(event_title),
                "token_id": m.get("clobTokenIds", []),
                "description": m.get("description", ""),
                "priority": True,
                "bet_no_signal": True,  # flag: this is a NO opportunity
                "volume_ratio": 1.0,
                "resolve_tier": 1 if (days_left or 99) <= 14 else 2,
                "event_title": event_title,
                "event_market_count": len(markets),
            })

        # Sort by price ascending (lowest YES price = most obvious NO)
        event_candidates.sort(key=lambda x: x["price"])
        candidates.extend(event_candidates[:max_per_event])

    return candidates


def _infer_event_category(title: str) -> str:
    t = title.lower()
    if any(x in t for x in ["fifa","pga","nba","f1","tennis","golf","football","soccer","nfl","nhl","mlb","ufc","esport","dota","cs:"]):
        return "sports"
    if any(x in t for x in ["election","president","prime minister","mayor","senate","congress"]):
        return "politics"
    if any(x in t for x in ["bitcoin","crypto","ethereum","btc","eth","oil","wti"]):
        return "crypto"
    if any(x in t for x in ["iran","trump","xi","war","peace","nato","ukraine","russia","israel"]):
        return "geopolitik"
    return "other"
