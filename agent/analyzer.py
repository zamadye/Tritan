"""
Probability estimation engine - Layer architecture:
  Layer 1: Statistical prior (from 19,624 resolved markets)
  Layer 2: LLM catalyst evaluation (strength + crowd error detection)
  Layer 3: Edge calculation = (p_base × catalyst_adj) - market_price
"""
import json
import os
import re
from pathlib import Path
from agent.llm import chat


# ── Layer 1: Statistical Prior ────────────────────────────────────────────────

def get_statistical_prior(market: dict) -> dict:
    """
    Get calibrated p_base using logistic regression model per category.
    Falls back to bucket-based prior if model not available.
    """
    prior_file = Path("data/statistical_prior.json")
    cal_file   = Path("data/calibration_model.json")

    price = market["price"]
    from agent.learner import _infer_category
    cat = _infer_category({"category": market.get("category",""), "market_question": market.get("question","")})

    # Entry price momentum signal
    ep_signal = {"momentum_signal": "NEUTRAL", "momentum_yes_rate": 0.5, "momentum_n": 0}
    if prior_file.exists():
        prior = json.loads(prior_file.read_text())
        bucket = f"{int(price*10)*10}-{int(price*10)*10+10}%"
        ep = prior.get("entry_price_prior",{}).get(bucket,{})
        if ep.get("n",0) >= 20:
            ep_signal = {"momentum_signal": ep.get("momentum_signal","NEUTRAL"),
                         "momentum_yes_rate": ep.get("yes_rate",0.5),
                         "momentum_n": ep.get("n",0)}

    # Logistic regression calibration (primary)
    if cal_file.exists() and 0 < price < 1:
        cal = json.loads(cal_file.read_text())
        model = cal.get(cat) or cal.get("other")
        if model and model["n"] >= 50:
            import math
            def sigmoid(x): return 1/(1+math.exp(-max(-500,min(500,x))))
            def logit(p): return math.log(p/(1-p))
            a, b = model["a"], model["b"]
            p_cal = round(sigmoid(a * logit(price) + b), 4)
            return {
                "p_base": p_cal,
                "n": model["n"],
                "source": f"logistic:{cat}",
                "brier_improvement": model["improvement"],
                **ep_signal,
            }

    # Fallback: bucket-based prior
    if prior_file.exists():
        prior = json.loads(prior_file.read_text())
        bucket = f"{int(price*10)*10}-{int(price*10)*10+10}%"
        cat_data = prior.get("categories",{}).get(cat,{}).get(bucket)
        if cat_data and cat_data["n"] >= 20:
            return {"p_base": cat_data["yes_rate"], "n": cat_data["n"],
                    "source": f"bucket:{cat}", **ep_signal}
        overall = prior.get("overall",{}).get(bucket)
        if overall and overall["n"] >= 50:
            return {"p_base": overall["yes_rate"], "n": overall["n"],
                    "source": "bucket:overall", **ep_signal}

    return {"p_base": price, "n": 0, "source": "fallback", **ep_signal}


# ── Layer 2: LLM Catalyst Evaluator ──────────────────────────────────────────

def _load_knowledge() -> str:
    kb = Path(__file__).parent / "KNOWLEDGE.md"
    return kb.read_text()[:400] if kb.exists() else ""


