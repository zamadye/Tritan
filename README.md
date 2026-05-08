# TRITAN — Prediction Market Edge System

Automated trading framework for Polymarket with agentic LLM verification and statistical edge detection.

---

## What This Solves

Most prediction market bots fail for three reasons:

1. **LLM as predictor** — LLMs don't have an edge over market prices. TRITAN uses LLMs only to detect information gaps, not to predict outcomes.
2. **No statistical baseline** — Without calibration against historical data, every bet is a guess. TRITAN calibrates against 19,624 resolved markets.
3. **No audit trail** — Can't improve what you can't measure. Every trade logs the exact data sources, tool calls, and reasoning used.

---

## How It Works

```
Market scan (Gamma API)
    ↓
Statistical gate — p_calibrated vs market_price (≥8% gap required)
    ↓
Agentic verification — LLM autonomously fetches relevant data:
    • search_web (Tavily/NewsAPI)
    • get_crypto_price (CoinGecko)
    • get_sports_data (ESPN)
    • get_market_context (Polymarket)
    ↓
Confidence gate — per-category threshold
    ↓
Position sizing (Kelly fraction)
    ↓
Execution + full audit log
    ↓
Auto-exit: Take Profit / Trailing Stop / Time limit
```

---

## Architecture

```
TRITAN/
├── agent/
│   ├── core.py        # Main loop, scan cycle, gate logic
│   ├── scanner.py     # Market discovery via Gamma API
│   ├── analyzer.py    # Statistical prior + agentic LLM layer
│   ├── executor.py    # Order execution (demo + live)
│   ├── monitor.py     # Auto-exit: TP/SL/trailing/time
│   ├── resolver.py    # Outcome resolution + P&L calculation
│   ├── sizer.py       # Kelly position sizing
│   ├── learner.py     # Performance tracking + evolution
│   ├── tools.py       # Agentic tool executors
│   ├── research.py    # Macro context fetcher
│   └── osint.py       # Category-specific signal aggregator
│
├── web/               # Next.js dashboard
│   └── app/api/       # Stats, agent control, settings
│
├── data/
│   ├── statistical_prior.json    # 19,624 resolved market priors
│   ├── calibration_model.json    # Logistic regression per category
│   └── demo_trades.json          # Full trade audit trail
│
├── main.py            # CLI entry point
├── requirements.txt   # Pinned dependencies
└── .env.example       # Configuration template
```

---

## Key Differentiators

**Statistical calibration** — Not LLM guessing. Logistic regression model trained on 19,624 resolved Polymarket markets. Brier score improvement over naive baseline: 7.6% (category `other`), up to 17.9% (geopolitik).

**Agentic tool loop** — LLM doesn't receive generic news. It autonomously decides which tools to call per market: crypto price for BTC markets, ESPN injuries for sports, web search for geopolitical events. Max 3 iterations, 45s timeout, full cost control.

**Full audit trail** — Every trade logs: `p_base`, `p_base_source`, `p_base_n`, `tool_calls_log`, `information_gap`, `information_gap_reason`, `brier_score`. Buyer can verify every decision independently.

**Strict gate** — Bet only when: (1) statistical edge ≥8%, (2) LLM confirms information gap OR category has proven edge, (3) confidence ≥ per-category threshold. High-risk categories (crypto, geopolitik, politics) require ≥10% edge.

---

## Tech Stack

- **Python 3.13** — Core agent
- **Polymarket CLOB + Gamma API** — Market data and execution
- **MiMo v2.5** (OpenAI-compatible) — Reasoning LLM
- **Tavily + NewsAPI** — Real-time search
- **CoinGecko + ESPN + Odds API** — Category-specific data
- **Next.js 16** — Web dashboard with auth
- **Systemd** — Production deployment

---

## Setup

```bash
git clone <repo>
cd TRITAN
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill in your keys
python main.py run    # starts in demo mode
```

Dashboard: `cd web && npm install && npm run build && npm start`

---

## Configuration

All behavior controlled via `.env`. Key settings:

| Variable | Default | Description |
|---|---|---|
| `AGENT_MODE` | `demo` | `demo` or `live` |
| `MIN_STAT_EDGE` | `0.08` | Minimum statistical edge to analyze |
| `MIN_CONFIDENCE` | `0.55` | Minimum LLM confidence to bet |
| `EXIT_TAKE_PROFIT` | `0.15` | Exit at +15% return |
| `EXIT_STOP_LOSS` | `0.12` | Exit at -12% return |
| `SCAN_INTERVAL_ACTIVE_MINUTES` | `5` | Scan every 5 min during active hours |

---

## License

MIT — see [LICENSE](LICENSE)
