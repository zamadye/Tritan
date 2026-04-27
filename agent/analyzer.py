"""Probability estimation engine using OpenClaw LLM with self-evolving reasoning."""
import json
import os
from agent.llm import chat


def estimate_probability(market: dict, news_context: str = "", evolution_context: str = "", prev_loss: bool = False) -> dict:
    cal_adj = _get_calibration_adjustment(market.get("category", ""))

    # Get real-time sports/geopolitik data
    from agent.sports import get_sports_context
    from agent.osint import get_osint_signals
    sports_ctx = get_sports_context(market.get("question", ""))
    osint_ctx  = get_osint_signals(market.get("question", ""))

    # Detect category early (needed for fixes below)
    q_lower = market.get("question","").lower()
    is_sports = any(x in q_lower for x in
        ["vs.","vs ","ipl","ufc","tennis","open:","grand prix","mlb","nba","nhl","nfl"])

    # Combine all context: news + sports + OSINT
    full_context = "\n".join(filter(None, [news_context, sports_ctx, osint_ctx]))

    prev_loss_note = (
        "\n⚠️  PREVIOUS BET ON THIS MARKET WAS WRONG. Be extra critical. "
        "Only bet again if you have NEW concrete evidence that changes the picture. "
        "Require confidence ≥70% and edge ≥12% to recommend YES/NO.\n"
        if prev_loss else ""
    )

    prompt = f"""You are an elite superforecaster. Your job: find markets where you have STRONG evidence the market price is WRONG.

━━━ MARKET ━━━
QUESTION: {market['question']}
MARKET PRICE (YES): {market['price']:.2%}
RESOLVES: {market['end_date']}
CATEGORY: {market.get('category', 'unknown')}

━━━ REAL-TIME EVIDENCE ━━━
{full_context if full_context else 'No data found — rely on base rates only, lower confidence.'}

━━━ YOUR PAST MISTAKES (learn from these) ━━━
{evolution_context if evolution_context else 'No history yet.'}
{prev_loss_note}{f"CALIBRATION: Apply {cal_adj:+.0%} to p_true for this category." if cal_adj else ""}

━━━ REASONING STEPS (be explicit) ━━━
1. BASE RATE: What % of identical historical situations resolved YES?
2. NEWS IMPACT: Does the news STRONGLY shift the base rate? By how much?
3. RESOLUTION CLARITY: Is the resolution criteria 100% objective? (high/medium/low)
4. MARKET MISPRICING: WHY is the market price wrong? What are other traders missing?
5. CONFIDENCE CHECK: Only claim 70%+ confidence if you have CONCRETE evidence, not just base rates.
   - 80-90%: You have direct verifiable data (price feeds, official announcements, scores)
   - 70-79%: Strong base rate + supporting news
   - 60-69%: Base rate only, or conflicting signals
   - <60%: Uncertain — output SKIP

━━━ CRITICAL RULES ━━━
- HIGH confidence (≥70%) requires SPECIFIC evidence, not just "historically X tends to happen"
- If news is absent → cap confidence at 65%
- If resolution criteria is "low" clarity → cap confidence at 60%
- Edge must be ≥8% to recommend YES/NO — otherwise SKIP
- For sports/crypto: you CAN reach 80%+ if you have real-time data from news

Output ONLY valid JSON:
{{
  "p_true": <float 0-1>,
  "confidence": <float 0-1>,
  "edge": <p_true minus {market['price']:.4f}>,
  "recommended_side": "<YES/NO/SKIP>",
  "base_rate": <float 0-1>,
  "news_adjustment": <float, shift from news>,
  "key_factors_for": ["<concrete fact>", "<concrete fact>"],
  "key_factors_against": ["<concrete fact>"],
  "resolution_clarity": "<high/medium/low>",
  "market_efficiency_note": "<why is market price wrong or right?>",
  "calibration_applied": "<what adjustments applied>",
  "reasoning_summary": "<base rate X% → news shifts by Y% → final Z% because [specific reason]>"
}}"""

    try:
        raw = chat(prompt)
        raw = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        result = json.loads(raw)

        # Enforce confidence caps based on evidence quality
        clarity = result.get("resolution_clarity", "medium")
        has_news = bool(full_context)
        conf = result.get("confidence", 0.6)

        if not full_context and conf > 0.65:
            conf = 0.65
            result["calibration_applied"] = (result.get("calibration_applied","") + " | capped at 65% (no news)").strip(" |")
        if clarity == "low" and conf > 0.60:
            conf = 0.60
            result["calibration_applied"] = (result.get("calibration_applied","") + " | capped at 60% (low clarity)").strip(" |")

        result["confidence"] = round(conf, 3)

        # ── SPORTS: Vegas as primary signal ──────────────────────────
        # For sports, Vegas implied prob = ground truth. LLM only adjusts ±10%
        if is_sports and osint_ctx and "Implied Prob" in osint_ctx:
            import re
            vegas_probs = re.findall(r"Implied Prob \w+:\s*([\d.]+)", osint_ctx)
            if len(vegas_probs) >= 2:
                # Vegas home/away implied probs
                vp_home = float(vegas_probs[0])
                vp_away = float(vegas_probs[1])
                # Determine which side we're betting
                p_true = result.get("p_true", market["price"])
                side_bet = result.get("recommended_side","SKIP")
                vegas_base = vp_home if side_bet=="YES" else vp_away

                # LLM can only adjust Vegas by ±10%
                llm_adjustment = p_true - vegas_base
                llm_adjustment = max(-0.10, min(0.10, llm_adjustment))
                new_p_true = round(vegas_base + llm_adjustment, 3)

                result["p_true"] = new_p_true
                result["edge"] = round(new_p_true - market["price"], 4)
                result["calibration_applied"] = (
                    result.get("calibration_applied","") +
                    f" | Vegas-anchored: {vegas_base:.0%}±{llm_adjustment:+.0%}={new_p_true:.0%}"
                ).strip(" |")

                # Recalculate recommended side based on new p_true
                edge_yes = new_p_true - market["price"]
                edge_no  = (1-new_p_true) - (1-market["price"])
                edge_threshold = float(os.getenv("EDGE_THRESHOLD", 0.10))
                if abs(edge_yes) >= edge_threshold or abs(edge_no) >= edge_threshold:
                    result["recommended_side"] = "YES" if edge_yes > edge_no else "NO"
                else:
                    result["recommended_side"] = "SKIP"
        if is_sports and news_context:
            # Extract team names from market question
            import re
            q_words = set(w.lower().strip("?.,!()") for w in market.get("question","").split()
                         if len(w) > 3 and w[0].isupper())
            news_lower = news_context.lower()
            # If news mentions "already finished/completed" but team names don't match → skip
            stale_phrases = ["already finished","already completed","match already","game already",
                             "already won","already defeated","final score"]
            if any(phrase in news_lower for phrase in stale_phrases):
                # Check if the teams in news match the market
                teams_in_news = sum(1 for w in q_words if w in news_lower)
                if teams_in_news < 1:
                    result["recommended_side"] = "SKIP"
                    result["calibration_applied"] = (
                        result.get("calibration_applied","") +
                        " | SKIP: stale news from different game"
                    ).strip(" |")

        # ── SPORTS confidence hard cap ────────────────────────────────
        q_lower = market.get("question","").lower()
        is_sports = any(x in q_lower for x in
            ["vs.","vs ","ipl","ufc","tennis","open:","grand prix","mlb","nba","nhl","nfl"])
        if is_sports and conf > 0.75:
            conf = 0.75
            result["calibration_applied"] = (
                result.get("calibration_applied","") +
                " | capped at 75% (sports hard cap)"
            ).strip(" |")
            result["confidence"] = conf

        # ── FIX 1: Vegas hard constraint ──────────────────────────────
        # Extract Vegas implied probability from OSINT context
        vegas_prob = _extract_vegas_prob(osint_ctx, result.get("recommended_side","YES"))
        if vegas_prob and conf > 0:
            max_conf = min(1.0, vegas_prob + 0.12)  # LLM max 12% above Vegas
            if conf > max_conf:
                conf = round(max_conf, 3)
                result["calibration_applied"] = (
                    result.get("calibration_applied","") +
                    f" | capped at {conf:.0%} (Vegas={vegas_prob:.0%})"
                ).strip(" |")
                result["confidence"] = conf

        # ── FIX 2: Overconfidence penalty from evolution ──────────────
        evo_file = os.path.join(os.path.dirname(__file__), "..", "data", "evolution_lessons.json")
        try:
            import json as _json
            from pathlib import Path as _Path
            evo_data = _json.loads(_Path(evo_file).read_text()) if _Path(evo_file).exists() else {}
            overconf_count = len(evo_data.get("overconfidence_patterns", []))

            # Hard cap FIRST: jika overconfidence >= 30x, max conf = 0.68
            if overconf_count >= 30 and conf > 0.68:
                old = conf; conf = 0.68
                result["calibration_applied"] = (
                    result.get("calibration_applied","") +
                    f" | hard_cap=68% (overconf {overconf_count}x)"
                ).strip(" |")
                result["confidence"] = conf

            # Penalty: 0.5% per event, max 20%
            elif overconf_count >= 5 and conf > 0.60:
                penalty = min(0.20, overconf_count * 0.005)
                conf = round(conf - penalty, 3)
                result["calibration_applied"] = (
                    result.get("calibration_applied","") +
                    f" | -{penalty:.0%} overconf_penalty ({overconf_count}x)"
                ).strip(" |")
                result["confidence"] = conf

            # Per-category calibration adjustment
            from agent.learner import _infer_category
            cat = _infer_category({"category": market.get("category",""), "market_question": market.get("question","")})
            cat_adj = evo_data.get("calibration_adjustments", {}).get(cat, 0)
            if cat_adj != 0:
                p_true = result.get("p_true", market["price"])
                result["p_true"] = round(max(0.01, min(0.99, p_true + cat_adj)), 3)
                result["edge"]   = round(result["p_true"] - market["price"], 4)
                result["calibration_applied"] = (
                    result.get("calibration_applied","") +
                    f" | cat_adj={cat_adj:+.0%} ({cat})"
                ).strip(" |")
        except Exception as e:
            pass

        # ── FIX 3: Category-aware market timing filter ────────────────
        end_date = market.get("end_date", "")
        category = market.get("category", "")
        if end_date:
            try:
                from datetime import datetime, timezone
                end_dt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
                days_left = (end_dt - datetime.now(timezone.utc)).days

                # Different tolerance per category:
                # Sports/crypto: result fast, skip if >1 day past deadline
                # Geopolitik/politics/economics: can take days to officially resolve
                if any(x in market.get("question","").lower() for x in
                       ["vs.","vs ","ufc","tennis","open:","grand prix","mlb","nba","nhl"]):
                    stale_threshold = 0    # sports: skip if ANY day past deadline
                elif any(x in market.get("question","").lower() for x in
                         ["bitcoin","btc","eth","crypto","wti","oil","gold"]):
                    stale_threshold = -1   # crypto/commodity: skip if >1 day past
                else:
                    stale_threshold = -5   # geo/politics: allow 5 days grace

                if days_left < stale_threshold:
                    result["recommended_side"] = "SKIP"
                    result["calibration_applied"] = (
                        result.get("calibration_applied","") +
                        f" | SKIP: {abs(days_left)}d past deadline"
                    ).strip(" |")
            except Exception:
                pass

        # Sanity-clamp edge to [-1, 1]
        raw_edge = result.get("edge", 0.0)
        p_true = result.get("p_true", market["price"])
        real_edge = round(p_true - market["price"], 4)  # always recompute from p_true
        result["edge"] = real_edge

        # Auto-SKIP if edge below threshold
        if abs(real_edge) < float(os.getenv("EDGE_THRESHOLD", 0.08)):
            result["recommended_side"] = "SKIP"

        result["p_true_estimated"] = result.get("p_true", market["price"])
        result["confidence_at_bet"] = result["confidence"]
        result["edge_at_bet"] = result.get("edge", 0.0)
        return result

    except Exception as e:
        print(f"[ANALYZER] ❌ LLM error: {e}")
        return {
            "p_true": market["price"], "p_true_estimated": market["price"],
            "confidence": 0.0, "confidence_at_bet": 0.0,
            "edge": 0.0, "edge_at_bet": 0.0,
            "recommended_side": "SKIP",
            "key_factors_for": [], "key_factors_against": [],
            "base_rate": market["price"],
            "reasoning_summary": f"Analysis failed: {e}",
        }


