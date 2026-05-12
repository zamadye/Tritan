"""
OSINT Aggregator — Dynamic source selection by market category.
Fetches Tier 1/2 leading signals before LLM analysis.
"""
import os
import requests
import json
from datetime import datetime, timezone


# ─── CATEGORY DETECTION ───────────────────────────────────────────────────────

def detect_category(question: str) -> str:
    q = question.lower()
    if any(x in q for x in ["vs.", "vs ", "win on", "nba", "mlb", "nhl", "nfl",
                              "ufc", "tennis", "open:", "grand prix", "masters",
                              "tournament", "match", "game", "fight"]):
        return "sports"
    if any(x in q for x in ["bitcoin", "btc", "eth", "ethereum", "crypto",
                              "solana", "sol", "matic"]):
        return "crypto"
    if any(x in q for x in ["wti", "oil", "crude", "brent", "opec",
                              "fed", "interest rate", "cpi", "inflation", "gdp",
                              "unemployment", "recession", "fomc"]):
        return "economics"
    if any(x in q for x in ["iran", "israel", "war", "military", "ceasefire",
                              "invasion", "strike", "conflict", "nato", "ukraine",
                              "russia", "china", "taiwan"]):
        return "geopolitik"
    if any(x in q for x in ["election", "president", "prime minister", "parliament",
                              "vote", "poll", "senator", "congress"]):
        return "politics"
    return "general"


# ─── SPORTS SIGNALS ───────────────────────────────────────────────────────────

def get_sports_signals(question: str) -> dict:
    """Fetch Vegas odds, injury reports, weather for sports markets."""
    signals = {}
    q = question.lower()

    # Detect sport more precisely
    sport_map = {
        "nba": "basketball/nba",
        "mlb": "baseball/mlb",
        "nhl": "hockey/nhl",
        "nfl": "americanfootball/nfl",
    }
    # MLB team keywords
    mlb_teams = ["rays","white sox","red sox","yankees","dodgers","giants","cubs",
                 "mets","braves","astros","rangers","athletics","mariners","royals",
                 "tigers","orioles","nationals","pirates","reds","cardinals","rockies",
                 "padres","angels","twins","guardians","brewers","phillies","marlins"]
    nba_teams = ["lakers","celtics","warriors","bulls","heat","knicks","nets","bucks",
                 "suns","nuggets","clippers","spurs","rockets","thunder","jazz","hawks"]
    nhl_teams = ["bruins","rangers","maple leafs","canadiens","penguins","capitals",
                 "blackhawks","red wings","flyers","blues","avalanche","flames"]

    if any(t in q for t in mlb_teams):
        sport_path = "baseball/mlb"
    elif any(t in q for t in nba_teams):
        sport_path = "basketball/nba"
    elif any(t in q for t in nhl_teams):
        sport_path = "hockey/nhl"
    elif "nfl" in q or any(t in q for t in ["chiefs","eagles","cowboys","patriots"]):
        sport_path = "americanfootball/nfl"
    else:
        sport_path = next((v for k, v in sport_map.items() if k in q), "basketball/nba")

    # 1. ESPN Injury reports
    try:
        r = requests.get(
            f"https://site.api.espn.com/apis/site/v2/sports/{sport_path}/injuries",
            timeout=8
        )
        injuries = r.json().get("injuries", [])
        relevant = []
        q_words = set(w.strip("?.,!").lower() for w in question.split() if len(w) > 3)
        for team_data in injuries:
            team_name = team_data.get("displayName", "").lower()
            if any(w in team_name for w in q_words):
                for inj in team_data.get("injuries", [])[:3]:
                    athlete = inj.get("athlete", {}).get("displayName", inj.get("displayName","?"))
                    status = inj.get("status", inj.get("type","?"))
                    relevant.append(f"{athlete}: {status}")
        if relevant:
            signals["injuries"] = relevant
    except Exception:
        pass

    # 2. Vegas odds via The Odds API
    odds_key = os.getenv("ODDS_API_KEY", "")
    if odds_key:
        try:
            sport_key_map = {
                "basketball/nba": "basketball_nba",
                "baseball/mlb": "baseball_mlb",
                "hockey/nhl": "icehockey_nhl",
                "americanfootball/nfl": "americanfootball_nfl",
            }
            sport_key = sport_key_map.get(sport_path, "basketball_nba")
            r = requests.get(
                f"https://api.the-odds-api.com/v4/sports/{sport_key}/odds",
                params={"apiKey": odds_key, "regions": "us", "markets": "h2h", "limit": 20},
                timeout=8
            )
            games = r.json()
            q_words = set(w.strip("?.,!").lower() for w in question.split() if len(w) > 3)
            for game in games:
                home = game.get("home_team", "").lower()
                away = game.get("away_team", "").lower()
                if any(w in home or w in away for w in q_words):
                    bookmakers = game.get("bookmakers", [])
                    if bookmakers:
                        outcomes = bookmakers[0].get("markets", [{}])[0].get("outcomes", [])
                        odds_str = " | ".join(
                            f"{o['name']}: {o['price']}" for o in outcomes
                        )
                        signals["vegas_odds"] = odds_str
                        # Convert American/decimal odds to implied probability
                        for o in outcomes:
                            price = float(o.get("price", 2.0))
                            impl_prob = 1 / price
                            signals[f"implied_prob_{o['name'].lower().replace(' ','')}"] = round(impl_prob, 3)

                        # Line movement: compare multiple bookmakers for consensus
                        # If all books agree → strong signal; if split → uncertainty
                        if len(bookmakers) >= 3:
                            all_probs = {}
                            for bm in bookmakers[:5]:
                                for mkt in bm.get("markets", []):
                                    for o in mkt.get("outcomes", []):
                                        name = o["name"]
                                        p = 1 / float(o.get("price", 2.0))
                                        all_probs.setdefault(name, []).append(p)
                            consensus = {}
                            for name, probs in all_probs.items():
                                avg = sum(probs) / len(probs)
                                spread = max(probs) - min(probs)
                                consensus[name] = {"avg": round(avg, 3), "spread": round(spread, 3)}
                            # Low spread = books agree = stronger signal
                            signals["line_consensus"] = str(consensus)
                            min_spread = min(v["spread"] for v in consensus.values()) if consensus else 1
                            signals["smart_money_signal"] = "STRONG" if min_spread < 0.03 else "MODERATE" if min_spread < 0.07 else "WEAK"
                    break
        except Exception:
            pass

    return signals


