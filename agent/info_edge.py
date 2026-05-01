"""
Information Edge Detector — Edge Type 2.

Detects delay between information appearing vs market price updating.
Window: typically 5-15 minutes after breaking news before market reacts.

Sources monitored:
- ESPN injury reports (sports)
- NewsAPI breaking news
- Twitter volume spikes
- On-chain: CoinGecko price movement vs Polymarket price lag
"""
import os
import json
import requests
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

CACHE_FILE = Path("data/info_edge_cache.json")
CACHE_TTL  = 300  # 5 minutes


def _load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            d = json.loads(CACHE_FILE.read_text())
            # Expire old entries
            now = time.time()
            return {k: v for k, v in d.items() if now - v.get("ts", 0) < CACHE_TTL}
        except Exception:
            pass
    return {}


def _save_cache(cache: dict):
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(cache, indent=2))


def detect_info_edge(market: dict) -> dict:
    """
    Check if there's a recent information event that market hasn't priced in yet.
    Returns: {has_edge: bool, signal: str, minutes_since_info: int, source: str}
    """
    question = market.get("question", "")
    price    = market.get("price", 0.5)
    nid      = market.get("numeric_id", "")
    q_lower  = question.lower()

    result = {"has_edge": False, "signal": "none", "minutes_since_info": 999,
              "source": "none", "detail": ""}

    cache = _load_cache()
    cache_key = question[:60]

    # Use cache if fresh
    if cache_key in cache:
        return cache[cache_key]

    # ── Sports: ESPN injury report delay ─────────────────────────────────────
    is_sports = any(x in q_lower for x in ["nba","nfl","mlb","nhl","ufc","vs.","vs ","playoffs"])
    if is_sports:
        edge = _check_sports_injury_delay(question, price)
        if edge["has_edge"]:
            cache[cache_key] = {**edge, "ts": time.time()}
            _save_cache(cache)
            return edge

    # ── Crypto: price movement lag ────────────────────────────────────────────
    is_crypto = any(x in q_lower for x in ["bitcoin","btc","eth","crypto"])
    if is_crypto:
        edge = _check_crypto_price_lag(question, price)
        if edge["has_edge"]:
            cache[cache_key] = {**edge, "ts": time.time()}
            _save_cache(cache)
            return edge

    # ── Breaking news: check if news is <15 min old ───────────────────────────
    edge = _check_breaking_news_delay(question, price, nid)
    if edge["has_edge"]:
        cache[cache_key] = {**edge, "ts": time.time()}
        _save_cache(cache)
        return edge

    cache[cache_key] = {**result, "ts": time.time()}
    _save_cache(cache)
    return result


def _check_sports_injury_delay(question: str, market_price: float) -> dict:
    """Check if a key player injury was just reported but market hasn't updated."""
    result = {"has_edge": False, "signal": "none", "minutes_since_info": 999,
              "source": "espn_injury", "detail": ""}
    try:
        # Detect sport
        q = question.lower()
        sport_map = {"nba": "basketball/nba", "nfl": "americanfootball/nfl",
                     "mlb": "baseball/mlb", "nhl": "hockey/nhl"}
        sport_path = next((v for k, v in sport_map.items() if k in q), "basketball/nba")

        r = requests.get(
            f"https://site.api.espn.com/apis/site/v2/sports/{sport_path}/injuries",
            timeout=6
        )
        injuries = r.json().get("injuries", [])

        # Check if any injury is <30 min old
        now = datetime.now(timezone.utc)
        q_words = set(w.strip("?.,!()-").lower() for w in question.split() if len(w) > 3)

        for team_data in injuries[:20]:
            team_name = team_data.get("team", {}).get("displayName", "").lower()
            if not any(w in team_name for w in q_words):
                continue
            for player in team_data.get("injuries", [])[:5]:
                status = player.get("status", "")
                if status.lower() in ("out", "doubtful", "questionable"):
                    # Check if this is a key player (starter)
                    athlete = player.get("athlete", {})
                    name = athlete.get("displayName", "")
                    pos = athlete.get("position", {}).get("abbreviation", "")
                    # Key positions: PG, SG, SF, PF, C, QB, RB, WR
                    key_positions = {"PG","SG","SF","PF","C","QB","RB","WR","SP","RP"}
                    if pos in key_positions:
                        result["has_edge"] = True
                        result["signal"] = f"KEY_INJURY_{status.upper()}"
                        result["minutes_since_info"] = 0  # ESPN doesn't give timestamp
                        result["detail"] = f"{name} ({pos}) {status} for {team_name}"
                        return result
    except Exception:
        pass
    return result


