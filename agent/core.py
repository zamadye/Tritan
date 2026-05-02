"""Main agent loop — orchestrates scan → analyze → size → execute."""
import os
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

from agent.scanner import get_candidate_markets
from agent.analyzer import estimate_probability, fetch_news
from agent.sizer import calculate_position
from agent.executor import execute_trade
from agent.learner import get_stats, generate_performance_report, get_evolution_context
from agent.resolver import check_and_resolve

console = Console()


def _get_bankroll(mode: str) -> float:
    if mode == "demo":
        base = float(os.getenv("DEMO_BANKROLL", 20.0))
        log_file = os.getenv("DEMO_TRADES_FILE", "./data/demo_trades.json")
        trades = json.loads(Path(log_file).read_text()) if Path(log_file).exists() else []
        deployed = sum(t["size_usd"] for t in trades if not t.get("actual_outcome"))
        pnl = sum(t.get("pnl", 0) for t in trades if t.get("actual_outcome"))
        return round(max(base - deployed + pnl, 0), 2)
    else:
        # Live: fetch real USDC balance from Polygon
        try:
            import requests as _req
            wallet = os.getenv("POLYGON_WALLET_ADDRESS", "")
            rpc = "https://polygon-mainnet.g.alchemy.com/v2/-LJWrAuXvUC8QszJzGzs0"
            USDC = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
            data = "0x70a08231000000000000000000000000" + wallet[2:].zfill(64)
            r = _req.post(rpc, json={"jsonrpc":"2.0","method":"eth_call",
                "params":[{"to":USDC,"data":data},"latest"],"id":1}, timeout=5)
            bal = int(r.json().get("result","0x0"), 16) / 1e6
            return round(bal, 2) if bal > 0 else float(os.getenv("DEMO_BANKROLL", 20.0))
        except Exception:
            return float(os.getenv("DEMO_BANKROLL", 20.0))


def _open_market_ids(mode: str) -> set:
    """Return set of market questions that already have an open position (no duplicate bets).
    Lost markets are NOT blocked — the learning system (evolution_lessons) handles caution instead.
    """
    log_file = os.getenv("DEMO_TRADES_FILE" if mode == "demo" else "LIVE_TRADES_FILE",
                         f"./data/{mode}_trades.json")
    trades = json.loads(Path(log_file).read_text()) if Path(log_file).exists() else []
    blocked = set()
    for t in trades:
        if not t.get("actual_outcome"):
            blocked.add(t["market_question"][:60])
    return blocked


def _enrich_trade(trade: dict, analysis: dict, mode: str):
    log_file = os.getenv("DEMO_TRADES_FILE" if mode == "demo" else "LIVE_TRADES_FILE",
                         f"./data/{mode}_trades.json")
    p = Path(log_file)
    trades = json.loads(p.read_text()) if p.exists() else []
    for t in trades:
        if t["trade_id"] == trade["trade_id"]:
            t["p_true_estimated"]   = analysis.get("p_true_estimated", analysis.get("p_true"))
            t["confidence_at_bet"]  = analysis.get("confidence_at_bet", analysis.get("confidence"))
            t["edge_at_bet"]        = analysis.get("edge_at_bet", analysis.get("edge"))
            t["base_rate"]          = analysis.get("base_rate")
            t["resolution_clarity"] = analysis.get("resolution_clarity")
            t["reasoning_summary"]  = analysis.get("reasoning_summary")
            t["calibration_applied"]= analysis.get("calibration_applied", "")
            t["key_factors_for"]    = analysis.get("key_factors_for", [])
            t["key_factors_against"]= analysis.get("key_factors_against", [])
            break
    p.write_text(json.dumps(trades, indent=2))


def _build_clob_client():
    try:
        from py_clob_client.client import ClobClient
        host = os.getenv("POLYMARKET_CLOB_HOST", "https://clob.polymarket.com")
        client = ClobClient(host, key=os.getenv("POLYGON_PRIVATE_KEY", ""),
                            chain_id=int(os.getenv("CHAIN_ID", 137)),
                            signature_type=int(os.getenv("SIGNATURE_TYPE", 0)))
        client.set_api_creds(client.create_or_derive_api_creds())
        return client
    except Exception as e:
        console.print(f"[red]CLOB client init failed: {e}[/red]")
        return None


def print_banner(mode: str):
    stats = get_stats(mode)
    bankroll = _get_bankroll(mode)
    win_pct = f"{stats['win_rate']*100:.1f}%" if stats["resolved"] else "N/A"
    console.print(Panel(
        f"[bold cyan]🤖 POLY-AGENT v2.0[/bold cyan]\n"
        f"Mode: [yellow]{'DEMO 📝' if mode == 'demo' else 'LIVE 💰'}[/yellow]\n"
        f"Bankroll: [green]${bankroll:,.2f} USDC[/green]\n"
        f"Total Trades: {stats['total_trades']} | Win Rate: {win_pct}\n"
        f"ROI: {stats['total_pnl']:+.2f} | Brier: {stats['avg_brier']:.3f}\n"
        f"Open Positions: {stats['open_positions']}",
        title="POLY-AGENT", border_style="cyan",
    ))


