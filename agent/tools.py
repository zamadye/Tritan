"""Tool executor for agentic loop — LLM calls these to verify data and detect gaps."""
import os
import json
import requests
from datetime import datetime, timezone


# ── Tool definitions (sent to LLM) ───────────────────────────────────────────

TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the web for real-time news, events, or information about a topic. Use for breaking news, geopolitical events, general market context.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Specific search query"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_crypto_price",
            "description": "Get current price and 24h change for a cryptocurrency. Use for crypto prediction markets.",
            "parameters": {
                "type": "object",
                "properties": {
                    "coin": {"type": "string", "description": "Coin id: bitcoin, ethereum, solana, etc."}
                },
                "required": ["coin"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_sports_data",
            "description": "Get injury reports and recent results for a sports team or player. Use for sports prediction markets.",
            "parameters": {
                "type": "object",
                "properties": {
                    "sport": {"type": "string", "description": "Sport: nba, mlb, nhl, nfl"},
                    "team":  {"type": "string", "description": "Team name keyword"}
                },
                "required": ["sport"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_market_context",
            "description": "Get related Polymarket markets and their prices to cross-verify sentiment. Use to detect if related markets have already priced in information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Keyword to search related markets"}
                },
                "required": ["keyword"]
            }
        }
    }
]


# ── Tool implementations ──────────────────────────────────────────────────────

def search_web(query: str) -> str:
    # Try Tavily first
    key = os.getenv("TAVILY_API_KEY", "")
    if key:
        try:
            r = requests.post("https://api.tavily.com/search",
                json={"api_key": key, "query": query, "max_results": 4,
                      "search_depth": "basic"}, timeout=8)
            if r.status_code == 200:
                results = r.json().get("results", [])
                if results:
                    lines = []
                    for res in results[:4]:
                        date = res.get("published_date", "")[:10]
                        lines.append(f"[{date}] {res.get('title','')} — {res.get('content','')[:150]}")
                    return "\n".join(lines)
        except Exception:
            pass

    # Fallback: NewsAPI
    news_key = os.getenv("NEWS_API_KEY", "")
    if news_key:
        try:
            r = requests.get("https://newsapi.org/v2/everything",
                params={"q": query[:100], "pageSize": 4, "sortBy": "publishedAt",
                        "language": "en", "apiKey": news_key}, timeout=8)
            if r.status_code == 200:
                articles = r.json().get("articles", [])
                if articles:
                    lines = []
                    for a in articles[:4]:
                        date = (a.get("publishedAt") or "")[:10]
                        lines.append(f"[{date}] {a.get('title','')} — {a.get('description','')[:150]}")
                    return "\n".join(lines)
        except Exception:
            pass

    return f"No search results available for: {query}"


def get_crypto_price(coin: str) -> str:
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price",
            params={"ids": coin.lower(), "vs_currencies": "usd",
                    "include_24hr_change": "true", "include_1hr_change": "true"},
            timeout=6)
        data = r.json().get(coin.lower(), {})
        if not data:
            return f"No price data for {coin}"
        price    = data.get("usd", 0)
        chg_24h  = data.get("usd_24h_change", 0)
        chg_1h   = data.get("usd_1h_change", 0)
        return f"{coin}: ${price:,.2f} | 1h: {chg_1h:+.2f}% | 24h: {chg_24h:+.2f}%"
    except Exception as e:
        return f"get_crypto_price error: {e}"


def get_sports_data(sport: str, team: str = "") -> str:
    sport_map = {"nba": "basketball/nba", "mlb": "baseball/mlb",
                 "nhl": "hockey/nhl", "nfl": "americanfootball/nfl"}
    path = sport_map.get(sport.lower(), "basketball/nba")
    lines = []
    try:
        r = requests.get(
            f"https://site.api.espn.com/apis/site/v2/sports/{path}/injuries",
            timeout=6)
        injuries = r.json().get("injuries", [])
        team_kw = team.lower()
        for td in injuries:
            tname = td.get("displayName", "").lower()
            if team_kw and team_kw not in tname:
                continue
            for inj in td.get("injuries", [])[:3]:
                name   = inj.get("athlete", {}).get("displayName", "?")
                status = inj.get("status", "?")
                pos    = inj.get("athlete", {}).get("position", {}).get("abbreviation", "")
                lines.append(f"INJURY [{tname}] {name} ({pos}): {status}")
        if not lines:
            lines.append(f"No injury data found for {sport} {team}")
    except Exception as e:
        lines.append(f"get_sports_data error: {e}")
    return "\n".join(lines[:8])


def get_market_context(keyword: str) -> str:
    try:
        r = requests.get(
            f"{os.getenv('POLYMARKET_GAMMA_API','https://gamma-api.polymarket.com')}/markets",
            params={"active": "true", "limit": 10, "order": "volume24hr",
                    "ascending": "false"}, timeout=6)
        markets = r.json()
        kw = keyword.lower()
        related = [m for m in markets
                   if kw in m.get("question","").lower()][:5]
        if not related:
            return f"No related markets found for '{keyword}'"
        lines = []
        for m in related:
            op = m.get("outcomePrices", ["0.5"])
            price = float(op[0]) if isinstance(op, list) else 0.5
            vol = float(m.get("volume24hr", 0))
            lines.append(f"[YES={price:.0%} vol=${vol:,.0f}] {m.get('question','')[:70]}")
        return "\n".join(lines)
    except Exception as e:
        return f"get_market_context error: {e}"


# ── Dispatcher ────────────────────────────────────────────────────────────────

def execute_tool(name: str, args: dict) -> str:
    """Execute a tool call from LLM and return result as string."""
    if name == "search_web":
        return search_web(args.get("query", ""))
    elif name == "get_crypto_price":
        return get_crypto_price(args.get("coin", "bitcoin"))
    elif name == "get_sports_data":
        return get_sports_data(args.get("sport", "nba"), args.get("team", ""))
    elif name == "get_market_context":
        return get_market_context(args.get("keyword", ""))
    return f"Unknown tool: {name}"