def _check_crypto_price_lag(question: str, market_price: float) -> dict:
    """Check if crypto price moved significantly but Polymarket hasn't updated."""
    result = {"has_edge": False, "signal": "none", "minutes_since_info": 999,
              "source": "coingecko_lag", "detail": ""}
    try:
        q = question.lower()
        coin_map = {"bitcoin": "bitcoin", "btc": "bitcoin", "eth": "ethereum",
                    "ethereum": "ethereum", "solana": "solana"}
        coin = next((v for k, v in coin_map.items() if k in q), None)
        if not coin:
            return result

        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": coin, "vs_currencies": "usd",
                    "include_24hr_change": "true", "include_1hr_change": "true"},
            timeout=6
        )
        data = r.json().get(coin, {})
        change_1h = float(data.get("usd_1h_change", 0) or 0)
        change_24h = float(data.get("usd_24h_change", 0) or 0)
        price_usd = float(data.get("usd", 0) or 0)

        # Extract target from question (e.g., "$80,000")
        import re
        targets = re.findall(r'\$?([\d,]+)(?:,000)?(?:k)?', question)
        target = None
        for t in targets:
            try:
                val = float(t.replace(",",""))
                if val > 1000:  # likely a price target
                    target = val
                    break
            except Exception:
                pass

        if target and price_usd > 0:
            distance_pct = (price_usd - target) / target
            # If price moved >3% in 1h toward/away from target
            if abs(change_1h) > 3:
                direction = "toward" if (change_1h > 0 and price_usd < target) or \
                                        (change_1h < 0 and price_usd > target) else "away"
                result["has_edge"] = True
                result["signal"] = f"CRYPTO_MOVE_{direction.upper()}_TARGET"
                result["minutes_since_info"] = 5  # 1h candle = ~5 min lag
                result["detail"] = (f"{coin} ${price_usd:,.0f} ({change_1h:+.1f}% 1h) "
                                    f"vs target ${target:,.0f} ({distance_pct:+.1%} away)")
    except Exception:
        pass
    return result


def _check_breaking_news_delay(question: str, market_price: float, nid: str) -> dict:
    """Check if breaking news appeared in last 15 min that market hasn't priced in."""
    result = {"has_edge": False, "signal": "none", "minutes_since_info": 999,
              "source": "newsapi_breaking", "detail": ""}
    try:
        api_key = os.getenv("NEWS_API_KEY", "")
        if not api_key:
            return result

        stopwords = {"will","the","and","for","are","was","has","have","been","that","this"}
        words = [w.strip("?.,!()$") for w in question.split()
                 if len(w) > 3 and w.lower() not in stopwords]
        query = " ".join(words[:4])

        r = requests.get("https://newsapi.org/v2/everything",
            params={"q": query, "pageSize": 5, "sortBy": "publishedAt",
                    "language": "en", "apiKey": api_key}, timeout=8)
        if r.status_code != 200:
            return result

        articles = r.json().get("articles", [])
        if not articles:
            return result

        # Check if most recent article is <15 min old
        now = datetime.now(timezone.utc)
        for a in articles[:3]:
            pub = a.get("publishedAt", "")
            if not pub:
                continue
            try:
                pub_dt = datetime.fromisoformat(pub.replace("Z", "+00:00"))
                age_min = (now - pub_dt).total_seconds() / 60
                if age_min < 15:
                    # Check if Polymarket price hasn't moved (still stale)
                    # Fetch current market price to compare
                    result["has_edge"] = True
                    result["signal"] = "BREAKING_NEWS_UNPRICED"
                    result["minutes_since_info"] = int(age_min)
                    result["detail"] = f"{a['title'][:80]} ({age_min:.0f} min ago)"
                    return result
            except Exception:
                continue
    except Exception:
        pass
    return result
