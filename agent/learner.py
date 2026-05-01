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
    if any(x in q for x in ["vs.", "vs ", "tennis", "open:", "ipl", "ufc", "nba", "nfl", "mlb", "nhl", "grand prix", "soccer", "football", "basketball", "baseball", "hockey", "playoffs", "series", "match", "game", "fight", "bout", "tournament", "championship"]):
        return "sports"
    if any(x in q for x in ["bitcoin", "btc", "eth", "crypto", "wti", "oil", "gold", "nasdaq"]):
        return "crypto"
    if any(x in q for x in ["iran", "trump", "war", "ceasefire", "hezbollah", "ukraine", "nato", "sanctions"]):
        return "geopolitik"
    if any(x in q for x in ["election", "president", "congress", "senate", "vote", "poll", "party", "minister", "arrested", "indicted", "impeach", "resign", "appointed", "confirmed", "nominated"]):
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
    """Generate momentum trading lessons — only from momentum-strategy trades (Apr 29+)."""
    # Filter: only use momentum trades (new strategy), not old base-rate trades
    momentum_cutoff = "2026-04-29"
    momentum_trades = [t for t in trades if (t.get("timestamp","") or "") >= momentum_cutoff]
    resolved = [t for t in momentum_trades if t.get("actual_outcome")]
    if not resolved:
        # Fallback to all trades if no momentum trades resolved yet
        resolved = [t for t in trades if t.get("actual_outcome")]
    if not resolved:
        return

    lessons = {
        "total_resolved": len(resolved),
        "overall_win_rate": round(sum(1 for t in resolved if t.get("prediction_correct")) / len(resolved), 3),
        "momentum_lessons": [],
        "price_movement_patterns": {},
        "exit_patterns": {},
        "edge_reality": {},
        "category_bias": {},
        "calibration_adjustments": {},
        "overconfidence_patterns": [],
        "recent_mistakes": [],
    }

    # Edge reality
    edge_buckets = defaultdict(lambda: {"n":0,"w":0})
    for t in resolved:
        e = abs(t.get("edge_at_bet") or 0)
        b = f"{round(e*10)*10:.0f}%"
        edge_buckets[b]["n"]+=1
        edge_buckets[b]["w"]+=int(bool(t.get("prediction_correct")))
    for b, s in edge_buckets.items():
        lessons["edge_reality"][b] = {"actual_wr": round(s["w"]/s["n"],2), "n": s["n"]}

    # Price movement patterns: entry price range → profit rate
    price_buckets = defaultdict(lambda: {"n":0,"w":0,"pnl":0.0})
    for t in resolved:
        ep = t.get("price_at_entry", 0.5)
        b = f"{int(ep*10)*10}-{int(ep*10)*10+10}%"
        price_buckets[b]["n"]+=1
        price_buckets[b]["w"]+=int(bool(t.get("prediction_correct")))
        price_buckets[b]["pnl"]+=t.get("pnl",0)
    for b, s in price_buckets.items():
        lessons["price_movement_patterns"][b] = {
            "win_rate": round(s["w"]/s["n"],2),
            "avg_pnl": round(s["pnl"]/s["n"],2),
            "n": s["n"]
        }

    # Exit patterns
    exit_counts = defaultdict(int)
    for t in resolved:
        r = t.get("exit_reason","RESOLVED")
        if "TAKE_PROFIT" in str(r): exit_counts["TAKE_PROFIT"]+=1
        elif "TRAILING" in str(r):  exit_counts["TRAILING_STOP"]+=1
        elif "STOP_LOSS" in str(r): exit_counts["STOP_LOSS"]+=1
        elif "TIME" in str(r):      exit_counts["TIME_LIMIT"]+=1
        else:                       exit_counts["RESOLVED"]+=1
    lessons["exit_patterns"] = dict(exit_counts)

    # Momentum lessons: profitable exits with catalyst
    for t in [t for t in reversed(resolved) if t.get("prediction_correct") and t.get("reasoning_summary")][:5]:
        lessons["momentum_lessons"].append({
            "category": _infer_category(t),
            "entry_price": t.get("price_at_entry"),
            "pnl": t.get("pnl"),
            "exit_reason": t.get("exit_reason","RESOLVED"),
            "catalyst": (t.get("reasoning_summary","")[:120]),
        })

    # Recent mistakes
    for t in [t for t in reversed(resolved) if not t.get("prediction_correct")][:3]:
        lessons["recent_mistakes"].append({
            "question": t.get("market_question","")[:70],
            "category": _infer_category(t),
            "entry_price": t.get("price_at_entry"),
            "reasoning": (t.get("reasoning_summary","")[:100]),
            "lesson": _infer_lesson(t),
        })

    # Overconfidence
    for t in resolved:
        if not t.get("prediction_correct") and t.get("confidence_at_bet",0) >= 0.70:
            lessons["overconfidence_patterns"].append({
                "category": _infer_category(t),
                "confidence_claimed": t.get("confidence_at_bet"),
            })

    evo_file = os.getenv("EVOLUTION_FILE", "./data/evolution_lessons.json")
    if mode == "live":
        evo_file = evo_file.replace("evolution_lessons", "evolution_lessons_live")
    Path(evo_file).parent.mkdir(parents=True, exist_ok=True)
    Path(evo_file).write_text(json.dumps(lessons, indent=2))


