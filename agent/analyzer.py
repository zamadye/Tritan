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

    # Build prompt — MiMo works WITHOUT JSON templates, parse flexibly
    data_summary = full_context[:300] if full_context else "No data."
    info_note = f" {info_edge_ctx.strip()}" if info_edge_ctx else ""
    lesson_note = evolution_context[:150] if evolution_context else ""
    prev_note = "Previous bet on this market was wrong. " if prev_loss else ""

    prompt = (
        f"{prev_note}Analyze this prediction market: {market['question']}. "
        f"Current price: {p_market:.0%}. Statistical base rate: {p_base:.0%} (n={prior['n']}). "
        f"Momentum: {prior.get('momentum_signal','?')} ({prior.get('momentum_yes_rate',0.5):.0%} resolve YES). "
        f"Price gap: {p_base-p_market:+.0%}. Category: {market.get('category','?')}. "
        f"Data: {data_summary}{info_note} "
        f"Lessons: {lesson_note} "
        f"Is there a specific catalyst that will move this price in the next 4 hours? "
        f"Reply with a JSON object."
    )

    try:
        raw = chat(prompt)
        if not raw or not raw.strip():
            raw = chat(f"Analyze: {market['question'][:60]}. Price={p_market:.0%} vs base={p_base:.0%}. Catalyst in 4h? Reply JSON.")
        if not raw or not raw.strip():
            raise ValueError("Empty LLM response")

        raw = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        start = raw.find("{"); end = raw.rfind("}") + 1
        if start != -1 and end > start:
            raw = raw[start:end]
        try:
            result = json.loads(raw)
        except json.JSONDecodeError:
            raw = re.sub(r",\s*([}\]])", r"\1", raw)
            try:
                result = json.loads(raw)
            except json.JSONDecodeError:
                result = {}

        # Flexible extraction — MiMo uses its own field names
        def _find(d, *keys, default=None):
            for k in keys:
                if k in d: return d[k]
                # Search nested
                for v in d.values():
                    if isinstance(v, dict) and k in v: return v[k]
            return default

        def _to_float(val, default=0.0):
            if val is None: return default
            if isinstance(val, (int, float)): return float(val)
            if isinstance(val, str):
                val = val.strip().lower()
                mapping = {"high":0.75,"medium":0.60,"low":0.45,"very high":0.80,
                           "very low":0.35,"strong":0.75,"weak":0.45,"none":0.0}
                if val in mapping: return mapping[val]
                try: return float(val)
                except: return default
            return default

        catalyst_score = _to_float(_find(result, "score","catalyst_score","strength","catalyst_strength"))
        crowd_error    = bool(_find(result, "err","error","mispriced","crowd_error","is_mispriced", default=False))
        action_raw     = str(_find(result, "act","action","recommendation","decision","signal", default="SKIP") or "SKIP").upper()
        confidence     = _to_float(_find(result, "conf","confidence","certainty","probability"))
        dq             = str(_find(result, "qual","quality","data_quality","evidence_quality", default="weak") or "weak").lower()
        catalyst_str   = str(_find(result, "cat","catalyst","trigger","event", default="none") or "none")
        direction      = str(_find(result, "dir","direction","crowd_error_direction", default="none") or "none").lower()
        info_edge      = bool(_find(result, "edge","information_edge","info_edge", default=False))
        reason         = str(_find(result, "why","reason","reasoning","rationale","analysis","summary", default="") or "")

        # Normalize action
        if "YES" in action_raw or "BUY" in action_raw or "LONG" in action_raw: action = "BET_YES"
        elif "NO" in action_raw or "SELL" in action_raw or "SHORT" in action_raw: action = "BET_NO"
        else: action = "SKIP"

        # If confidence not found, estimate from catalyst_score
        if confidence == 0 and catalyst_score > 0:
            confidence = min(0.65, catalyst_score * 0.8)

        # Validation gate — two valid paths to bet:
        # Path A: catalyst-driven (score >= 0.4)
        # Path B: statistical mispricing — requires n>=100 AND gap>=8%
        statistical_gap = abs(prior["p_base"] - p_market)
        has_stat_edge   = (statistical_gap >= 0.08 and prior["n"] >= 100)

        # Filter: skip if market resolves in <2h (too late to act)
        try:
            from datetime import datetime, timezone as _tz
            end_dt = datetime.fromisoformat(market.get("end_date","").replace("Z","+00:00"))
            hours_to_resolve = (end_dt - datetime.now(_tz.utc)).total_seconds() / 3600
            if 0 < hours_to_resolve < 2:
                action = "SKIP"
                reason = f"Too close to resolution ({hours_to_resolve:.1f}h remaining)"
        except Exception:
            pass

        if dq == "none" and not has_stat_edge:
            action = "SKIP"
        if catalyst_score < 0.4 and not crowd_error and not has_stat_edge:
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

        # If statistical edge exists, override SKIP from LLM (AFTER p_true calculation)
        if has_stat_edge and action == "SKIP" and catalyst_score < 0.2:
            action = "BET_NO" if prior["p_base"] < p_market else "BET_YES"
            reason = f"Statistical mispricing: p_base={prior['p_base']:.0%} vs market={p_market:.0%} gap={statistical_gap:.0%} (n={prior['n']})"
            confidence = max(confidence, float(os.getenv("MIN_CONFIDENCE", 0.58)))

        # Map action to side
        side = "YES" if action == "BET_YES" else "NO" if action == "BET_NO" else "SKIP"

        # Skip if edge too small
        edge_threshold = float(os.getenv("EDGE_THRESHOLD", 0.04))
        if abs(edge) < edge_threshold:
            side = "SKIP"

        # Confidence cap based on data quality
        if dq == "weak" and confidence > 0.65:
            confidence = 0.65
        if dq == "none" and not has_stat_edge:
            confidence = 0.0
        elif dq == "none" and has_stat_edge:
            # Statistical edge is valid even without news data
            confidence = 0.60

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
            "reasoning_summary":  reason,
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