def estimate_probability(market: dict, news_context: str = "", evolution_context: str = "", prev_loss: bool = False) -> dict:
    from agent.sports import get_sports_context
    from agent.osint import get_osint_signals

    sports_ctx = get_sports_context(market.get("question", ""))
    osint_ctx  = get_osint_signals(market.get("question", ""))
    full_context = "\n".join(filter(None, [news_context, sports_ctx, osint_ctx]))
    full_context = full_context.replace("|", "-").replace("━", "-").replace("═", "-")
    knowledge    = _load_knowledge()

    # Layer 1: statistical prior + logistic calibration
    prior    = get_statistical_prior(market)
    p_base   = prior["p_base"]
    p_market = market["price"]

    # Edge Type 2: information delay detector
    from agent.info_edge import detect_info_edge
    info_edge_data = detect_info_edge(market)
    info_edge_ctx  = ""
    if info_edge_data["has_edge"]:
        info_edge_ctx = (
            f"\n⚡ INFO EDGE: {info_edge_data['signal']} "
            f"({info_edge_data['minutes_since_info']} min ago) — {info_edge_data['detail']}"
            f"\nMarket likely has not priced this in yet."
        )



    prev_loss_note = (
        "⚠️ PREVIOUS BET ON THIS MARKET WAS WRONG. Only bet again with NEW concrete evidence.\n"
        if prev_loss else ""
    )

    prompt = (
        f"Analyze this prediction market for a momentum trade.\n"
        f"Market: {market['question']}\n"
        f"Current price: {p_market:.0%}. Historical base rate: {p_base:.0%} "
        f"(from {prior['n']} similar resolved markets, source: {prior['source']}). "
        f"Category: {market.get('category','?')}.\n"
        f"Momentum signal: markets at this price 24h before resolve → "
        f"{prior.get('momentum_signal','NEUTRAL')} "
        f"({prior.get('momentum_yes_rate',0.5):.0%} resolved YES, n={prior.get('momentum_n',0)}).\n\n"
        f"Real-time data:\n{full_context[:500] if full_context else 'No data available.'}"
        f"{info_edge_ctx}\n\n"
        f"Past lessons:\n{evolution_context[:200] if evolution_context else 'None yet.'}\n"
        f"{prev_loss_note}\n"
        f"Question: Is there a specific verifiable catalyst that will move this price in the next 4 hours?\n"
        f"Note: Base rate {p_base:.0%} vs market {p_market:.0%} = {p_base-p_market:+.0%} gap. "
        f"Momentum signal says {prior.get('momentum_signal','NEUTRAL')}. "
        f"Is this gap justified by current news?\n\n"
        f"Reply with a JSON object containing:\n"
        f"- score: float 0-1 (catalyst strength)\n"
        f"- catalyst: string (what is the catalyst, or none)\n"
        f"- type: string (official/breaking/data/rumor/none)\n"
        f"- error: bool (is market price wrong vs base rate?)\n"
        f"- direction: string (yes_cheap/no_cheap/none)\n"
        f"- edge: bool (do you have info market has not priced in?)\n"
        f"- action: string (BET_YES/BET_NO/SKIP)\n"
        f"- conf: float 0-1\n"
        f"- quality: string (strong/weak/none)\n"
        f"- reason: string (max 80 chars, cite specific facts)"
    )

    try:
        raw = chat(prompt)
        raw = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        start = raw.find("{"); end = raw.rfind("}") + 1
        if start != -1 and end > start:
            raw = raw[start:end]
        try:
            result = json.loads(raw)
        except json.JSONDecodeError:
            raw = re.sub(r",\s*([}\]])", r"\1", raw)
            result = json.loads(raw)

        # Layer 3: Edge calculation — map short field names to internal names
        catalyst_score = float(result.get("score", result.get("catalyst_score", 0)))
        crowd_error    = result.get("error", result.get("crowd_error_detected", False))
        action         = result.get("action", result.get("recommended_action", "SKIP"))
        confidence     = float(result.get("conf", result.get("confidence", 0)))
        dq             = result.get("quality", result.get("data_quality", "weak"))
        catalyst_str   = result.get("catalyst", "none")
        direction      = result.get("direction", result.get("crowd_error_direction", "none"))
        info_edge      = result.get("edge", result.get("information_edge", False))

        # Force SKIP if no data or weak catalyst without crowd error
        if dq == "none":
            action = "SKIP"
        # Strict validation gate (per architecture spec):
        # Edge valid ONLY IF: p_calibrated diff > 8% AND specific information exists
        if catalyst_score < 0.4 and not crowd_error:
            action = "SKIP"
        if catalyst_score < 0.2:  # no catalyst at all → always skip
            action = "SKIP"

        # Calculate p_true from base rate + catalyst adjustment
        # Catalyst can shift p_base by up to ±20%
        catalyst_adj = (catalyst_score - 0.5) * 0.40  # -0.20 to +0.20
        if action == "BET_NO":
            catalyst_adj = -abs(catalyst_adj)
        elif action == "BET_YES":
            catalyst_adj = abs(catalyst_adj)
        else:
            catalyst_adj = 0

        p_true = max(0.01, min(0.99, p_base + catalyst_adj))
        edge   = round(p_true - p_market, 4)

        # Map action to side
        side = "YES" if action == "BET_YES" else "NO" if action == "BET_NO" else "SKIP"

        # Skip if edge too small
        edge_threshold = float(os.getenv("EDGE_THRESHOLD", 0.04))
        if abs(edge) < edge_threshold:
            side = "SKIP"

        # Confidence cap based on data quality
        if dq == "weak" and confidence > 0.65:
            confidence = 0.65
        if dq == "none":
            confidence = 0.0

        return {
            "p_true":             round(p_true, 4),
            "p_true_estimated":   round(p_true, 4),
            "p_base":             p_base,
            "p_base_source":      prior["source"],
            "p_base_n":           prior["n"],
            "confidence":         round(confidence, 3),
            "confidence_at_bet":  round(confidence, 3),
            "edge":               edge,
            "edge_at_bet":        edge,
            "recommended_side":   side,
            "catalyst_score":     catalyst_score,
            "catalyst":           catalyst_str,
            "catalyst_type":      result.get("type", result.get("catalyst_type","none")),
            "crowd_error_detected": crowd_error,
            "information_edge":   info_edge,
            "data_quality":       dq,
            "base_rate":          p_base,
            "calibration_applied": f"p_base={p_base:.2%}(n={prior['n']},{prior['source']}) + catalyst_adj={catalyst_adj:+.2%} = p_true={p_true:.2%}",
            "reasoning_summary":  result.get("reasoning",""),
            "resolution_clarity": "high" if dq == "strong" else "medium",
        }

    except Exception as e:
        print(f"[ANALYZER] ❌ LLM error: {e}")
        return {
            "p_true": market["price"], "p_true_estimated": market["price"],
            "p_base": p_base, "confidence": 0.0, "confidence_at_bet": 0.0,
            "edge": 0.0, "edge_at_bet": 0.0, "recommended_side": "SKIP",
            "catalyst_score": 0, "data_quality": "none",
            "reasoning_summary": f"Analysis failed: {e}",
            "calibration_applied": "",
        }


