"""Fine-tuning evaluator — runs every 30-50 trades to identify what's working and what's not.

Analyzes:
1. Which catalyst types lead to wins vs losses
2. Which categories have positive/negative edge
3. Whether confidence correlates with outcomes
4. Common exit patterns (TP hit vs trailing stop vs SL)
5. Generates actionable parameter adjustments
"""
import json
import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone


EVAL_INTERVAL = int(os.getenv("EVAL_INTERVAL_TRADES", 30))
EVAL_FILE = Path("data/fine_tune_eval.json")


def should_run_evaluation(trades: list) -> bool:
    """Check if we've accumulated enough new trades since last eval."""
    resolved = [t for t in trades if t.get("actual_outcome")]
    n = len(resolved)
    if n < 10:
        return False

    # Load last eval count
    if EVAL_FILE.exists():
        try:
            last = json.loads(EVAL_FILE.read_text())
            last_n = last.get("trade_count", 0)
            return (n - last_n) >= EVAL_INTERVAL
        except Exception:
            pass
    return n >= EVAL_INTERVAL


def run_fine_tune_evaluation(trades: list, mode: str = "live") -> dict:
    """Analyze all resolved trades and generate fine-tuning insights."""
    resolved = [t for t in trades if t.get("actual_outcome")]
    if len(resolved) < 10:
        return {}

    # Only use real P&L (sell executed or natural resolve)
    def is_real(t):
        return bool(t.get("sell_order_id")) or t.get("actual_outcome") in ("YES", "NO")

    # ── 1. Catalyst type analysis ──────────────────────────────────────
    catalyst_stats = defaultdict(lambda: {"w": 0, "l": 0, "pnl": 0.0})
    for t in resolved:
        cat_type = t.get("catalyst_type", "NONE") or "NONE"
        win = t.get("prediction_correct", False)
        pnl = t.get("pnl", 0) or 0
        catalyst_stats[cat_type]["w" if win else "l"] += 1
        catalyst_stats[cat_type]["pnl"] += pnl

    # ── 2. Category analysis ───────────────────────────────────────────
    cat_stats = defaultdict(lambda: {"w": 0, "l": 0, "pnl": 0.0})
    for t in resolved:
        cat = t.get("category", "other") or "other"
        win = t.get("prediction_correct", False)
        cat_stats[cat]["w" if win else "l"] += 1
        cat_stats[cat]["pnl"] += t.get("pnl", 0) or 0

    # ── 3. Confidence calibration ──────────────────────────────────────
    conf_buckets = defaultdict(lambda: {"w": 0, "l": 0})
    for t in resolved:
        conf = float(t.get("confidence_at_bet") or 0)
        bucket = f"{int(conf * 10) * 10}-{int(conf * 10) * 10 + 10}%"
        conf_buckets[bucket]["w" if t.get("prediction_correct") else "l"] += 1

    # ── 4. Exit pattern analysis ───────────────────────────────────────
    exit_stats = defaultdict(lambda: {"count": 0, "pnl": 0.0, "wins": 0})
    for t in resolved:
        r = t.get("exit_reason", "") or t.get("actual_outcome", "")
        if "TAKE_PROFIT" in r:    key = "TAKE_PROFIT"
        elif "TRAILING" in r:     key = "TRAILING_STOP"
        elif "STOP_LOSS" in r:    key = "STOP_LOSS"
        elif "DEADLINE" in r or "EVENT" in r: key = "TIME_DEADLINE"
        elif "THESIS" in r:       key = "THESIS_INVALID"
        else:                     key = "RESOLVED"
        exit_stats[key]["count"] += 1
        exit_stats[key]["pnl"] += t.get("pnl", 0) or 0
        if t.get("prediction_correct"):
            exit_stats[key]["wins"] += 1

    # ── 5. Information gap analysis ────────────────────────────────────
    info_gap_stats = {"with_gap": {"w": 0, "l": 0}, "no_gap": {"w": 0, "l": 0}}
    for t in resolved:
        has_gap = t.get("information_edge", False) or t.get("information_gap", False)
        key = "with_gap" if has_gap else "no_gap"
        info_gap_stats[key]["w" if t.get("prediction_correct") else "l"] += 1

    # ── 6. Generate actionable insights ───────────────────────────────
    insights = []
    recommendations = {}

    # Catalyst insights
    for cat_type, s in catalyst_stats.items():
        n = s["w"] + s["l"]
        if n >= 3:
            wr = s["w"] / n
            if wr < 0.35 and n >= 5:
                insights.append(f"⚠️ CATALYST {cat_type}: WR={wr:.0%} ({n} trades) — consider skipping")
            elif wr >= 0.65 and n >= 3:
                insights.append(f"✅ CATALYST {cat_type}: WR={wr:.0%} ({n} trades) — strong signal")

    # Category insights
    for cat, s in cat_stats.items():
        n = s["w"] + s["l"]
        if n >= 5:
            wr = s["w"] / n
            avg_pnl = s["pnl"] / n
            if wr < 0.40:
                insights.append(f"⚠️ CATEGORY {cat}: WR={wr:.0%} avg_pnl=${avg_pnl:+.2f} — reduce exposure")
                recommendations[f"reduce_{cat}"] = True
            elif wr >= 0.60:
                insights.append(f"✅ CATEGORY {cat}: WR={wr:.0%} avg_pnl=${avg_pnl:+.2f} — increase priority")

    # Exit insights
    sl_data = exit_stats.get("STOP_LOSS", {})
    if sl_data.get("count", 0) >= 5:
        sl_pct = sl_data["count"] / len(resolved)
        if sl_pct > 0.40:
            insights.append(f"⚠️ STOP_LOSS rate {sl_pct:.0%} — SL too tight or entries too aggressive")
            recommendations["loosen_sl"] = True

    trailing_data = exit_stats.get("TRAILING_STOP", {})
    if trailing_data.get("count", 0) >= 3:
        trailing_pnl = trailing_data["pnl"] / trailing_data["count"]
        if trailing_pnl < 0:
            insights.append(f"⚠️ TRAILING_STOP avg P&L ${trailing_pnl:+.2f} — trail too loose, tighten")
            recommendations["tighten_trail"] = True

    # Info gap insights
    with_gap = info_gap_stats["with_gap"]
    no_gap = info_gap_stats["no_gap"]
    wg_n = with_gap["w"] + with_gap["l"]
    ng_n = no_gap["w"] + no_gap["l"]
    if wg_n >= 3 and ng_n >= 3:
        wg_wr = with_gap["w"] / wg_n
        ng_wr = no_gap["w"] / ng_n
        if wg_wr > ng_wr + 0.15:
            insights.append(f"✅ INFO_GAP bets WR={wg_wr:.0%} vs no-gap WR={ng_wr:.0%} — prioritize info gap")
        elif ng_wr > wg_wr + 0.10:
            insights.append(f"⚠️ No-gap bets WR={ng_wr:.0%} > info-gap WR={wg_wr:.0%} — info gap not predictive")

    # ── 7. Save evaluation ─────────────────────────────────────────────
    eval_result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "trade_count": len(resolved),
        "real_trade_count": sum(1 for t in resolved if is_real(t)),
        "overall_wr": round(sum(1 for t in resolved if t.get("prediction_correct")) / len(resolved), 3),
        "total_pnl": round(sum(t.get("pnl", 0) or 0 for t in resolved if is_real(t)), 2),
        "catalyst_analysis": {k: {**v, "wr": round(v["w"]/(v["w"]+v["l"]), 2) if v["w"]+v["l"] > 0 else 0}
                               for k, v in catalyst_stats.items()},
        "category_analysis": {k: {**v, "wr": round(v["w"]/(v["w"]+v["l"]), 2) if v["w"]+v["l"] > 0 else 0}
                               for k, v in cat_stats.items()},
        "confidence_calibration": {k: {**v, "wr": round(v["w"]/(v["w"]+v["l"]), 2) if v["w"]+v["l"] > 0 else 0}
                                    for k, v in conf_buckets.items()},
        "exit_analysis": dict(exit_stats),
        "info_gap_analysis": info_gap_stats,
        "insights": insights,
        "recommendations": recommendations,
    }

    EVAL_FILE.write_text(json.dumps(eval_result, indent=2))

    print(f"\n{'='*60}")
    print(f"[FINE-TUNE] 📊 Evaluation at {len(resolved)} trades | WR={eval_result['overall_wr']:.0%} | Net P&L=${eval_result['total_pnl']:+.2f}")
    for insight in insights:
        print(f"[FINE-TUNE] {insight}")
    print(f"{'='*60}\n")

    return eval_result
