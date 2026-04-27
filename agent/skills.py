"""Skills — callable tools that the LLM can invoke autonomously."""
import os
import requests


def search_news(query: str) -> str:
    api_key = os.getenv("SERPER_API_KEY", "")
    if not api_key:
        return "No news API key configured."
    try:
        resp = requests.post(
            "https://google.serper.dev/news",
            headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
            json={"q": query, "num": int(os.getenv("MAX_NEWS_ARTICLES", 5))},
            timeout=8,
        )
        items = resp.json().get("news", [])
        return "\n".join(f"- {i['title']}: {i.get('snippet', '')}" for i in items) or "No news found."
    except Exception as e:
        return f"News fetch error: {e}"


def get_crypto_price(symbol: str) -> str:
    slug_map = {"BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana", "MATIC": "matic-network"}
    coin_id = slug_map.get(symbol.upper(), symbol.lower())
    try:
        resp = requests.get(
            f"https://api.coingecko.com/api/v3/simple/price",
            params={"ids": coin_id, "vs_currencies": "usd", "include_24hr_change": "true"},
            timeout=8,
        )
        data = resp.json().get(coin_id, {})
        if not data:
            return f"Price not found for {symbol}."
        return f"{symbol.upper()} price: ${data['usd']:,.2f} (24h change: {data.get('usd_24h_change', 0):.2f}%)"
    except Exception as e:
        return f"Price fetch error: {e}"


def get_market_data(market_id: str) -> str:
    try:
        url = f"{os.getenv('POLYMARKET_GAMMA_API', 'https://gamma-api.polymarket.com')}/markets/{market_id}"
        resp = requests.get(url, timeout=8)
        m = resp.json()
        price = float(m.get("lastTradePrice") or 0)
        vol = float(m.get("volume24hr") or 0)
        liq = float(m.get("liquidity") or 0)
        return f"Market '{m.get('question','')}': price={price:.3f}, vol24h=${vol:,.0f}, liquidity=${liq:,.0f}"
    except Exception as e:
        return f"Market data error: {e}"


def calculate_kelly(p_true: float, p_market: float, bankroll: float) -> str:
    edge = p_true - p_market
    if edge > 0:
        fk = edge / (1 - p_market)
        side = "YES"
    else:
        edge = (1 - p_true) - (1 - p_market)
        fk = edge / p_market if p_market > 0 else 0
        side = "NO"
    qk = fk * 0.25 * bankroll
    return f"Side={side}, Full Kelly={fk:.3f}, Quarter Kelly=${qk:.2f} (bankroll=${bankroll:.2f})"


# Tool definitions for Anthropic tool_use API
TOOL_DEFINITIONS = [
    {
        "name": "search_news",
        "description": "Search recent news articles relevant to a prediction market question.",
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string", "description": "Search query"}},
            "required": ["query"],
        },
    },
    {
        "name": "get_crypto_price",
        "description": "Get current price and 24h change for a cryptocurrency.",
        "input_schema": {
            "type": "object",
            "properties": {"symbol": {"type": "string", "description": "Ticker symbol e.g. BTC, ETH"}},
            "required": ["symbol"],
        },
    },
    {
        "name": "get_market_data",
        "description": "Get live Polymarket data for a specific market by condition ID.",
        "input_schema": {
            "type": "object",
            "properties": {"market_id": {"type": "string", "description": "Polymarket conditionId"}},
            "required": ["market_id"],
        },
    },
    {
        "name": "calculate_kelly",
        "description": "Calculate Kelly Criterion position size given probability estimates.",
        "input_schema": {
            "type": "object",
            "properties": {
                "p_true":    {"type": "number", "description": "Your estimated true probability (0-1)"},
                "p_market":  {"type": "number", "description": "Current market price (0-1)"},
                "bankroll":  {"type": "number", "description": "Current bankroll in USD"},
            },
            "required": ["p_true", "p_market", "bankroll"],
        },
    },
]


def execute_tool(name: str, inputs: dict) -> str:
    if name == "search_news":
        return search_news(inputs["query"])
    elif name == "get_crypto_price":
        return get_crypto_price(inputs["symbol"])
    elif name == "get_market_data":
        return get_market_data(inputs["market_id"])
    elif name == "calculate_kelly":
        return calculate_kelly(inputs["p_true"], inputs["p_market"], inputs["bankroll"])
    return f"Unknown tool: {name}"
