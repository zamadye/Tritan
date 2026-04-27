"""Post-resolution learning system, performance reporting, and evolution context."""
import json
import os
from collections import defaultdict
from pathlib import Path


def _load_trades(filepath: str) -> list:
    p = Path(filepath)
    return json.loads(p.read_text()) if p.exists() else []


def _save_trades(trades: list, filepath: str):
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    Path(filepath).write_text(json.dumps(trades, indent=2))


def process_resolved_market(trade_id: str, actual_outcome: str, mode: str = "demo"):
    log_file = os.getenv(
        "DEMO_TRADES_FILE" if mode == "demo" else "LIVE_TRADES_FILE",
        f"./data/{mode}_trades.json",
    )
    trades = _load_trades(log_file)

    for trade in trades:
        if trade["trade_id"] == trade_id:
            trade["actual_outcome"] = actual_outcome
            trade["prediction_correct"] = trade["side"] == actual_outcome

            if trade["prediction_correct"]:
                payout = trade["size_usd"] / trade["price_at_entry"]
                trade["pnl"] = round(payout - trade["size_usd"], 2)
            else:
                trade["pnl"] = -trade["size_usd"]

            p = trade["price_at_entry"] if trade["side"] == "YES" else 1 - trade["price_at_entry"]
            outcome_binary = 1 if actual_outcome == "YES" else 0
            trade["brier_score"] = round((p - outcome_binary) ** 2, 4)

            # Calibration error: how far was our p_true from actual outcome
            trade["calibration_error"] = round(abs(trade.get("p_true_estimated", p) - outcome_binary), 4)

            result = "✅ WIN" if trade["prediction_correct"] else "❌ LOSS"
            print(f"📊 Resolved: {result} | P&L: ${trade['pnl']:+.2f} | Brier: {trade['brier_score']:.3f}")
            break

    _save_trades(trades, log_file)
    _update_calibration(trades)
    _generate_evolution_lessons(trades, mode)


def _infer_category(trade: dict) -> str:
    """Infer category from question if field is empty."""
    cat = trade.get("category", "")
    if cat and cat.strip():
        return cat.strip().lower()
    q = trade.get("market_question", "").lower()
    if any(x in q for x in ["vs.", "vs ", "tennis", "open:", "ipl", "ufc", "nba", "nfl", "mlb", "nhl", "grand prix", "soccer", "football"]):
        return "sports"
    if any(x in q for x in ["bitcoin", "btc", "eth", "crypto", "wti", "oil", "gold", "nasdaq"]):
        return "crypto"
    if any(x in q for x in ["iran", "trump", "war", "ceasefire", "hezbollah", "ukraine", "nato", "sanctions"]):
        return "geopolitik"
    if any(x in q for x in ["election", "president", "congress", "senate", "vote", "poll", "party", "minister"]):
        return "politics"
    if any(x in q for x in ["gdp", "inflation", "fed", "rate", "economy", "recession", "unemployment"]):
        return "economics"
    if any(x in q for x in ["openai", "gpt", "claude", "gemini", "ai model", "llm"]):
        return "ai"
    return "other"


    cal_file = os.getenv("CALIBRATION_FILE", "./data/calibration.json")
    stats = defaultdict(lambda: {"bets": 0, "wins": 0, "total_brier": 0.0, "overconfident": 0})

    for t in trades:
        if t.get("actual_outcome"):
            cat = _infer_category(t)
            stats[cat]["bets"] += 1
            stats[cat]["wins"] += 1 if t.get("prediction_correct") else 0
            stats[cat]["total_brier"] += t.get("brier_score", 0.25)
            # Track overconfidence: predicted high confidence but was wrong
            if not t.get("prediction_correct") and t.get("confidence_at_bet", 0) > 0.7:
                stats[cat]["overconfident"] += 1

    Path(cal_file).parent.mkdir(parents=True, exist_ok=True)
    Path(cal_file).write_text(json.dumps(dict(stats), indent=2))