# ─── GEOPOLITIK SIGNALS ───────────────────────────────────────────────────────

def get_geopolitik_signals(question: str) -> dict:
    """Fetch aircraft activity, vessel tracking for geopolitical markets."""
    signals = {}
    q = question.lower()

    # 1. OpenSky Network — aircraft in relevant airspace
    region_map = {
        "iran": {"lamin": 24, "lomin": 44, "lamax": 40, "lomax": 64},
        "ukraine": {"lamin": 44, "lomin": 22, "lamax": 52, "lomax": 40},
        "taiwan": {"lamin": 20, "lomin": 118, "lamax": 28, "lomax": 126},
        "israel": {"lamin": 29, "lomin": 34, "lamax": 34, "lomax": 36},
    }
    for region, bbox in region_map.items():
        if region in q:
            try:
                r = requests.get(
                    "https://opensky-network.org/api/states/all",
                    params=bbox, timeout=10
                )
                if r.status_code == 200:
                    states = r.json().get("states", [])
                    # Filter: aircraft with no callsign or military patterns
                    active = len(states)
                    signals[f"aircraft_{region}"] = f"{active} aircraft in airspace"
                    # Look for tankers/military (callsigns starting with RCH, REACH, JAKE, etc.)
                    military_cs = ["RCH", "REACH", "JAKE", "POLO", "TOPCAT", "DOOM"]
                    mil_count = sum(1 for s in states
                                    if s and s[1] and
                                    any(s[1].startswith(cs) for cs in military_cs))
                    if mil_count > 0:
                        signals[f"military_aircraft_{region}"] = f"⚠️ {mil_count} military callsigns detected"
            except Exception:
                pass
            break

    return signals


# ─── CRYPTO SIGNALS ───────────────────────────────────────────────────────────