def run_scan_cycle(mode: str, clob_client=None):
    min_confidence = float(os.getenv("MIN_CONFIDENCE", 0.65))
    max_open = int(os.getenv("MAX_OPEN_POSITIONS", 5))
    delay = float(os.getenv("API_RATE_LIMIT_DELAY", 8.0))

    # Step 1: resolve settled markets + update learning
    check_and_resolve(mode)

    # Step 1b: check exit conditions (TP/SL/time limit)
    from agent.monitor import check_and_exit
    check_and_exit(mode)

    # Step 2: check bankroll + open positions (count only truly open, not blocked)
    bankroll = _get_bankroll(mode)
    open_ids = _open_market_ids(mode)
    # Count only unresolved trades for position limit
    log_file = os.getenv("DEMO_TRADES_FILE" if mode == "demo" else "LIVE_TRADES_FILE",
                         f"./data/{mode}_trades.json")
    all_trades = json.loads(Path(log_file).read_text()) if Path(log_file).exists() else []
    open_count = len([t for t in all_trades if not t.get("actual_outcome")])

    if bankroll < float(os.getenv("MIN_BET_SIZE", 0.50)):
        console.print(f"[yellow]⚠️  Bankroll ${bankroll:.2f} too low to bet. Waiting for resolutions.[/yellow]")
        return

    if open_count >= max_open:
        console.print(f"[yellow]⚠️  Max open positions ({max_open}) reached. Waiting for resolutions.[/yellow]")
        return

    # Step 3: load evolution context ONCE per cycle
    evo_context = get_evolution_context(mode)
    if evo_context:
        console.print(f"\n[dim]🧠 Evolution context loaded[/dim]")

    # Step 3b: Regime filter — skip if market is dead (no point trading noise)
    try:
        from agent.research import get_macro_context as _gmc
        _macro = _gmc()
        _btc_change = abs(_macro.get("crypto_sentiment",{}).get("btc_24h", 99))
        _fg = _macro.get("fear_greed",{}).get("values",[50])
        _fg_val = _fg[0] if _fg else 50
        if _btc_change < 0.5 and 45 <= _fg_val <= 55:
            console.print("[yellow]💤 Regime filter: market dead (BTC flat + F&G neutral). Skipping cycle.[/yellow]")
            return
    except Exception:
        pass

    # Step 4: scan
    console.print("\n[bold]🔍 Scanning markets...[/bold]")
    candidates = get_candidate_markets()
    console.print(f"Found {len(candidates)} candidate markets.")

    # Step 4b: fetch macro context ONCE per cycle (shared across all markets)
    from agent.research import get_macro_context, format_research_for_llm
    from agent.osint import get_fear_greed_trend
    macro_ctx = get_macro_context()
    fg_trend   = get_fear_greed_trend()
    cycle_macro = "\n".join(filter(None, [
        f"[MACRO] Fear&Greed: {macro_ctx.get('fear_greed',{}).get('current','?')} | trend: {macro_ctx.get('fear_greed',{}).get('7d_trend','?')}",
        f"[MACRO] BTC: ${macro_ctx.get('crypto_sentiment',{}).get('btc_price',0):,.0f} ({macro_ctx.get('crypto_sentiment',{}).get('btc_24h',0):+.1f}% 24h) → {macro_ctx.get('crypto_sentiment',{}).get('risk_signal','?')}",
        fg_trend,
    ]))

    bets_this_cycle = 0
    max_bets_per_cycle = min(max_open - open_count, 5)  # max 5 bets per cycle

    # Build prev_loss lookup — block market if lost 2+ times today
    from datetime import datetime, timezone, timedelta
    cutoff_24h = datetime.now(timezone.utc) - timedelta(hours=24)
    loss_count = {}
    for t in all_trades:
        if t.get("actual_outcome") and not t.get("prediction_correct"):
            try:
                ts = datetime.fromisoformat(t.get("resolved_at", t.get("timestamp","")).replace("Z","+00:00"))
                if ts > cutoff_24h:
                    key = t["market_question"][:60]
                    loss_count[key] = loss_count.get(key, 0) + 1
            except Exception:
                pass

    hard_blocked      = {k for k, v in loss_count.items() if v >= 2}
    prev_loss_markets = {k for k, v in loss_count.items() if v == 1}

    # Correlation control: count open positions per category
    from agent.learner import _infer_category
    MAX_PER_CATEGORY = int(os.getenv("MAX_OPEN_PER_CATEGORY", 3))
    MAX_CATEGORY_EXPOSURE = float(os.getenv("MAX_CATEGORY_EXPOSURE_PCT", 0.30))  # 30% bankroll
    cat_open_count    = {}
    cat_open_exposure = {}
    for t in all_trades:
        if not t.get("actual_outcome"):
            cat = _infer_category(t)
            cat_open_count[cat]    = cat_open_count.get(cat, 0) + 1
            cat_open_exposure[cat] = cat_open_exposure.get(cat, 0.0) + t["size_usd"]

    # Pre-filter: only analyze top 5 markets by volume (save LLM calls)
    MAX_LLM_CALLS = int(os.getenv("MAX_LLM_CALLS_PER_CYCLE", 5))
    llm_calls_this_cycle = 0

    for market in candidates:
        if bets_this_cycle >= max_bets_per_cycle:
            break
        if llm_calls_this_cycle >= MAX_LLM_CALLS:
            break
        if market["question"][:60] in open_ids:
            continue

        # Correlation filter: skip if category already at limit
        mcat = _infer_category({"category": market.get("category",""), "market_question": market.get("question","")})
        # Backfill category into market dict for executor
        if not market.get("category"):
            market["category"] = mcat
        if cat_open_count.get(mcat, 0) >= MAX_PER_CATEGORY:
            console.print(f"[dim]⛔ Corr limit ({mcat} {cat_open_count[mcat]}/{MAX_PER_CATEGORY}): {market['question'][:45]}[/dim]")
            continue
        if cat_open_exposure.get(mcat, 0) >= bankroll * MAX_CATEGORY_EXPOSURE:
            console.print(f"[dim]⛔ Exposure limit ({mcat} ${cat_open_exposure[mcat]:.2f}): {market['question'][:45]}[/dim]")
            continue
        if market["question"][:60] in hard_blocked:
            continue

        # Quick pre-filter without LLM: skip if price too extreme (no room to move)
        price = market["price"]
        if price < 0.06 or price > 0.94:
            continue

        # Research: cached 30min — no extra API cost if cached
        from agent.research import build_research_report, format_research_for_llm
        research      = build_research_report(market)
        research_ctx  = format_research_for_llm(research)
        news          = fetch_news(market)
        combined_news = "\n".join(filter(None, [cycle_macro, research_ctx, news]))

        prev_loss = market["question"][:60] in prev_loss_markets
        llm_calls_this_cycle += 1
        analysis = estimate_probability(market, combined_news, evo_context, prev_loss=prev_loss)
        time.sleep(delay)

        confidence = analysis.get("confidence", 0)
        p_true     = analysis.get("p_true", market["price"])
        p_market   = market["price"]

        if confidence < min_confidence:
            continue

        # Use momentum direction if available
        momentum = analysis.get("momentum_direction", "")
        rec_side  = analysis.get("recommended_side", "SKIP")
        if rec_side == "SKIP":
            continue

        bankroll = _get_bankroll(mode)
        size, side, _ = calculate_position(p_true, p_market, bankroll)

        if side == "SKIP" or size == 0:
            continue

        console.print(
            f"\n[green]═══ MARKET ANALYSIS ═══[/green]\n"
            f"Market: {market['question']}\n"
            f"p_true: {p_true:.2%} | p_market: {p_market:.2%} | Edge: {p_true-p_market:+.2%}\n"
            f"Confidence: {confidence:.0%} | Decision: BET {side} ${size:.2f}\n"
            f"Reasoning: {analysis.get('reasoning_summary','')[:120]}"
        )

        trade = execute_trade(market, side, size, mode, clob_client)
        _enrich_trade(trade, analysis, mode)
        open_ids.add(market["question"])
        # Update correlation counters
        cat_open_count[mcat]    = cat_open_count.get(mcat, 0) + 1
        cat_open_exposure[mcat] = cat_open_exposure.get(mcat, 0.0) + size
        bets_this_cycle += 1


def run(mode: str):
    print_banner(mode)

    clob_client = None
    if mode == "live":
        clob_client = _build_clob_client()
        if not clob_client:
            console.print("[red]Cannot start LIVE mode without CLOB client. Falling back to DEMO.[/red]")
            mode = "demo"

    base_interval = int(os.getenv("SCAN_INTERVAL_MINUTES", 15)) * 60
    # Jam aktif Polymarket: 14:00-22:00 UTC → scan lebih cepat
    active_interval = int(os.getenv("SCAN_INTERVAL_ACTIVE_MINUTES", 5)) * 60

    while True:
        try:
            hour_utc = datetime.now(timezone.utc).hour
            is_active = 14 <= hour_utc < 22
            interval  = active_interval if is_active else base_interval

            run_scan_cycle(mode, clob_client)
        except KeyboardInterrupt:
            console.print("\n[yellow]Agent paused by user.[/yellow]")
            break
        except Exception as e:
            console.print(f"[red]Cycle error: {e}[/red]")

        label = "🔥 ACTIVE" if is_active else "💤 OFF-PEAK"
        console.print(f"\n⏳ [{label}] Next scan in {interval//60} min...")
        time.sleep(interval)