def _extract_vegas_prob(osint_ctx: str, side: str) -> float | None:
    """Extract implied probability from Vegas odds in OSINT context."""
    if not osint_ctx or "Implied Prob" not in osint_ctx:
        return None
    try:
        import re
        # Match "Implied Prob Teamname: 0.559" patterns
        matches = re.findall(r"Implied Prob \w+:\s*([\d.]+)", osint_ctx)
        if len(matches) >= 2:
            probs = [float(m) for m in matches]
            # Return prob for the side we're betting
            return probs[0] if side == "YES" else probs[1]
        elif len(matches) == 1:
            return float(matches[0])
    except Exception:
        pass
    return None


def _get_calibration_adjustment(category: str) -> float:
    """Load per-category calibration adjustment from evolution lessons."""
    evo_file = os.getenv("EVOLUTION_FILE", "./data/evolution_lessons.json")
    try:
        from pathlib import Path
        if Path(evo_file).exists():
            lessons = json.loads(Path(evo_file).read_text())
            return lessons.get("calibration_adjustments", {}).get(category, 0.0)
    except Exception:
        pass
    return 0.0


def fetch_news(market: dict) -> str:
    """Fetch recent news — tries Tavily first, fallback to Serper."""
    news = _fetch_tavily(market.get("question", ""))
    if news:
        return news
    return _fetch_serper(market.get("question", ""))