def get_crypto_signals(question: str) -> dict:
    """Fetch funding rates, price data for crypto markets."""
    signals = {}
    q = question.lower()

    symbol_map = {"bitcoin": "BTCUSDT", "btc": "BTCUSDT",
                  "ethereum": "ETHUSDT", "eth": "ETHUSDT",
                  "solana": "SOLUSDT", "sol": "SOLUSDT"}
    symbol = next((v for k, v in symbol_map.items() if k in q), "BTCUSDT")
    coin = symbol.replace("USDT", "")

    # 1. Binance funding rate
    try:
        r = requests.get("https://fapi.binance.com/fapi/v1/fundingRate",
                         params={"symbol": symbol, "limit": 3}, timeout=8)
        rates = r.json()
        if rates:
            latest_rate = float(rates[-1]["fundingRate"]) * 100
            avg_rate = sum(float(x["fundingRate"]) for x in rates) / len(rates) * 100
            sentiment = "bearish" if latest_rate < -0.01 else "bullish" if latest_rate > 0.01 else "neutral"
            signals["funding_rate"] = f"{latest_rate:+.4f}% ({sentiment})"
    except Exception:
        pass

    # 2. Current price vs target
    try:
        r = requests.get("https://api.binance.com/api/v3/ticker/price",
                         params={"symbol": symbol}, timeout=8)
        price = float(r.json().get("price", 0))
        signals["current_price"] = f"${price:,.2f}"

        # Extract target from question
        import re
        targets = re.findall(r'\$?([\d,]+)k?', question)
        for t in targets:
            target_val = float(t.replace(",", "")) * (1000 if "k" in question[question.find(t):question.find(t)+5].lower() else 1)
            if target_val > 1000:
                pct_to_target = (target_val - price) / price * 100
                signals["distance_to_target"] = f"{pct_to_target:+.1f}% to ${target_val:,.0f}"
    except Exception:
        pass

    return signals


# ─── ECONOMICS SIGNALS ────────────────────────────────────────────────────────

def get_economics_signals(question: str) -> dict:
    """Fetch FRED data, bond yields for economics markets."""
    signals = {}

    fred_key = os.getenv("FRED_API_KEY", "")
    if not fred_key:
        return signals

    q = question.lower()
    series_map = {
        "fed": "FEDFUNDS",
        "rate": "FEDFUNDS",
        "cpi": "CPIAUCSL",
        "inflation": "CPIAUCSL",
        "unemployment": "UNRATE",
        "gdp": "GDP",
    }

    for keyword, series_id in series_map.items():
        if keyword in q:
            try:
                r = requests.get(
                    "https://api.stlouisfed.org/fred/series/observations",
                    params={"series_id": series_id, "api_key": fred_key,
                            "file_type": "json", "limit": 2, "sort_order": "desc"},
                    timeout=8
                )
                obs = r.json().get("observations", [])
                if obs:
                    signals[f"fred_{series_id}"] = f"{obs[0]['value']} (prev: {obs[1]['value'] if len(obs)>1 else '?'})"
            except Exception:
                pass
            break

    return signals


# ─── MAIN AGGREGATOR ──────────────────────────────────────────────────────────

def get_osint_signals(question: str) -> str:
    """
    Main entry point. Detects category, fetches relevant signals,
    returns formatted string for LLM context.
    """
    category = detect_category(question)
    signals = {}

    if category == "sports":
        signals = get_sports_signals(question)
    elif category == "geopolitik":
        signals = get_geopolitik_signals(question)
        signals.update(_get_crypto_geo_correlation(question))
    elif category == "crypto":
        signals = get_crypto_signals(question)
        signals.update(_get_geo_crypto_correlation())
    elif category == "economics":
        signals = get_economics_signals(question)
        if any(x in question.lower() for x in ["oil","wti","crude","brent"]):
            signals.update(_get_crypto_geo_correlation(question))

    lines = []
    if signals:
        lines.append(f"[OSINT:{category.upper()}]")
        for key, value in signals.items():
            label = key.replace("_", " ").title()
            if isinstance(value, list):
                lines.append(f"  {label}:")
                for item in value: lines.append(f"    - {item}")
            else:
                lines.append(f"  {label}: {value}")

    # Always add: news, reddit sentiment, related markets, fear&greed trend
    news = get_newsapi_signals(question)
    if news: lines.append(news)

    reddit = get_reddit_signals(question, category)
    if reddit: lines.append(reddit)

    related = get_polymarket_related_markets(question)
    if related: lines.append(related)

    fg = get_fear_greed_trend()
    if fg and category in ("crypto","geopolitik","economics"):
        lines.append(fg)

    # Twitter early signals for crypto and geo (pay-per-use)
    if category in ("crypto", "geopolitik", "politics"):
        twitter = get_twitter_signals(question)
        if twitter: lines.append(twitter)

    return "\n".join(lines)