def _infer_lesson(trade: dict) -> str:
    cat   = _infer_category(trade)
    side  = trade.get("side", "")
    entry = trade.get("price_at_entry", 0.5)
    conf  = trade.get("confidence_at_bet", 0)
    reason = (trade.get("reasoning_summary") or "").lower()

    if conf and conf > 0.70:
        return f"Overconfident ({conf:.0%}) at entry {entry:.2f} in {cat}. Catalyst was weaker than claimed."
    if "base rate" in reason or "historically" in reason:
        return f"Used base rate instead of real catalyst in {cat}. No momentum signal = no bet."
    if entry > 0.70 and side == "YES":
        return f"Bought YES at {entry:.2f} — too expensive, little upside. Prefer entry <0.60 for YES bets."
    if entry < 0.15 and side == "YES":
        return f"Bought YES at {entry:.2f} — very low price needs very strong catalyst to move. Was catalyst strong enough?"
    if "no data" in reason or "no catalyst" in reason or "skip" in reason:
        return f"Bet without clear catalyst in {cat}. If no data → SKIP."
    return f"Momentum thesis failed in {cat} at entry {entry:.2f}. Review what catalyst was missing."


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
        f"MOMENTUM TRADING HISTORY ({lessons['total_resolved']} trades, WR={lessons['overall_win_rate']:.0%}):",
    ]

    if lessons.get("exit_patterns"):
        ep = lessons["exit_patterns"]
        lines.append(f"Exit breakdown: TP={ep.get('TAKE_PROFIT',0)} · Trail={ep.get('TRAILING_STOP',0)} · SL={ep.get('STOP_LOSS',0)} · Time={ep.get('TIME_LIMIT',0)} · Resolved={ep.get('RESOLVED',0)}")

    if lessons.get("price_movement_patterns"):
        best = sorted(lessons["price_movement_patterns"].items(), key=lambda x: x[1]["avg_pnl"], reverse=True)[:3]
        lines.append("Best entry price ranges (by avg P&L):")
        for b, d in best:
            lines.append(f"  {b}: WR={d['win_rate']:.0%} avg_pnl=${d['avg_pnl']:+.2f} (n={d['n']})")

    if lessons.get("momentum_lessons"):
        lines.append("What worked (profitable momentum trades):")
        for m in lessons["momentum_lessons"][:3]:
            lines.append(f"  [{m['category']}] entry={m.get('entry_price',0):.2f} pnl=${m.get('pnl',0):+.2f} via {m.get('exit_reason','?')}: {m.get('catalyst','')[:80]}")

    if lessons.get("recent_mistakes"):
        lines.append("Recent losses (avoid repeating):")
        for m in lessons["recent_mistakes"]:
            lines.append(f"  [{m['category']}] entry={m.get('entry_price',0):.2f}: {m.get('lesson','')[:80]}")

    if lessons.get("overconfidence_patterns"):
        n = len(lessons["overconfidence_patterns"])
        lines.append(f"Overconfidence: {n}x high-conf bets were wrong — stay disciplined on catalyst quality.")

    return "\n".join(lines)[:800]  # cap at 800 chars to save tokens


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