def _fetch_tavily(query: str) -> str:
    api_key = os.getenv("TAVILY_API_KEY", "")
    if not api_key:
        return ""
    import requests
    try:
        resp = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": api_key,
                "query": query,
                "max_results": 8,           # lebih banyak artikel
                "search_depth": "advanced", # deep search
                "include_answer": True,     # Tavily AI summary
                "include_raw_content": False,
            },
            timeout=10,
        )
        data = resp.json()
        lines = []
        # Tavily AI answer (ringkasan langsung)
        if data.get("answer"):
            lines.append(f"[SUMMARY] {data['answer']}")
        # Individual results
        for r in data.get("results", []):
            lines.append(f"- {r['title']}: {r.get('content','')[:200]}")
        return "\n".join(lines) or ""
    except Exception:
        return ""


def _fetch_serper(query: str) -> str:
    api_key = os.getenv("SERPER_API_KEY", "")
    if not api_key:
        return ""
    import requests
    try:
        resp = requests.post(
            "https://google.serper.dev/news",
            headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
            json={"q": query, "num": int(os.getenv("MAX_NEWS_ARTICLES", 5))},
            timeout=8,
        )
        if resp.status_code != 200:
            return ""
        items = resp.json().get("news", [])
        return "\n".join(f"- {i['title']}: {i.get('snippet', '')}" for i in items)
    except Exception:
        return ""