def _generate_evolution_lessons(trades: list, mode: str = "demo"):
    """Generate structured lessons from resolved trades for LLM self-improvement."""
    resolved = [t for t in trades if t.get("actual_outcome")]
    if not resolved:
        return

    lessons = {
        "total_resolved": len(resolved),
        "overall_win_rate": sum(1 for t in resolved if t.get("prediction_correct")) / len(resolved),
        "category_bias": {},       # categories where agent is systematically wrong
        "overconfidence_patterns": [],  # cases where high confidence was wrong
        "underconfidence_patterns": [], # cases where low confidence was right
        "recent_mistakes": [],     # last 5 wrong predictions with details
        "calibration_adjustments": {},  # per-category confidence adjustment
    }

    # Category analysis
    cat_stats = defaultdict(lambda: {"bets": 0, "wins": 0, "avg_edge_claimed": 0.0, "avg_confidence": 0.0})
    for t in resolved:
        cat = _infer_category(t)
        cat_stats[cat]["bets"] += 1
        cat_stats[cat]["wins"] += 1 if t.get("prediction_correct") else 0
        cat_stats[cat]["avg_edge_claimed"] += abs(t.get("edge_at_bet", 0))
        cat_stats[cat]["avg_confidence"] += t.get("confidence_at_bet", 0.6)

    for cat, s in cat_stats.items():
        n = s["bets"]
        win_rate = s["wins"] / n
        avg_edge = s["avg_edge_claimed"] / n
        avg_conf = s["avg_confidence"] / n

        # Detect systematic bias
        if n >= 3:
            if win_rate < 0.40:
                lessons["category_bias"][cat] = {
                    "status": "AVOID",
                    "win_rate": round(win_rate, 2),
                    "note": f"Only {win_rate:.0%} win rate in {n} bets — agent consistently wrong here",
                }
            elif win_rate < 0.50:
                lessons["category_bias"][cat] = {
                    "status": "CAUTION",
                    "win_rate": round(win_rate, 2),
                    "note": f"Below 50% win rate — reduce confidence in {cat} markets",
                }

            # Calibration adjustment: if claimed high edge but losing, reduce confidence
            if avg_edge > 0.15 and win_rate < 0.45:
                lessons["calibration_adjustments"][cat] = round(-0.10, 2)  # reduce p_true by 10%
            elif avg_conf > 0.75 and win_rate < 0.50:
                lessons["calibration_adjustments"][cat] = round(-0.08, 2)

    # Recent mistakes (last 5 wrong predictions)
    mistakes = [t for t in reversed(resolved) if not t.get("prediction_correct")][:5]
    for t in mistakes:
        lessons["recent_mistakes"].append({
            "question": t.get("market_question", "")[:80],
            "category": _infer_category(t),
            "predicted_side": t.get("side"),
            "actual_outcome": t.get("actual_outcome"),
            "p_true_claimed": t.get("p_true_estimated", "?"),
            "confidence": t.get("confidence_at_bet", "?"),
            "lesson": _infer_lesson(t),
        })

    # Overconfidence: high confidence + wrong
    for t in resolved:
        if not t.get("prediction_correct") and t.get("confidence_at_bet", 0) >= 0.75:
            lessons["overconfidence_patterns"].append({
                "category": _infer_category(t),
                "confidence_claimed": t.get("confidence_at_bet"),
                "question_snippet": t.get("market_question", "")[:60],
            })

    # Underconfidence: low confidence + right (missed opportunity)
    for t in resolved:
        if t.get("prediction_correct") and t.get("confidence_at_bet", 1) <= 0.65:
            lessons["underconfidence_patterns"].append({
                "category": _infer_category(t),
                "confidence_claimed": t.get("confidence_at_bet"),
            })

    evo_file = os.getenv("EVOLUTION_FILE", "./data/evolution_lessons.json")
    if mode == "live":
        evo_file = evo_file.replace("evolution_lessons", "evolution_lessons_live")
    Path(evo_file).parent.mkdir(parents=True, exist_ok=True)
    Path(evo_file).write_text(json.dumps(lessons, indent=2))


