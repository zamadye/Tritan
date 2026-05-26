#!/usr/bin/env python3
"""Entry point CLI for POLY-AGENT."""
import argparse
import os
import sys
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Patch requests to bypass SSL for Polymarket (certificate expired on their end)
import requests as _req
_orig_get, _orig_post = _req.get, _req.post
def _get(url, **kw): 
    if 'polymarket.com' in str(url): kw.setdefault('verify', False)
    return _orig_get(url, **kw)
def _post(url, **kw):
    if 'polymarket.com' in str(url): kw.setdefault('verify', False)
    return _orig_post(url, **kw)
_req.get, _req.post = _get, _post

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"), override=True)


def main():
    parser = argparse.ArgumentParser(description="POLY-AGENT — Polymarket Trading Agent")
    parser.add_argument("--mode", choices=["demo", "live"], default=None)

    # Subcommands
    parser.add_argument("command", nargs="?", default="run",
                        choices=["run", "scan", "status", "report", "history", "learn",
                                 "analyze", "pause", "resume", "resolve"])
    parser.add_argument("args", nargs="*")
    args = parser.parse_args()

    mode = args.mode or os.getenv("AGENT_MODE", "demo")

    if args.command == "run":
        from agent.core import run
        run(mode)

    elif args.command == "scan":
        from agent.core import run_scan_cycle
        run_scan_cycle(mode)

    elif args.command == "status":
        from agent.learner import get_stats
        from rich.console import Console
        Console().print(get_stats(mode))

    elif args.command == "report":
        from agent.learner import generate_performance_report
        generate_performance_report(mode)

    elif args.command == "history":
        import json
        from pathlib import Path
        log_file = os.getenv(
            "DEMO_TRADES_FILE" if mode == "demo" else "LIVE_TRADES_FILE",
            f"./data/{mode}_trades.json",
        )
        trades = json.loads(Path(log_file).read_text()) if Path(log_file).exists() else []
        for t in trades[-20:]:
            outcome = t.get("actual_outcome", "OPEN")
            pnl = f"${t['pnl']:+.2f}" if t.get("pnl") is not None else "pending"
            print(f"[{t['mode'].upper()}] {t['side']} ${t['size_usd']:.2f} | {t['market_question'][:60]} | {outcome} | {pnl}")

    elif args.command == "learn":
        from agent.learner import generate_performance_report
        generate_performance_report(mode)

    elif args.command == "analyze":
        if not args.args:
            print("Usage: python main.py analyze <market_question_or_id>")
            sys.exit(1)
        from agent.analyzer import estimate_probability, fetch_news
        market = {"id": args.args[0], "question": " ".join(args.args), "price": 0.5, "end_date": "?"}
        news = fetch_news(market)
        result = estimate_probability(market, news)
        import json
        print(json.dumps(result, indent=2))

    elif args.command == "resolve":
        from agent.resolver import check_and_resolve
        n = check_and_resolve(mode)
        print(f"Resolved {n} trade(s).")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
