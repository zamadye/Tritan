"""Probability estimation engine using OpenClaw LLM with self-evolving reasoning."""
import json
import os
from agent.llm import chat


def _load_knowledge() -> str:
    """Load condensed knowledge base (max 400 chars to save tokens)."""
    from pathlib import Path as _Path
    kb = _Path(__file__).parent / "KNOWLEDGE.md"
    if not kb.exists():
        return ""
    # Only return entry strategy section (most critical)
    text = kb.read_text()
    return text[:400]


def estimate_probability(market: dict, news_context: str = "", evolution_context: str = "", prev_loss: bool = False) -> dict:
    cal_adj = _get_calibration_adjustment(market.get("category", ""))

    from agent.sports import get_sports_context
    from agent.osint import get_osint_signals
    sports_ctx = get_sports_context(market.get("question", ""))
    osint_ctx  = get_osint_signals(market.get("question", ""))

    q_lower = market.get("question","").lower()
    is_sports = any(x in q_lower for x in
        ["vs.","vs ","ipl","ufc","tennis","open:","grand prix","mlb","nba","nhl","nfl"])

    full_context = "\n".join(filter(None, [news_context, sports_ctx, osint_ctx]))
    knowledge    = _load_knowledge()

    prev_loss_note = (
        "\n⚠️  PREVIOUS BET ON THIS MARKET WAS WRONG. Be extra critical. "
        "Only bet again if you have NEW concrete evidence that changes the picture. "
        "Require confidence ≥70% and edge ≥12% to recommend YES/NO.\n"
        if prev_loss else ""
    )

    prompt = f"""You are a momentum trader on a prediction market. Your job: find markets where SENTIMENT, NEWS, or NARRATIVE will push the price UP or DOWN in the next few hours/days — regardless of the final outcome.

You are NOT trying to predict who wins. You are trying to predict: will the YES price go UP or DOWN from current {market['price']:.2%}?

━━━ DOMAIN KNOWLEDGE ━━━
{knowledge}

━━━ MARKET ━━━
QUESTION: {market['question']}
CURRENT YES PRICE: {market['price']:.2%}
RESOLVES: {market['end_date']}
CATEGORY: {market.get('category', 'unknown')}

━━━ REAL-TIME DATA (news, sentiment, market signals) ━━━
{full_context if full_context else '[NO DATA AVAILABLE — SKIP this market]'}

━━━ MOMENTUM LESSONS (from past trades) ━━━
{evolution_context if evolution_context else 'No history yet.'}
{prev_loss_note}

━━━ MOMENTUM TRADING RULES ━━━

RULE 1 — PRICE MOVEMENT, NOT OUTCOME:
- Ask: "Will YES price move UP from {market['price']:.2%} in the next 24-48h?"
- You don't need to know the final answer — you need to know the DIRECTION of price movement
- Positive news/sentiment → YES price goes UP → BET YES
- Negative news/sentiment → YES price goes DOWN → BET NO (buy NO = sell YES)

RULE 2 — MOMENTUM SIGNALS (what moves prices):
- Breaking news directly related to the question → STRONG signal
- Social sentiment shift (many people suddenly talking about it) → MEDIUM signal  
- Official announcement or data release → STRONG signal
- Volume spike on this market (>$50k/day) → market is moving, follow the flow
- Price already moved >5% today → momentum is real, ride it
- No news, no sentiment, no volume → SKIP (no catalyst to move price)

RULE 3 — ENTRY CRITERIA:
- Current price 15-85% (avoid near-certain markets, no room to move)
- At least ONE strong signal OR two medium signals
- Expected price movement: at least 10% from entry (your profit target)
- If price is already at 85%+: too late, skip
- If price is at 15%-: already priced in, skip

RULE 4 — CONFIDENCE = HOW STRONG IS THE CATALYST:
- 0.70-0.75: Breaking news + volume spike + sentiment aligned
- 0.65-0.69: Clear news catalyst, moderate volume
- 0.60-0.64: Weak signal, 1 data point only
- <0.60: No catalyst → SKIP

RULE 5 — SKIP FREELY:
- Most markets have no catalyst right now → SKIP them
- We make money on 3-5 high-quality momentum trades per day, not 20 random bets

━━━ OUTPUT FORMAT ━━━
IMPORTANT: Output ONLY the JSON object. No text before or after. Start with {{ and end with }}
{{
  "p_true": <float 0-1, where you think YES price will move TO>,
  "confidence": <float 0-1, how strong is the momentum catalyst>,
  "edge": <p_true minus {market['price']:.4f}>,
  "recommended_side": "<YES/NO/SKIP>",
  "momentum_direction": "<up/down/neutral>",
  "catalyst": "<what specific news/event/sentiment will move the price>",
  "price_target": <float, where you expect price to reach>,
  "time_horizon": "<hours until catalyst plays out, e.g. '4h', '24h', '48h'>",
  "key_factors_for": ["<specific fact that supports price movement>"],
  "key_factors_against": ["<specific fact against>"],
  "data_quality": "<strong/weak/none>",
  "volume_signal": "<high/medium/low/unknown>",
  "calibration_applied": "",
  "reasoning_summary": "<CATALYST: [what] → DIRECTION: [up/down] → TARGET: [price] because [specific reason]>"
}}"""

    try:
        raw = chat(prompt)
        # Robust JSON extraction
        raw = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        # Extract JSON block between first { and last }
        start = raw.find("{")
        end   = raw.rfind("}") + 1
        if start != -1 and end > start:
            raw = raw[start:end]

        # Try standard parse first
        try:
            result = json.loads(raw)
        except json.JSONDecodeError:
            # Fallback: fix common LLM JSON issues
            import re
            # Remove trailing commas before } or ]
            raw = re.sub(r",\s*([}\]])", r"\1", raw)
            # Replace single quotes with double quotes (careful with apostrophes)
            raw = re.sub(r"(?<![a-zA-Z])'([^']*)'(?![a-zA-Z])", r'"\1"', raw)
            # Remove comments
            raw = re.sub(r"//[^\n]*", "", raw)
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
    """Fetch recent news — Serper primary (Tavily quota exceeded), fallback to NewsAPI."""
    q = market.get("question", "")
    news = _fetch_serper(q)
    if news:
        return news
    news = _fetch_tavily(q)
    if news:
        return news
    return _fetch_newsapi(q)


