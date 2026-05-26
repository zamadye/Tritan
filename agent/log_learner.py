"""Log-based learning — reads analysis logs to extract lessons for current decisions.

Before each LLM analysis, agent checks:
1. Has this market (or similar) been analyzed before?
2. What was the decision and outcome?
3. What patterns led to wins vs losses?

Returns context string injected into LLM prompt.
"""
import re
import os
from pathlib import Path
from functools import lru_cache
from datetime import datetime, timezone, timedelta


LOG_DIR = Path("data/analysis_logs")
_cache: dict = {}
_cache_time: datetime = None
CACHE_TTL = 300  # 5 minutes


def _load_logs_cache() -> list[dict]:
    """Load and cache parsed logs."""
    global _cache, _cache_time
    now = datetime.now(timezone.utc)
    if _cache_time and (now - _cache_time).total_seconds() < CACHE_TTL:
        return list(_cache.values())

    if not LOG_DIR.exists():
        return []

    records = {}
    for f in sorted(LOG_DIR.glob("*.md"), reverse=True)[:500]:  # last 500 logs
        try:
            content = f.read_text()
            r = {"file": f.name}

            def get(pattern):
                m = re.search(pattern, content)
                return m.group(1).strip() if m else ""

            r["question"]   = get(r"\*\*Question:\*\* (.+)")
            r["category"]   = get(r"\*\*Category:\*\* (.+)")
            r["action"]     = get(r"\*\*Action:\*\* (.+)")
            r["confidence"] = get(r"\*\*Confidence:\*\* (.+)")
            r["gate_passed"]= "✅" in get(r"\*\*Passed:\*\* (.+)")
            r["gate_reason"]= get(r"\*\*Reason:\*\* (.+)")
            r["reasoning"]  = get(r"### Reasoning\n(.+)")
            r["info_gap"]   = get(r"\*\*Information Gap:\*\* (.+)")
            r["catalyst"]   = get(r"\*\*Catalyst Type:\*\* (.+)")

            outcome = re.search(r"\*\*(WIN|LOSS)\*\*.*P&L: \$([+-][\d.]+)", content)
            if outcome:
                r["result"] = outcome[1]
                r["pnl"] = float(outcome[2])

            records[f.name] = r
        except Exception:
            continue

    _cache = records
    _cache_time = now
    return list(records.values())


def get_similar_market_lessons(question: str, category: str, max_lessons: int = 3) -> str:
    """Find similar past analyses and extract lessons for current decision."""
    logs = _load_logs_cache()
    if not logs:
        return ""

    # Extract key words from question
    stopwords = {"will","the","and","for","are","was","has","have","been","that","this","with","from","win","lose"}
    words = {w.strip("?.,!()").lower() for w in question.split() if len(w) > 3 and w.lower() not in stopwords}

    # Find similar markets (same category + overlapping keywords)
    similar = []
    for log in logs:
        if log.get("category") != category:
            continue
        log_words = {w.strip("?.,!()").lower() for w in log.get("question","").split() if len(w) > 3}
        overlap = len(words & log_words)
        if overlap >= 2:
            similar.append((overlap, log))

    similar.sort(key=lambda x: -x[0])
    top = [log for _, log in similar[:max_lessons]]

    if not top:
        # Fallback: same category with outcomes
        resolved = [log for log in logs if log.get("category") == category and log.get("result")]
        top = resolved[:max_lessons]

    if not top:
        return ""

    lines = ["[PAST DECISIONS - similar markets]"]
    for log in top:
        result = log.get("result", "pending")
        pnl = f"${log.get('pnl',0):+.2f}" if log.get("result") else "unresolved"
        gate = "PASS" if log.get("gate_passed") else f"FAIL({log.get('gate_reason','')})"
        lines.append(
            f"  Q: {log.get('question','')[:60]}"
            f"\n  Decision: {log.get('action','?')} conf={log.get('confidence','?')} gate={gate}"
            f"\n  Outcome: {result} {pnl}"
            f"\n  Reason: {log.get('reasoning','')[:100]}"
        )

    return "\n".join(lines)


def get_category_win_rate(category: str) -> str:
    """Get win rate for this category from past logs."""
    logs = _load_logs_cache()
    resolved = [l for l in logs if l.get("category") == category and l.get("result")]
    if len(resolved) < 3:
        return ""
    wins = [l for l in resolved if l.get("result") == "WIN"]
    wr = len(wins) / len(resolved)
    return f"[CATEGORY STATS] {category}: {len(wins)}/{len(resolved)} = {wr:.0%} WR from past {len(resolved)} resolved"
