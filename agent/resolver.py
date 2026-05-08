"""Auto-resolver — polls Gamma API for resolved markets, updates P&L, triggers learning."""
import json
import os
import requests
from datetime import datetime, timezone
from pathlib import Path
from agent.learner import _generate_evolution_lessons, get_stats


def _load_trades(filepath: str) -> list:
    p = Path(filepath)
    return json.loads(p.read_text()) if p.exists() else []


def _save_trades(trades: list, filepath: str):
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    Path(filepath).write_text(json.dumps(trades, indent=2))


def _build_closed_index() -> dict:
    """Fetch closed AND active markets (active can have settled prices), index by question."""
    base = os.getenv('POLYMARKET_GAMMA_API', 'https://gamma-api.polymarket.com')
    index = {}
    for params in [
        {"active": "false", "closed": "true",  "limit": 200, "order": "volume24hr", "ascending": "false"},
        {"active": "true",  "closed": "false", "limit": 200, "order": "volume24hr", "ascending": "false"},
    ]:
        try:
            resp = requests.get(f"{base}/markets", params=params, timeout=10)
            for m in resp.json():
                q = m.get("question", "").lower().strip()
                if q:
                    index[q] = m
        except Exception as e:
            print(f"[RESOLVER] Index error: {e}")
    return index


def _parse_outcome(m: dict) -> str | None:
    """Extract YES/NO from market prices — regardless of closed/active status."""
    op_raw = m.get("outcomePrices", [])
    if isinstance(op_raw, str):
        try:
            op = json.loads(op_raw)
        except Exception:
            op = []
    else:
        op = op_raw

    if len(op) >= 2:
        try:
            yes_p = float(op[0])
            no_p  = float(op[1])
            if yes_p >= 0.99:
                return "YES"
            if no_p >= 0.99:
                return "NO"
        except (ValueError, TypeError):
            pass

    winner = m.get("winner", "").lower()
    if winner in ("yes", "true", "1"):
        return "YES"
    if winner in ("no", "false", "0"):
        return "NO"
    return None


def _resolve_outcome(condition_id: str, question: str, index: dict, numeric_id: str = "") -> str | None:
    """Resolve via numeric_id (most reliable) → name match in closed index."""
    base = os.getenv('POLYMARKET_GAMMA_API', 'https://gamma-api.polymarket.com')

    # 1. Numeric id — direct, reliable
    if numeric_id:
        try:
            m = requests.get(f"{base}/markets/{numeric_id}", timeout=8).json()
            outcome = _parse_outcome(m)
            if outcome:
                return outcome
        except Exception:
            pass

    # 2. Exact + fuzzy name match in closed index
    if question:
        q = question.lower().strip()
        if q in index:
            return _parse_outcome(index[q])
        for key, m in index.items():
            if q[:55] in key or key[:55] in q:
                outcome = _parse_outcome(m)
                if outcome:
                    return outcome

    return None