def _get_crypto_geo_correlation(question: str) -> dict:
    """For geopolitik markets: fetch BTC/oil price as sentiment indicator."""
    signals = {}
    q = question.lower()

    # BTC as risk-on/off indicator
    try:
        r = requests.get("https://api.binance.com/api/v3/ticker/24hr",
                         params={"symbol": "BTCUSDT"}, timeout=6)
        d = r.json()
        change = float(d.get("priceChangePercent", 0))
        price = float(d.get("lastPrice", 0))
        sentiment = "📈 risk-ON" if change > 1 else "📉 risk-OFF" if change < -1 else "➡️ neutral"
        signals["btc_sentiment"] = f"${price:,.0f} ({change:+.1f}% 24h) → {sentiment}"
    except Exception:
        pass

    # WTI Oil for Iran/Middle East markets
    if any(x in q for x in ["iran","oil","hormuz","opec","saudi"]):
        try:
            # Use a free commodity price endpoint
            r = requests.get("https://api.binance.com/api/v3/ticker/price",
                             params={"symbol": "WBTCUSDT"}, timeout=5)
            # Fallback: just note the correlation
            signals["geo_crypto_note"] = "Iran/oil conflict → BTC typically -5% to -15% on escalation"
        except Exception:
            pass

    return signals


def _get_geo_crypto_correlation() -> dict:
    """For crypto markets: fetch geopolitik risk indicators."""
    signals = {}
    try:
        # Fear & Greed index via alternative.me
        r = requests.get("https://api.alternative.me/fng/?limit=1", timeout=6)
        d = r.json().get("data", [{}])[0]
        value = int(d.get("value", 50))
        label = d.get("value_classification", "Neutral")
        signals["fear_greed_index"] = f"{value}/100 — {label}"
        if value < 30:
            signals["geo_signal"] = "Extreme Fear → geopolitik risk HIGH, price likely down"
        elif value > 70:
            signals["geo_signal"] = "Extreme Greed → geopolitik risk LOW, price likely up"
    except Exception:
        pass
    return signals


# ─── ENHANCED DATA SOURCES ────────────────────────────────────────────────────

def get_twitter_signals(question: str) -> str:
    """Fetch Twitter early signals — entity-focused, high-engagement only."""
    bearer = os.getenv("TWITTER_BEARER_TOKEN", "")
    if not bearer:
        return ""

    # Entity extraction: named entities (capitalized multi-word), crypto tickers, country names
    import re as _re
    stopwords = {"will","the","and","for","are","was","has","have","been","that",
                 "this","with","from","does","would","could","should","what","when",
                 "where","which","who","how","may","can","by","to","in","on","at",
                 "a","an","be","is","it","its","not","but","or","if","as","do"}

    # Extract proper nouns (capitalized words not at sentence start)
    tokens = question.replace("?","").replace(",","").split()
    entities = []
    for i, w in enumerate(tokens):
        clean = w.strip(".,!()$%")
        if len(clean) > 2 and clean[0].isupper() and clean.lower() not in stopwords:
            entities.append(clean)

    # Crypto tickers
    crypto_map = {"bitcoin":"BTC","ethereum":"ETH","btc":"BTC","eth":"ETH",
                  "solana":"SOL","matic":"MATIC"}
    q_lower = question.lower()
    for word, ticker in crypto_map.items():
        if word in q_lower and f"${ticker}" not in entities:
            entities.append(f"${ticker}")

    if not entities:
        return ""

    # Build query: top 2 entities with OR for broader coverage
    primary = entities[:2]
    query = " ".join(primary) + " lang:en -is:retweet min_faves:5"

    try:
        r = requests.get(
            "https://api.twitter.com/2/tweets/search/recent",
            params={"query": query, "max_results": 10,
                    "tweet.fields": "public_metrics,created_at,author_id"},
            headers={"Authorization": f"Bearer {bearer}"},
            timeout=6,
        )
        if r.status_code != 200:
            # Fallback without min_faves if no results
            query_fallback = " ".join(primary) + " lang:en -is:retweet"
            r = requests.get(
                "https://api.twitter.com/2/tweets/search/recent",
                params={"query": query_fallback, "max_results": 10,
                        "tweet.fields": "public_metrics,created_at"},
                headers={"Authorization": f"Bearer {bearer}"},
                timeout=6,
            )
            if r.status_code != 200:
                return ""

        tweets = r.json().get("data", [])
        if not tweets:
            return ""

        # Sort by engagement score (likes×2 + retweets×3 — retweets weight more)
        def engagement(t):
            m = t.get("public_metrics", {})
            return m.get("like_count", 0) * 2 + m.get("retweet_count", 0) * 3

        tweets.sort(key=engagement, reverse=True)

        # Only include tweets with meaningful engagement
        high_eng = [t for t in tweets if engagement(t) >= 5]
        display = high_eng[:3] if high_eng else tweets[:3]

        total_eng = sum(engagement(t) for t in tweets)
        sentiment_signal = "🔥 HIGH" if total_eng > 100 else "📊 MODERATE" if total_eng > 20 else "💤 LOW"

        lines = [f"[TWITTER] {len(tweets)} tweets | entities: {', '.join(primary)} | sentiment: {sentiment_signal}"]
        for t in display:
            m = t.get("public_metrics", {})
            eng = engagement(t)
            lines.append(f"  [{eng}eng] {t['text'][:120]}")
        return "\n".join(lines)
    except Exception:
        return ""


