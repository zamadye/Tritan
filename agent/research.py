"""
Research Engine — Fetch, summarize, and find causal patterns before betting.

Flow:
1. Fetch all relevant data (news, macro, sports stats, market data)
2. Build causal chain: Event A → Effect B → Market Impact C
3. Save research report to data/research/
4. Return structured context for LLM analyzer
"""
import os
import json
import requests
from datetime import datetime, timezone
from pathlib import Path


RESEARCH_DIR = Path("data/research")
RESEARCH_DIR.mkdir(parents=True, exist_ok=True)


# ── MACRO ECONOMY DATA ────────────────────────────────────────────────────────

def get_macro_context() -> dict:
    """Fetch key macro indicators that affect ALL markets."""
    macro = {}

    # Fed Funds Rate + expectations (CME FedWatch via Polymarket proxy)
    try:
        r = requests.get(
            "https://gamma-api.polymarket.com/markets",
            params={"active": "true", "limit": 50, "order": "volume24hr", "ascending": "false"},
            timeout=6,
        )
        markets = r.json()
        fed_markets = [m for m in markets if "fed" in m.get("question","").lower()
                       or "rate" in m.get("question","").lower()
                       or "fomc" in m.get("question","").lower()]
        if fed_markets:
            macro["fed_expectations"] = [
                f"{m['question'][:60]} → YES={float((m.get('outcomePrices') or ['0.5'])[0] if isinstance(m.get('outcomePrices'),list) else 0.5):.0%}"
                for m in fed_markets[:3]
            ]
    except Exception:
        pass

    # Fear & Greed 7-day trend
    try:
        r = requests.get("https://api.alternative.me/fng/?limit=7", timeout=5)
        data = r.json().get("data", [])
        if data:
            vals = [int(d["value"]) for d in data]
            trend = "improving" if vals[0] > vals[3] else "deteriorating"
            macro["fear_greed"] = {
                "current": f"{vals[0]}/100 ({data[0]['value_classification']})",
                "7d_trend": trend,
                "values": vals[:7],
            }
    except Exception:
        pass

    # BTC as global risk sentiment proxy (CoinGecko)
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": "bitcoin,ethereum", "vs_currencies": "usd",
                    "include_24hr_change": "true", "include_7d_in_currency": "true"},
            timeout=6,
        )
        d = r.json()
        btc = d.get("bitcoin", {})
        macro["crypto_sentiment"] = {
            "btc_price": btc.get("usd", 0),
            "btc_24h": btc.get("usd_24h_change", 0),
            "risk_signal": "risk-ON" if btc.get("usd_24h_change", 0) > 1 else
                           "risk-OFF" if btc.get("usd_24h_change", 0) < -1 else "neutral",
        }
    except Exception:
        pass

    return macro


# ── CAUSAL CHAIN BUILDER ──────────────────────────────────────────────────────