def fetch_news(market: dict) -> str:
    """Fetch news - Serper primary, fallback to NewsAPI."""
    q = market.get("question","")
    news = _fetch_serper(q)
    if news: return news
    news = _fetch_tavily(q)
    if news: return news
    return _fetch_newsapi(q)


def _fetch_serper(query: str) -> str:
    api_key = os.getenv("SERPER_API_KEY","")
    if not api_key: return ""
    import requests
    try:
        r = requests.post("https://google.serper.dev/news",
            headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
            json={"q": query, "num": 6}, timeout=8)
        if r.status_code != 200: return ""
        items = r.json().get("news",[])
        return "\n".join(f"- {i['title']}: {i.get('snippet','')}" for i in items)
    except: return ""


def _fetch_tavily(query: str) -> str:
    api_key = os.getenv("TAVILY_API_KEY","")
    if not api_key: return ""
    import requests
    try:
        r = requests.post("https://api.tavily.com/search",
            json={"api_key": api_key, "query": query, "max_results": 4,
                  "search_depth": "basic", "include_answer": True}, timeout=8)
        data = r.json()
        if data.get("detail"): return ""
        lines = []
        if data.get("answer"): lines.append(f"[SUMMARY] {data['answer']}")
        for item in data.get("results",[]): lines.append(f"- {item['title']}: {item.get('content','')[:150]}")
        return "\n".join(lines)
    except: return ""


def _fetch_newsapi(query: str) -> str:
    api_key = os.getenv("NEWS_API_KEY","")
    if not api_key: return ""
    import requests
    stopwords = {"will","the","and","for","are","was","has","have","been","that","this","with","from"}
    words = [w.strip("?.,!()$") for w in query.split() if len(w)>3 and w.lower() not in stopwords]
    try:
        r = requests.get("https://newsapi.org/v2/everything",
            params={"q":" ".join(words[:4]),"pageSize":5,"sortBy":"publishedAt",
                    "language":"en","apiKey":api_key}, timeout=8)
        if r.status_code != 200: return ""
        arts = r.json().get("articles",[])
        return "\n".join(f"- {a['title']}: {a.get('description','')}" for a in arts)
    except: return ""


def _get_calibration_adjustment(category: str) -> float:
    """Legacy - kept for compatibility. Now handled by statistical prior."""
    return 0.0
