"""Sports data — ESPN public API (no key) + geopolitik signals."""
import requests

ESPN = "https://site.api.espn.com/apis/site/v2/sports"

SPORTS = {
    "nba": f"{ESPN}/basketball/nba",
    "mlb": f"{ESPN}/baseball/mlb",
    "nhl": f"{ESPN}/hockey/nhl",
    "nfl": f"{ESPN}/americanfootball/nfl",
    "soccer": f"{ESPN}/soccer/eng.1",
    "ufc": f"{ESPN}/mma/ufc",
}


def _detect_sport(q: str) -> str:
    q = q.lower()
    if any(x in q for x in ["fc","united","city","arsenal","chelsea","liverpool","madrid","barcelona","soccer","mls"]):
        return "soccer"
    if any(x in q for x in ["mlb","yankees","dodgers","astros","sox","cubs"]):
        return "mlb"
    if any(x in q for x in ["nhl","hockey","bruins","rangers","leafs","penguins"]):
        return "nhl"
    if any(x in q for x in ["nfl","chiefs","eagles","cowboys","patriots","49ers"]):
        return "nfl"
    if any(x in q for x in ["ufc","mma","fight","bout","lightweight","heavyweight"]):
        return "ufc"
    return "nba"


def get_game_context(question: str) -> str:
    """Fetch real-time ESPN data for a sports market question."""
    sport = _detect_sport(question)
    base = SPORTS.get(sport, SPORTS["nba"])
    lines = []

    try:
        r = requests.get(f"{base}/scoreboard", timeout=8)
        events = r.json().get("events", [])
        q_words = set(w.lower().strip("?.,!") for w in question.split() if len(w) > 3)

        for event in events:
            name = event.get("name", "").lower()
            # Match if any team name word appears in question
            if not any(w in name for w in q_words):
                continue

            comp = event.get("competitions", [{}])[0]
            status = event.get("status", {}).get("type", {}).get("description", "scheduled")
            lines.append(f"[ESPN] {event.get('name')} | {status}")

            for c in comp.get("competitors", []):
                team = c.get("team", {}).get("displayName", "?")
                rec = c.get("records", [{}])
                record = rec[0].get("summary", "?") if rec else "?"
                ha = c.get("homeAway", "?").upper()
                score = c.get("score", "-")
                lines.append(f"  {ha}: {team} | Record: {record} | Score: {score}")

            # Bookmaker odds if available
            odds = comp.get("odds", [])
            if odds:
                o = odds[0]
                lines.append(f"  Odds: {o.get('details','?')} | O/U: {o.get('overUnder','?')}")
            break

    except Exception as e:
        lines.append(f"ESPN unavailable: {e}")

    return "\n".join(lines)


def get_geopolitik_signals(question: str) -> str:
    """Structured signals for geopolitical markets."""
    q = question.lower()
    hints = []
    if "iran" in q:
        hints.append("Iran market: check ceasefire status, military activity, diplomatic talks.")
    if "trump" in q or "tariff" in q:
        hints.append("US trade policy: check White House announcements, trade deal updates.")
    if "fed" in q or "interest rate" in q:
        hints.append("Fed policy: CME FedWatch implied probability is key base rate.")
    if any(x in q for x in ["election","prime minister","president","parliament"]):
        hints.append("Political market: incumbent advantage, latest polls, institutional control.")
    if any(x in q for x in ["btc","bitcoin","eth","crypto"]):
        hints.append("Crypto market: check current price vs target on Binance/Coinbase.")
    return "\n".join(hints)


def get_sports_context(question: str) -> str:
    """Combined sports + geopolitik + crypto context for analyzer."""
    q = question.lower()
    is_sports = any(x in q for x in [
        "vs","win on","nba","nfl","mlb","nhl","ufc","mma","tennis","soccer",
        "fc","warriors","lakers","celtics","spurs","nuggets","clippers",
        "masters","tournament","match","game","fight","bout","open"
    ])
    is_geo = any(x in q for x in [
        "iran","trump","tariff","fed","rate","election","president",
        "prime minister","war","military","ceasefire","peace"
    ])
    is_crypto = any(x in q for x in ["bitcoin","btc","eth","ethereum","crypto","solana","sol"])

    parts = []
    if is_sports:
        ctx = get_game_context(question)
        if ctx:
            parts.append(ctx)
    if is_geo:
        sig = get_geopolitik_signals(question)
        if sig:
            parts.append(sig)
    if is_crypto:
        price_ctx = _get_crypto_price(question)
        if price_ctx:
            parts.append(price_ctx)

    return "\n".join(parts)


def _get_crypto_price(question: str) -> str:
    """Fetch real-time crypto price from CoinGecko."""
    import requests
    q = question.lower()
    coin_map = {
        "bitcoin": "bitcoin", "btc": "bitcoin",
        "ethereum": "ethereum", "eth": "ethereum",
        "solana": "solana", "sol": "solana",
    }
    coin_id = next((v for k, v in coin_map.items() if k in q), None)
    if not coin_id:
        return ""
    try:
        r = requests.get(
            f"https://api.coingecko.com/api/v3/simple/price",
            params={"ids": coin_id, "vs_currencies": "usd", "include_24hr_change": "true",
                    "include_7d_change": "true"},
            timeout=8,
        )
        data = r.json().get(coin_id, {})
        price = data.get("usd", 0)
        change_24h = data.get("usd_24h_change", 0)
        change_7d = data.get("usd_7d_change", 0)
        return (f"[LIVE PRICE] {coin_id.upper()}: ${price:,.2f} | "
                f"24h: {change_24h:+.1f}% | 7d: {change_7d:+.1f}%")
    except Exception:
        return ""