CAUSAL_CHAINS = {
    # ── GEOPOLITICAL ──────────────────────────────────────────────────────────
    "hormuz": [
        "Strait of Hormuz closure → oil shipping disrupted → oil price +15-30%",
        "Oil price spike → shipping costs rise → plastic/chemical/fertilizer prices rise",
        "Oil spike → inflation pressure → Fed less likely to cut rates → BTC falls",
        "Oil spike → airline costs rise → travel stocks fall → recession risk",
        "Hormuz reopens → oil price -10-20% → inflation eases → Fed dovish → BTC rallies",
    ],
    "iran": [
        "Iran-US tension escalates → oil supply risk → WTI crude +5-15%",
        "Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls",
        "Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally",
        "Iran military strike → oil spike → global inflation → Fed hawkish",
        "Iran sanctions tighten → crypto adoption in Iran increases (capital flight)",
    ],
    "ukraine": [
        "Ukraine conflict escalates → wheat/grain prices rise → food inflation globally",
        "Ukraine ceasefire → European energy prices fall → EUR strengthens vs USD",
        "Russia sanctions tighten → energy supply disruption → EU recession risk",
        "Ukraine peace deal → European reconstruction spending → EUR strengthens",
        "Russia oil embargo → global oil supply shock → inflation spike",
    ],
    "china": [
        "China-Taiwan tension → semiconductor supply disruption → tech stocks fall",
        "China economic slowdown → commodity demand falls → oil/copper/iron prices fall",
        "China stimulus announced → commodity demand rises → AUD/BRL strengthen",
        "China property crisis deepens → global risk-OFF → BTC falls",
        "China trade surplus grows → USD/CNY pressure → EM currency stress",
    ],
    "tariff": [
        "US tariffs on China → supply chain disruption → consumer prices rise 2-5%",
        "Trade war escalation → USD strengthens → EM currencies weaken → crypto falls",
        "Tariff reduction/deal → risk-ON → equities/crypto rally 5-15%",
        "Tariff on steel/aluminum → manufacturing costs rise → inflation",
        "Retaliatory tariffs → US agricultural exports fall → farm sector stress",
    ],

    # ── MONETARY POLICY ───────────────────────────────────────────────────────
    "fed_cut": [
        "Fed rate cut → USD weakens → BTC/gold rally (inverse USD correlation)",
        "Fed rate cut → mortgage rates fall → housing market recovers",
        "Fed cut signals recession fear → equities initially fall then rally",
        "Fed cut → yield curve steepens → bank stocks rally",
        "Surprise Fed cut → immediate BTC +5-10% within 24h",
    ],
    "fed_hike": [
        "Fed rate hike → USD strengthens → BTC/gold fall",
        "Fed hike → bond yields rise → tech/growth stocks fall (higher discount rate)",
        "Fed hike → credit tightens → crypto lending platforms stressed",
        "Fed hike → mortgage rates rise → housing market cools",
        "Surprise Fed hike → immediate BTC -8-15% within 24h",
    ],
    "fed": [
        "FOMC meeting → market volatility spikes 24h before and after",
        "Fed pause (hold) → uncertainty → BTC sideways, then direction from guidance",
        "Fed hawkish language → USD up → BTC/gold down",
        "Fed dovish language → USD down → BTC/gold up",
    ],
    "inflation": [
        "CPI above expectations → Fed hawkish → rate cut delayed → BTC falls",
        "CPI below expectations → Fed dovish → rate cut sooner → BTC rallies",
        "Inflation sticky → consumer spending falls → recession risk rises",
        "Core PCE above 2.5% → Fed holds rates → USD strong → EM stress",
        "Deflation risk → Fed emergency cut → BTC/gold spike",
    ],
    "unemployment": [
        "Unemployment rises → Fed more likely to cut → BTC/equities rally",
        "Unemployment falls (strong jobs) → Fed holds rates → USD strong → BTC flat",
        "Jobless claims spike → recession signal → risk-OFF → BTC falls -5-10%",
        "NFP miss → Fed dovish pivot → BTC +3-8% within 48h",
        "NFP beat → Fed hawkish → BTC -3-5% within 24h",
    ],

    # ── CRYPTO SPECIFIC ───────────────────────────────────────────────────────
    "bitcoin": [
        "BTC within 3% of round number ($80k/$90k) → gamma squeeze → price accelerates",
        "BTC ETF inflows spike → institutional buying → price +5-15%",
        "BTC ETF outflows → selling pressure → price -5-10%",
        "BTC halving approaching → supply shock narrative → price rally",
        "Crypto exchange hack/collapse → panic selling → BTC -15-30%",
        "Whale accumulation (on-chain) → supply squeeze → price up",
        "Miner capitulation → hash rate falls → price bottom signal",
    ],
    "btc": [
        "BTC dominance rising → altcoins falling → BTC relatively strong",
        "BTC options expiry (monthly) → volatility spike → direction unclear",
        "BTC funding rate negative → shorts dominant → potential short squeeze up",
        "BTC funding rate very positive → longs dominant → potential long squeeze down",
    ],
    "crypto": [
        "Regulatory clarity (positive) → institutional adoption → price rally",
        "Regulatory crackdown → exchange delistings → price fall",
        "Stablecoin depeg → contagion risk → broad crypto sell-off",
        "DeFi hack → TVL falls → sector rotation out of DeFi",
    ],

    # ── SPORTS ───────────────────────────────────────────────────────────────
    "nba": [
        "Star player injury (day-to-day) → team win probability falls 10-20%",
        "Star player returns from injury → team win probability rises 15-25%",
        "Home court advantage → home team wins 60% of playoff games historically",
        "Team on 3+ game win streak → momentum factor → +5% win probability",
        "Back-to-back games → fatigue factor → road team disadvantage increases",
        "Coaching change mid-series → uncertainty → slight underdog advantage",
    ],
    "nfl": [
        "Starting QB injury → team win probability falls 20-35%",
        "Weather (rain/snow/wind >20mph) → passing game disrupted → under on points",
        "Home playoff game → home team wins 65% historically",
        "Bye week advantage → rested team +5% win probability",
    ],
    "mlb": [
        "Starting pitcher ERA below 3.0 → team win probability +15%",
        "Bullpen ERA above 5.0 → late-game collapse risk",
        "Home run park factor → high-scoring game more likely",
        "Day game after night game → fatigue factor for hitters",
    ],
    "tennis": [
        "Clay court specialist vs hard court player → clay specialist +20% on clay",
        "Player coming off injury → stamina risk in long matches",
        "Head-to-head record matters more in tennis than other sports",
        "Top seed vs qualifier → top seed wins 80%+ in early rounds",
    ],
    "ufc": [
        "Grappler vs striker → grappler wins if fight goes to ground",
        "Significant strike differential → striker wins 70% if +50 strikes/round",
        "Late replacement fighter → -15% win probability due to camp disruption",
        "Weight cut issues → performance degradation in later rounds",
    ],

    # ── TECHNOLOGY/AI ─────────────────────────────────────────────────────────
    "openai": [
        "OpenAI product launch → competitor stocks fall (GOOG, MSFT react)",
        "OpenAI funding round → AI sector sentiment improves → AI stocks rally",
        "OpenAI safety controversy → regulatory scrutiny → sector uncertainty",
    ],
    "ai": [
        "Major AI model release → benchmark competition → sector excitement",
        "AI regulation proposed → uncertainty → AI stocks fall short-term",
        "AI chip shortage → NVIDIA revenue beats → AI infrastructure stocks rally",
        "AI energy demand → data center power stocks rally",
    ],

    # ── FOREX/MACRO ───────────────────────────────────────────────────────────
    "eur": [
        "ECB rate cut → EUR weakens vs USD → EUR/USD falls",
        "EU GDP beats expectations → EUR strengthens",
        "EU political crisis (elections) → EUR uncertainty → falls",
        "EUR/USD above 1.10 → European exports competitive → EU stocks rally",
    ],
    "dollar": [
        "USD strengthens → EM debt stress → EM currencies fall",
        "USD weakens → commodity prices rise (oil/gold priced in USD)",
        "DXY above 105 → BTC historically falls → risk-OFF signal",
        "DXY below 100 → BTC historically rallies → risk-ON signal",
    ],
    "oil": [
        "OPEC production cut → oil price +5-15%",
        "OPEC production increase → oil price -5-10%",
        "US shale production rises → oil price ceiling effect",
        "Oil above $90 → inflation pressure → Fed hawkish → BTC falls",
        "Oil below $60 → deflation risk → Fed dovish → BTC rallies",
        "Oil price spike → airline/shipping stocks fall → consumer discretionary falls",
    ],
    "gold": [
        "Gold above $3000 → safe haven demand high → risk-OFF environment",
        "Gold falls → risk-ON → equities/crypto rally",
        "Gold/BTC correlation positive → both move together in macro stress",
        "Central bank gold buying → long-term price support",
    ],
}