def _infer_lesson(trade: dict) -> str:
    cat = trade.get("category", "")
    side = trade.get("side", "")
    actual = trade.get("actual_outcome", "")
    conf = trade.get("confidence_at_bet", 0)

    if conf and conf > 0.75:
        return f"Overconfident ({conf:.0%}) — was wrong. Reduce confidence in similar {cat} markets."
    if side == "YES" and actual == "NO":
        return f"Overestimated YES probability in {cat}. Check base rates more carefully."
    if side == "NO" and actual == "YES":
        return f"Underestimated YES probability in {cat}. Market may have had better information."
    return f"Prediction incorrect in {cat} — review reasoning methodology."


def get_evolution_context(mode: str = "demo") -> str:
    """Return a compact evolution context string to inject into LLM prompts.
    Live mode inherits all lessons from demo — mistakes in demo won't repeat in live.
    """
    evo_file = os.getenv("EVOLUTION_FILE", "./data/evolution_lessons.json")

    # Live mode: merge demo lessons + live lessons (demo lessons take priority as larger dataset)
    if mode == "live":
        demo_lessons = _load_lessons(evo_file)
        live_evo_file = evo_file.replace("evolution_lessons", "evolution_lessons_live")
        live_lessons  = _load_lessons(live_evo_file)
        lessons = _merge_lessons(demo_lessons, live_lessons)
    else:
        lessons = _load_lessons(evo_file)

    if not lessons or lessons.get("total_resolved", 0) == 0:
        return ""

    lines = [
        f"AGENT SELF-LEARNING CONTEXT ({lessons['total_resolved']} resolved trades, "
        f"overall win rate: {lessons['overall_win_rate']:.0%}):",
    ]

    if lessons.get("category_bias"):
        lines.append("Category performance warnings:")
        for cat, info in lessons["category_bias"].items():
            lines.append(f"  - {cat}: {info['status']} ({info['note']})")

    if lessons.get("calibration_adjustments"):
        lines.append("Calibration adjustments (apply to p_true estimates):")
        for cat, adj in lessons["calibration_adjustments"].items():
            lines.append(f"  - {cat}: {adj:+.0%} adjustment needed")

    if lessons.get("recent_mistakes"):
        lines.append("Recent mistakes to learn from:")
        for m in lessons["recent_mistakes"][:3]:
            lines.append(
                f"  - [{m['category']}] Predicted {m['predicted_side']}, "
                f"actual={m['actual_outcome']}, conf={m['confidence']} → {m['lesson']}"
            )

    if lessons.get("overconfidence_patterns"):
        n = len(lessons["overconfidence_patterns"])
        lines.append(f"Overconfidence detected {n}x — be more conservative with high-confidence calls.")

    return "\n".join(lines)


def _load_lessons(filepath: str) -> dict:
    try:
        p = Path(filepath)
        return json.loads(p.read_text()) if p.exists() else {}
    except Exception:
        return {}