def _fetch_serper(query: str) -> str:
    api_key = os.getenv("SERPER_API_KEY", "")
    if not api_key:
        return ""
    import requests
    try:
        resp = requests.post(
            "https://google.serper.dev/news",
            headers={"X-API-KEY": api_key, "Content-Type": "application/json"},
            json={"q": query, "num": 8},
            timeout=8,
        )
        if resp.status_code != 200:
            return ""
        items = resp.json().get("news", [])
        return "\n".join(f"- {i['title']}: {i.get('snippet','')}" for i in items)
    except Exception:
        return ""


def _fetch_tavily(query: str) -> str:
    api_key = os.getenv("TAVILY_API_KEY", "")
    if not api_key:
        return ""
    import requests
    try:
        resp = requests.post(
            "https://api.tavily.com/search",
            json={"api_key": api_key, "query": query, "max_results": 5,
                  "search_depth": "basic", "include_answer": True},
            timeout=8,
        )
        data = resp.json()
        if data.get("detail"):  # quota exceeded or error
            return ""
        lines = []
        if data.get("answer"):
            lines.append(f"[SUMMARY] {data['answer']}")
        for r in data.get("results", []):
            lines.append(f"- {r['title']}: {r.get('content','')[:200]}")
        return "\n".join(lines) or ""
    except Exception:
        return ""


def _fetch_newsapi(query: str) -> str:
    api_key = os.getenv("NEWS_API_KEY", "")
    if not api_key:
        return ""
    import requests
    try:
        resp = requests.get(
            "https://newsapi.org/v2/everything",
            params={"q": query, "pageSize": 5, "sortBy": "publishedAt", "apiKey": api_key},
            timeout=8,
        )
        articles = resp.json().get("articles", [])
        return "\n".join(f"- {a['title']}: {a.get('description','')}" for a in articles)
    except Exception:
        return ""