def detect_causal_chains(question: str, news_text: str) -> list:
    """Detect which causal chains are relevant to this market."""
    combined = (question + " " + news_text).lower()
    relevant = []
    for keyword, chains in CAUSAL_CHAINS.items():
        if keyword in combined:
            relevant.extend(chains)
    return relevant[:6]  # max 6 chains


# ── SPORTS DEEP RESEARCH ──────────────────────────────────────────────────────

def get_sports_deep_context(question: str) -> dict:
    """Fetch team records, player stats, recent form for sports markets."""
    q = question.lower()
    context = {}

    # Detect teams from question
    # ESPN scoreboard + team stats
    sport_map = {
        "nba": ("basketball/nba", ["pistons","magic","celtics","knicks","heat","bucks","sixers","nets","bulls","hawks","wizards","hornets","pacers","cavaliers","raptors","warriors","lakers","clippers","suns","nuggets","thunder","blazers","jazz","kings","spurs","rockets","grizzlies","pelicans","mavs","mavericks","timberwolves"]),
        "mlb": ("baseball/mlb", ["yankees","dodgers","astros","sox","cubs","mets","braves","phillies","cardinals","giants","padres","mariners","twins","tigers","royals","angels","athletics","rangers","orioles","rays","blue jays","nationals","reds","pirates","brewers","rockies","diamondbacks","marlins"]),
        "nfl": ("americanfootball/nfl", ["chiefs","eagles","cowboys","patriots","49ers","rams","bills","ravens","bengals","browns","steelers","titans","colts","jaguars","texans","broncos","raiders","chargers","seahawks","cardinals","falcons","saints","buccaneers","panthers","bears","lions","packers","vikings","giants","commanders","jets","dolphins"]),
        "nhl": ("hockey/nhl", ["bruins","rangers","leafs","penguins","capitals","lightning","panthers","canadiens","senators","sabres","red wings","blackhawks","blues","predators","jets","wild","avalanche","stars","flames","oilers","canucks","sharks","ducks","kings","coyotes","golden knights","kraken","hurricanes","blue jackets","devils","islanders","flyers"]),
    }

    detected_sport = None
    for sport, (path, teams) in sport_map.items():
        if sport in q or any(t in q for t in teams):
            detected_sport = (sport, path)
            break

    if not detected_sport:
        return context

    sport_name, sport_path = detected_sport
    base = f"https://site.api.espn.com/apis/site/v2/sports/{sport_path}"

    # Scoreboard (recent games)
    try:
        r = requests.get(f"{base}/scoreboard", timeout=8)
        events = r.json().get("events", [])
        q_words = set(w.strip("?.,!()-") for w in question.split() if len(w) > 3)

        games = []
        for e in events[:10]:
            name = e.get("name","").lower()
            short = e.get("shortName","").lower()
            if sum(1 for w in q_words if w.lower() in name or w.lower() in short) >= 1:
                comp = e.get("competitions",[{}])[0]
                status = e.get("status",{}).get("type",{}).get("description","?")
                teams_data = []
                for c in comp.get("competitors",[]):
                    team = c.get("team",{}).get("displayName","?")
                    rec = c.get("records",[{}])
                    record = rec[0].get("summary","?") if rec else "?"
                    score = c.get("score","-")
                    ha = c.get("homeAway","?")
                    teams_data.append(f"{team}({ha}) {record} score:{score}")
                games.append(f"{e.get('shortName',e.get('name','?'))} | {status} | {' vs '.join(teams_data)}")

        if games:
            context["recent_games"] = games[:3]
        else:
            # Show all today's games as context
            context["todays_games"] = [
                f"{e.get('shortName','?')} | {e.get('status',{}).get('type',{}).get('description','?')}"
                for e in events[:5]
            ]
    except Exception:
        pass

    # Standings
    try:
        r = requests.get(f"{base}/standings", timeout=6)
        data = r.json()
        standings = []
        for group in data.get("children", [data])[:2]:
            for entry in group.get("standings", {}).get("entries", [])[:5]:
                team = entry.get("team", {}).get("displayName", "?")
                stats = {s["name"]: s["displayValue"] for s in entry.get("stats", [])}
                wins = stats.get("wins", "?")
                losses = stats.get("losses", "?")
                pct = stats.get("winPercent", stats.get("playoffSeed", "?"))
                standings.append(f"{team}: {wins}W-{losses}L ({pct})")
        if standings:
            context["standings"] = standings[:8]
    except Exception:
        pass

    # Playoff series scores (NBA/NHL specific)
    if sport_name in ("nba", "nhl"):
        try:
            r = requests.get(f"{base}/scoreboard?groups=playoff", timeout=6)
            playoff_events = r.json().get("events", [])
            q_words = set(w.strip("?.,!()-").lower() for w in question.split() if len(w) > 3)
            for e in playoff_events:
                name = e.get("name","").lower()
                if sum(1 for w in q_words if w in name) >= 1:
                    comp = e.get("competitions",[{}])[0]
                    series_summary = comp.get("series", {})
                    if series_summary:
                        context["playoff_series"] = str(series_summary)
                    break
        except Exception:
            pass

    # Injuries (ESPN)
    try:
        r = requests.get(f"{base}/injuries", timeout=6)
        injuries = r.json()
        inj_list = []
        for team_data in injuries.get("injuries", [])[:10]:
            team_name = team_data.get("team", {}).get("displayName", "?")
            for player in team_data.get("injuries", [])[:3]:
                name = player.get("athlete", {}).get("displayName", "?")
                status = player.get("status", "?")
                detail = player.get("details", {}).get("detail", "")
                inj_list.append(f"{team_name}: {name} — {status} ({detail})")
        if inj_list:
            context["injuries"] = inj_list[:10]
    except Exception:
        pass

    return context


