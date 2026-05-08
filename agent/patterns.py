"""Pattern Library — extract and serve historical price movement patterns.

Builds a knowledge base from resolved trades answering:
"For market type X with price characteristic Y, what is the historical outcome?"

Patterns are extracted from demo_trades.json and used as additional context
in the analyzer prompt — giving LLM historical precedent, not just real-time data.

Usage:
    from agent.patterns import get_pattern_context
    context = get_pattern_context(market, p_base, p_market)
"""
import json
import os
from pathlib import Path
from collections import defaultdict


PATTERN_FILE = Path("data/pattern_library.json")


def build_pattern_library(mode: str = "demo") -> dict:
    """Extract price movement patterns from resolved trade history.

    Patterns extracted:
    - By category: WR, avg edge, avg hold time
    - By price range: which entry prices are most profitable
    - By exit reason: which exit type generates most profit
    - By information_gap: does gap detection improve WR?

    Returns:
        dict: Pattern library saved to data/pattern_library.json
    """
    log_file = os.getenv("DEMO_TRADES_FILE" if mode == "demo" else "LIVE_TRADES_FILE",
                         f"./data/{mode}_trades.json")
    trades = json.loads(Path(log_file).read_text()) if Path(log_file).exists() else []
    resolved = [t for t in trades if t.get("actual_outcome") and t.get("pnl") is not None]

    if len(resolved) < 10:
        return {}  # not enough data yet

    patterns = {}

    # ── Pattern 1: Category performance ──────────────────────────────────────
    cat_stats = defaultdict(lambda: {"n": 0, "wins": 0, "pnl": 0.0, "edges": []})
    for t in resolved:
        cat = t.get("category", "other")
        cat_stats[cat]["n"] += 1
        if t.get("prediction_correct"):
            cat_stats[cat]["wins"] += 1
        cat_stats[cat]["pnl"] += t.get("pnl", 0)
        edge = t.get("edge_at_bet")
        if edge is not None:
            cat_stats[cat]["edges"].append(abs(edge))

    patterns["by_category"] = {}
    for cat, s in cat_stats.items():
        if s["n"] >= 3:
            avg_edge = sum(s["edges"]) / len(s["edges"]) if s["edges"] else 0
            patterns["by_category"][cat] = {
                "n": s["n"],
                "wr": round(s["wins"] / s["n"], 3),
                "total_pnl": round(s["pnl"], 2),
                "avg_edge": round(avg_edge, 3),
                "verdict": "STRONG" if s["wins"]/s["n"] >= 0.55 else
                           "WEAK" if s["wins"]/s["n"] < 0.45 else "NEUTRAL"
            }

    # ── Pattern 2: Entry price range performance ──────────────────────────────
    price_buckets = defaultdict(lambda: {"n": 0, "wins": 0, "pnl": 0.0})
    for t in resolved:
        price = t.get("price_at_entry", 0.5)
        bucket = f"{int(price * 10) * 10}-{int(price * 10) * 10 + 10}%"
        price_buckets[bucket]["n"] += 1
        if t.get("prediction_correct"):
            price_buckets[bucket]["wins"] += 1
        price_buckets[bucket]["pnl"] += t.get("pnl", 0)

    patterns["by_entry_price"] = {}
    for bucket, s in price_buckets.items():
        if s["n"] >= 3:
            patterns["by_entry_price"][bucket] = {
                "n": s["n"],
                "wr": round(s["wins"] / s["n"], 3),
                "total_pnl": round(s["pnl"], 2),
            }

    # ── Pattern 3: Information gap impact ────────────────────────────────────
    gap_trades    = [t for t in resolved if t.get("information_gap")]
    no_gap_trades = [t for t in resolved if not t.get("information_gap") and t.get("p_base")]

    if gap_trades:
        gap_wins = sum(1 for t in gap_trades if t.get("prediction_correct"))
        patterns["information_gap"] = {
            "with_gap":    {"n": len(gap_trades),    "wr": round(gap_wins / len(gap_trades), 3)},
            "without_gap": {"n": len(no_gap_trades), "wr": round(
                sum(1 for t in no_gap_trades if t.get("prediction_correct")) / len(no_gap_trades), 3
            ) if no_gap_trades else 0},
            "gap_adds_value": gap_wins / len(gap_trades) > 0.5 if gap_trades else False
        }

    # ── Pattern 4: Exit reason analysis ──────────────────────────────────────
    exit_stats = defaultdict(lambda: {"n": 0, "pnl": 0.0})
    for t in resolved:
        reason = t.get("exit_reason", "RESOLVED")
        key = ("TAKE_PROFIT" if "TAKE_PROFIT" in reason else
               "TRAILING_STOP" if "TRAILING" in reason else
               "STOP_LOSS" if "STOP_LOSS" in reason else
               "EVENT_DEADLINE" if "DEADLINE" in reason else "RESOLVED")
        exit_stats[key]["n"] += 1
        exit_stats[key]["pnl"] += t.get("pnl", 0)

    patterns["by_exit_reason"] = {
        k: {"n": v["n"], "avg_pnl": round(v["pnl"] / v["n"], 3)}
        for k, v in exit_stats.items() if v["n"] > 0
    }

    # ── Save ──────────────────────────────────────────────────────────────────
    patterns["_meta"] = {
        "total_resolved": len(resolved),
        "generated_from": log_file,
    }
    PATTERN_FILE.parent.mkdir(parents=True, exist_ok=True)
    PATTERN_FILE.write_text(json.dumps(patterns, indent=2))
    return patterns


def get_pattern_context(category: str, p_base: float, p_market: float) -> str:
    """Return relevant historical patterns as a string for LLM context.

    Called once per market analysis. Adds historical precedent without
    replacing real-time data — purely additive context.

    Args:
        category: Market category (sports, crypto, geopolitik, etc.)
        p_base: Calibrated base probability from statistical model.
        p_market: Current market price.

    Returns:
        str: Pattern summary for LLM, or empty string if insufficient data.
    """
    if not PATTERN_FILE.exists():
        return ""

    try:
        patterns = json.loads(PATTERN_FILE.read_text())
    except Exception:
        return ""

    total = patterns.get("_meta", {}).get("total_resolved", 0)
    if total < 10:
        return ""

    lines = []

    # Category pattern
    cat_data = patterns.get("by_category", {}).get(category)
    if cat_data and cat_data["n"] >= 3:
        lines.append(
            f"[PATTERN] {category.upper()}: WR={cat_data['wr']:.0%} "
            f"from {cat_data['n']} trades ({cat_data['verdict']})"
        )

    # Entry price pattern
    bucket = f"{int(p_market * 10) * 10}-{int(p_market * 10) * 10 + 10}%"
    price_data = patterns.get("by_entry_price", {}).get(bucket)
    if price_data and price_data["n"] >= 3:
        lines.append(
            f"[PATTERN] Entry {bucket}: WR={price_data['wr']:.0%} "
            f"from {price_data['n']} trades"
        )

    # Info gap value
    gap_data = patterns.get("information_gap")
    if gap_data:
        lines.append(
            f"[PATTERN] Info gap trades: WR={gap_data['with_gap']['wr']:.0%} "
            f"vs no-gap: WR={gap_data['without_gap']['wr']:.0%}"
        )

    return "\n".join(lines)


def refresh_patterns(mode: str = "demo") -> int:
    """Rebuild pattern library from current trade data. Returns trade count."""
    patterns = build_pattern_library(mode)
    return patterns.get("_meta", {}).get("total_resolved", 0)