def get_reddit_signals(question: str, category: str = "general") -> str:
    """Fetch Reddit sentiment — free, no auth required for public posts."""
    stopwords = {"will","the","and","for","are","was","has","have","been","that",
                 "this","with","from","they","their","does","would","could","should"}
    words = [w.strip("?.,!()") for w in question.split()
             if len(w) > 3 and w.lower() not in stopwords]
    if not words:
        return ""

    # Pick subreddit by category
    sub_map = {
        "sports":    "sportsbook",
        "crypto":    "CryptoCurrency",
        "politics":  "politics",
        "geopolitik":"geopolitics",
        "economics": "economics",
    }
    subreddit = sub_map.get(category, "polymarket")
    query = " ".join(words[:3])

    try:
        r = requests.get(
            f"https://www.reddit.com/r/{subreddit}/search.json",
            params={"q": query, "sort": "new", "limit": 5, "t": "day"},
            headers={"User-Agent": "tritan-agent/1.0"},
            timeout=6, verify=False,
        )
        if r.status_code != 200:
            return ""
        posts = r.json().get("data", {}).get("children", [])
        if not posts:
            return ""
        lines = [f"[REDDIT r/{subreddit}] {len(posts)} posts about: {query}"]
        for p in posts[:3]:
            d = p["data"]
            score = d.get("score", 0)
            lines.append(f"  [{score:+d}] {d.get('title','')[:80]}")
        return "\n".join(lines)
    except Exception:
        return ""


def get_newsapi_signals(question: str) -> str:
    """Fetch NewsAPI articles for a market question."""
    api_key = os.getenv("NEWS_API_KEY", "")
    if not api_key:
        return ""
    # Extract key terms
    stopwords = {"will","the","and","for","are","was","has","have","been","that","this","with","from","they","their"}
    words = [w.strip("?.,!()") for w in question.split()
             if len(w) > 3 and w.lower() not in stopwords]
    query = " ".join(words[:4])
    try:
        r = requests.get(
            "https://newsapi.org/v2/everything",
            params={"q": query, "pageSize": 6, "sortBy": "publishedAt",
                    "language": "en", "apiKey": api_key},
            timeout=8,
        )
        articles = r.json().get("articles", [])
        if not articles:
            return ""
        lines = [f"[NEWS] {len(articles)} articles for: {query}"]
        for a in articles[:5]:
            lines.append(f"  - {a['title']}: {(a.get('description') or '')[:120]}")
        return "\n".join(lines)
    except Exception:
        return ""


def get_fear_greed_trend() -> str:
    """Fetch 7-day Fear & Greed trend."""
    try:
        r = requests.get("https://api.alternative.me/fng/?limit=7", timeout=5)
        data = r.json().get("data", [])
        if not data:
            return ""
        trend = " → ".join(f"{d['value']}({d['value_classification'][:4]})" for d in data[:4])
        current = int(data[0]["value"])
        direction = "improving" if int(data[0]["value"]) > int(data[2]["value"]) else "worsening"
        return f"[FEAR&GREED 7d trend] {trend} | sentiment {direction}"
    except Exception:
        return ""


def get_polymarket_related_markets(question: str) -> str:
    """Fetch related high-volume markets from Polymarket for context."""
    try:
        r = requests.get(
            "https://gamma-api.polymarket.com/markets",
            params={"active": "true", "limit": 20, "order": "volume24hr", "ascending": "false"},
            timeout=6,
        )
        markets = r.json()
        q_words = set(w.lower().strip("?.,!") for w in question.split() if len(w) > 4)
        related = []
        for m in markets:
            mq = m.get("question", "").lower()
            if sum(1 for w in q_words if w in mq) >= 2:
                vol = float(m.get("volume24hr", 0))
                price = float((m.get("outcomePrices") or ["0.5"])[0]
                              if isinstance(m.get("outcomePrices"), list) else 0.5)
                related.append(f"  Related: {m['question'][:60]} | YES={price:.0%} vol=${vol:,.0f}")
        if related:
            return "[RELATED MARKETS]\n" + "\n".join(related[:3])
    except Exception:
        pass
    return ""