# ── NEWS PATTERN ANALYSIS ─────────────────────────────────────────────────────

def fetch_multi_source_news(question: str) -> list:
    """Fetch news from multiple sources. Handles rate limits gracefully."""
    articles = []
    stopwords = {"will","the","and","for","are","was","has","have","been","that",
                 "this","with","from","they","their","reach","april","may","june"}
    words = [w.strip("?.,!()$") for w in question.split()
             if len(w) > 3 and w.lower() not in stopwords and not w.startswith("$")]
    query = " ".join(words[:5])

    # NewsAPI
    try:
        api_key = os.getenv("NEWS_API_KEY","")
        if api_key:
            r = requests.get("https://newsapi.org/v2/everything",
                params={"q": query, "pageSize": 6, "sortBy": "publishedAt",
                        "language": "en", "apiKey": api_key}, timeout=8)
            if r.status_code == 200:
                for a in r.json().get("articles",[]):
                    articles.append({
                        "source": "NewsAPI",
                        "title": a.get("title",""),
                        "description": a.get("description","") or "",
                        "published": a.get("publishedAt","")[:10],
                    })
            # 429 = rate limited, skip silently
    except Exception:
        pass

    # Tavily (fallback if NewsAPI returned nothing — replaces Serper)
    if not articles:
        try:
            api_key = os.getenv("TAVILY_API_KEY","")
            if api_key:
                r = requests.post("https://api.tavily.com/search",
                    json={"api_key": api_key, "query": query,
                          "max_results": 5, "search_depth": "basic"}, timeout=8)
                if r.status_code == 200:
                    for item in r.json().get("results",[]):
                        articles.append({
                            "source": "Tavily",
                            "title": item.get("title",""),
                            "description": item.get("content","")[:200],
                            "published": item.get("published_date",""),
                        })
        except Exception:
            pass

    # Twitter — skip silently if no access (requires Pro tier)
    # Status: Basic access only, search endpoint returns 403

    return articles