def _merge_lessons(demo: dict, live: dict) -> dict:
    """Merge demo + live lessons. Demo has more data so it dominates."""
    if not demo and not live:
        return {}
    if not live:
        return demo
    if not demo:
        return live

    merged = dict(demo)
    merged["total_resolved"] = demo.get("total_resolved", 0) + live.get("total_resolved", 0)

    # Weighted win rate
    d_n = demo.get("total_resolved", 0)
    l_n = live.get("total_resolved", 0)
    d_wr = demo.get("overall_win_rate", 0)
    l_wr = live.get("overall_win_rate", 0)
    merged["overall_win_rate"] = round((d_wr * d_n + l_wr * l_n) / max(d_n + l_n, 1), 4)

    # Merge category bias — live overrides demo if live has enough data
    merged_bias = dict(demo.get("category_bias", {}))
    for cat, info in live.get("category_bias", {}).items():
        if cat not in merged_bias or l_n >= 5:
            merged_bias[cat] = info
    merged["category_bias"] = merged_bias

    # Merge calibration adjustments — average if both exist
    merged_cal = dict(demo.get("calibration_adjustments", {}))
    for cat, adj in live.get("calibration_adjustments", {}).items():
        if cat in merged_cal:
            merged_cal[cat] = round((merged_cal[cat] + adj) / 2, 3)
        else:
            merged_cal[cat] = adj
    merged["calibration_adjustments"] = merged_cal

    # Recent mistakes: combine last 5 from each, live mistakes first (more relevant)
    merged["recent_mistakes"] = (
        live.get("recent_mistakes", [])[:3] + demo.get("recent_mistakes", [])[:3]
    )[:5]

    # Overconfidence: combine all
    merged["overconfidence_patterns"] = (
        demo.get("overconfidence_patterns", []) + live.get("overconfidence_patterns", [])
    )

    return merged


def generate_performance_report(mode: str = "demo"):
    log_file = os.getenv(
        "DEMO_TRADES_FILE" if mode == "demo" else "LIVE_TRADES_FILE",
        f"./data/{mode}_trades.json",
    )
    trades = _load_trades(log_file)
    resolved = [t for t in trades if t.get("actual_outcome")]

    if not resolved:
        print("No resolved trades yet.")
        return

    stats = defaultdict(lambda: {"bets": 0, "wins": 0, "pnl": 0.0, "brier": []})
    for t in resolved:
        cat = _infer_category(t)
        stats[cat]["bets"] += 1
        stats[cat]["wins"] += 1 if t.get("prediction_correct") else 0
        stats[cat]["pnl"] += t.get("pnl", 0)
        stats[cat]["brier"].append(t.get("brier_score", 0.25))

    print("\n📈 PERFORMANCE REPORT BY CATEGORY")
    print("=" * 70)
    print(f"{'Category':<15} {'Bets':>5} {'Win%':>7} {'ROI':>8} {'Brier':>7}  Status")
    print("-" * 70)

    for cat, s in sorted(stats.items()):
        win_pct = s["wins"] / s["bets"] * 100
        avg_brier = sum(s["brier"]) / len(s["brier"])
        roi = s["pnl"] / max(s["bets"] * 10, 1) * 100
        status = "✅ GOOD" if win_pct >= 60 else "⚠️ CAUTION" if win_pct >= 50 else "❌ AVOID"
        print(f"{cat:<15} {s['bets']:>5} {win_pct:>6.1f}% {roi:>+7.1f}% {avg_brier:>7.3f}  {status}")


def get_stats(mode: str = "demo") -> dict:
    log_file = os.getenv(
        "DEMO_TRADES_FILE" if mode == "demo" else "LIVE_TRADES_FILE",
        f"./data/{mode}_trades.json",
    )
    trades = _load_trades(log_file)
    resolved = [t for t in trades if t.get("actual_outcome")]
    wins = sum(1 for t in resolved if t.get("prediction_correct"))
    total_pnl = sum(t.get("pnl", 0) for t in resolved)
    win_rate = wins / len(resolved) if resolved else 0.0
    brier_scores = [t.get("brier_score", 0.25) for t in resolved]
    avg_brier = sum(brier_scores) / len(brier_scores) if brier_scores else 0.25
    open_positions = len([t for t in trades if not t.get("actual_outcome")])

    return {
        "total_trades": len(trades),
        "resolved": len(resolved),
        "win_rate": win_rate,
        "total_pnl": total_pnl,
        "avg_brier": avg_brier,
        "open_positions": open_positions,
    }