def check_and_resolve(mode: str = "demo") -> int:
    log_file = os.getenv(
        "DEMO_TRADES_FILE" if mode == "demo" else "LIVE_TRADES_FILE",
        f"./data/{mode}_trades.json",
    )
    trades = _load_trades(log_file)
    open_trades = [t for t in trades if not t.get("actual_outcome")]

    if not open_trades:
        print("[RESOLVER] No open trades to check.")
        return 0

    print(f"[RESOLVER] Checking {len(open_trades)} open trades...")

    # Build closed index ONCE (1 API call for all trades)
    closed_index = _build_closed_index()
    print(f"[RESOLVER] {len(closed_index)} closed markets indexed")

    resolved_count = 0
    for trade in open_trades:
        outcome = _resolve_outcome(
            trade.get("market_id", ""),
            trade.get("market_question", ""),
            closed_index,
            trade.get("market_numeric_id", ""),
        )

        if outcome is None:
            continue

        trade["actual_outcome"] = outcome
        trade["prediction_correct"] = trade["side"] == outcome
        trade["resolved_at"] = datetime.now(timezone.utc).isoformat()

        if trade["prediction_correct"]:
            entry_price = trade["price_at_entry"] if trade["side"] == "YES" else 1 - trade["price_at_entry"]
            payout = trade["size_usd"] / entry_price
            trade["pnl"] = round(payout - trade["size_usd"], 2)
        else:
            trade["pnl"] = -trade["size_usd"]

        p = trade["price_at_entry"] if trade["side"] == "YES" else 1 - trade["price_at_entry"]
        outcome_binary = 1 if outcome == "YES" else 0
        trade["brier_score"] = round((p - outcome_binary) ** 2, 4)
        trade["calibration_error"] = round(
            abs(trade.get("p_true_estimated", p) - outcome_binary), 4
        )

        result_icon = "✅ WIN" if trade["prediction_correct"] else "❌ LOSS"
        print(
            f"[RESOLVER] {result_icon} | {trade['market_question'][:55]}\n"
            f"           Side={trade['side']} Actual={outcome} "
            f"P&L=${trade['pnl']:+.2f} Brier={trade['brier_score']:.3f}"
        )
        # Update streak for stepped compounding
        from agent.bankroll import update_streak
        update_streak(trade["prediction_correct"], mode)
        resolved_count += 1

    if resolved_count > 0:
        _save_trades(trades, log_file)
        _generate_evolution_lessons(trades, mode)
        stats = get_stats(mode)
        print(
            f"\n[RESOLVER] 📊 {resolved_count} resolved | "
            f"Win rate: {stats['win_rate']:.0%} | "
            f"P&L: ${stats['total_pnl']:+.2f} | "
            f"Brier: {stats['avg_brier']:.3f}"
        )
        _save_pnl_summary(trades, mode)
        _trigger_assistant(trades, resolved_count)
    else:
        print("[RESOLVER] No new resolutions found.")

    return resolved_count


def _trigger_assistant(trades: list, resolved_count: int):
    """Notify assistant after trade closes — fire and forget."""
    try:
        import requests as _req
        dashboard_url = os.getenv("DASHBOARD_URL", "http://localhost:3000")
        resolved = [t for t in trades if t.get("actual_outcome")]
        recent = sorted(resolved, key=lambda x: x.get("resolved_at",""), reverse=True)[:resolved_count]
        summary = ", ".join(
            f"{'WIN' if t.get('prediction_correct') else 'LOSS'} {t['side']} ${t.get('pnl',0):+.2f}"
            for t in recent
        )
        _req.post(
            f"{dashboard_url}/api/assistant",
            json={"message": f"Just closed {resolved_count} trade(s): {summary}. Analyze and give brief insight.", "mode": "trade_close"},
            timeout=15,
        )
    except Exception:
        pass


def _save_pnl_summary(trades: list, mode: str):
    resolved = [t for t in trades if t.get("actual_outcome")]
    if not resolved:
        return
    wins = [t for t in resolved if t.get("prediction_correct")]
    total_pnl = sum(t.get("pnl", 0) for t in resolved)
    summary = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "total_resolved": len(resolved),
        "wins": len(wins),
        "losses": len(resolved) - len(wins),
        "win_rate": round(len(wins) / len(resolved), 4),
        "total_pnl": round(total_pnl, 2),
        "avg_brier": round(sum(t.get("brier_score", 0.25) for t in resolved) / len(resolved), 4),
        "biggest_win": max((t.get("pnl", 0) for t in resolved), default=0),
        "biggest_loss": min((t.get("pnl", 0) for t in resolved), default=0),
        "recent": [
            {"question": t["market_question"][:60], "side": t["side"],
             "outcome": t["actual_outcome"], "pnl": t.get("pnl", 0),
             "correct": t.get("prediction_correct")}
            for t in sorted(resolved, key=lambda x: x.get("resolved_at", ""), reverse=True)[:10]
        ],
    }
    pnl_file = os.getenv("PNL_SUMMARY_FILE", "./data/pnl_summary.json")
    Path(pnl_file).parent.mkdir(parents=True, exist_ok=True)
    Path(pnl_file).write_text(json.dumps(summary, indent=2))
    print(f"[RESOLVER] 💾 P&L summary saved → {pnl_file}")