def build_research_report(market: dict) -> dict:
    """
    Build comprehensive research report for a market.
    Caches to data/research/{market_id}.json — reuses if <30 min old.
    """
    question  = market.get("question","")
    market_id = market.get("id", market.get("numeric_id","unknown"))
    report_path = RESEARCH_DIR / f"{str(market_id)[:20]}.json"

    # Return cached report if fresh
    # Hot categories (geopolitik, breaking news): 5 min cache
    # Others: 30 min cache
    hot_categories = {"geopolitik", "politics", "breaking"}
    q_lower = question.lower()
    is_hot = (
        any(x in q_lower for x in ["iran","ceasefire","war","military","strike","invasion","coup","arrest","breaking"]) or
        market.get("category","") in hot_categories
    )
    cache_minutes = 5 if is_hot else 30

    if report_path.exists():
        try:
            cached = json.loads(report_path.read_text())
            generated = datetime.fromisoformat(cached.get("generated_at","2000-01-01"))
            age_minutes = (datetime.now(timezone.utc) - generated).total_seconds() / 60
            if age_minutes < cache_minutes:
                return cached
        except Exception:
            pass

    now = datetime.now(timezone.utc).isoformat()
    report = {
        "market_id": market_id,
        "question": question,
        "market_price": market.get("price", 0.5),
        "generated_at": now,
        "macro": {},
        "sports": {},
        "news_articles": [],
        "causal_chains": [],
        "summary": "",
    }

    # 1. Macro context (always)
    report["macro"] = get_macro_context()

    # 2. Sports deep context (if sports market)
    q_lower = question.lower()
    is_sports = any(x in q_lower for x in ["nba","nfl","mlb","nhl","ufc","vs.","vs ","tennis","open:","playoffs","series"])
    if is_sports:
        report["sports"] = get_sports_deep_context(question)

    # 3. Multi-source news
    report["news_articles"] = fetch_multi_source_news(question)

    # 4. Causal chains
    news_text = " ".join(a["title"] + " " + a["description"] for a in report["news_articles"])
    report["causal_chains"] = detect_causal_chains(question, news_text)

    # 5. Save report
    report_path = RESEARCH_DIR / f"{str(market_id)[:20]}.json"
    report_path.write_text(json.dumps(report, indent=2, default=str))

    return report


def format_research_for_llm(report: dict) -> str:
    """Format research report into compact LLM context string."""
    lines = []
    q = report.get("question","")

    # Macro
    macro = report.get("macro",{})
    if macro.get("fear_greed"):
        fg = macro["fear_greed"]
        lines.append(f"[MACRO] Fear&Greed: {fg['current']} | 7d trend: {fg['7d_trend']}")
    if macro.get("crypto_sentiment"):
        cs = macro["crypto_sentiment"]
        lines.append(f"[MACRO] BTC: ${cs['btc_price']:,.0f} ({cs['btc_24h']:+.1f}% 24h) → {cs['risk_signal']}")
    if macro.get("fed_expectations"):
        lines.append("[MACRO] Fed market expectations:")
        for fe in macro["fed_expectations"][:2]:
            lines.append(f"  {fe}")

    # Sports
    sports = report.get("sports",{})
    if sports.get("playoff_series"):
        lines.append(f"[SPORTS] Playoff series: {sports['playoff_series']}")
    if sports.get("recent_games"):
        lines.append("[SPORTS] Recent games:")
        for g in sports["recent_games"][:3]:
            lines.append(f"  {g}")
    if sports.get("standings"):
        lines.append("[SPORTS] Standings:")
        for s in sports["standings"][:5]:
            lines.append(f"  {s}")
    if sports.get("injuries"):
        lines.append("[SPORTS] Injuries:")
        for inj in sports["injuries"][:6]:
            lines.append(f"  {inj}")

    # News (top 6 most recent)
    articles = report.get("news_articles",[])
    if articles:
        lines.append(f"[NEWS] {len(articles)} articles found:")
        for a in articles[:6]:
            lines.append(f"  [{a['source']}] {a['title'][:80]}: {a['description'][:100]}")

    # Causal chains
    chains = report.get("causal_chains",[])
    if chains:
        lines.append("[CAUSAL CHAINS] Relevant cause-effect patterns:")
        for c in chains[:4]:
            lines.append(f"  → {c}")

    return "\n".join(lines)
