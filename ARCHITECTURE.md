# TRITAN — Architecture Documentation

## Overview

TRITAN is a prediction market automation framework built on three independent
layers of edge detection. Each layer can be understood, audited, and extended
independently.

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1: STATISTICAL EDGE                                      │
│  Logistic regression calibration vs 19,624 resolved markets    │
│  → p_calibrated per category                                    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 2: INFORMATION EDGE                                      │
│  Agentic LLM loop — autonomous data verification per market    │
│  → information_gap detected or not                              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 3: EXECUTION + AUDIT                                     │
│  Kelly sizing, exit management, full trade log                  │
│  → every decision traceable to data source                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Full Data Flow

```
main.py run
    │
    ▼
core.run()
    │
    ├── print_banner()          # Display stats + bankroll
    │
    └── loop every N minutes:
            │
            ▼
        run_scan_cycle()
            │
            ├── resolver.check_and_resolve()     # Settle expired markets
            ├── monitor.check_and_exit()         # TP / SL / trailing / deadline
            │
            ├── scanner.get_candidate_markets()  # Fetch from Gamma API
            │       └── Filter: volume, liquidity, price range, days left
            │       └── Flag: bet_no_signal (50-60% range, historically overpriced)
            │
            ├── research.get_macro_context()     # BTC price, Fear&Greed (once/cycle)
            │
            └── for each market:
                    │
                    ├── [GATE 0] Skip if already open position
                    ├── [GATE 0] Skip if price < 6% or > 94%
                    │
                    ├── analyzer.estimate_probability()
                    │       │
                    │       ├── get_statistical_prior()     # Layer 1
                    │       │       └── calibration_model.json (logistic regression)
                    │       │       └── statistical_prior.json (bucket fallback)
                    │       │
                    │       ├── osint.get_osint_signals()   # Category signals
                    │       ├── research.build_research_report()
                    │       ├── info_edge.detect_info_edge()
                    │       │
                    │       └── llm.chat_with_tools()       # Layer 2
                    │               └── Tool loop (max 3 iter, 45s timeout):
                    │                   ├── search_web()       → Tavily/NewsAPI
                    │                   ├── get_crypto_price() → CoinGecko
                    │                   ├── get_sports_data()  → ESPN
                    │                   └── get_market_context() → Gamma API
                    │
                    ├── [GATE 1] stat_edge = |p_base - market_price| ≥ threshold
                    │           threshold = 8% (standard) / 10% (high-risk categories)
                    │
                    ├── [GATE 2] confidence ≥ per-category minimum
                    │
                    ├── sizer.calculate_position()          # Kelly fraction
                    │
                    └── executor.execute_trade()            # Layer 3
                            └── Append to demo_trades.json with full audit fields
```

---

## Module Reference

### `agent/core.py` — Main Orchestrator
Entry point for the scan loop. Manages cycle timing, bankroll checks,
correlation controls, and coordinates all other modules.

Key functions:
- `run(mode)` — starts the infinite loop
- `run_scan_cycle(mode)` — one full cycle: resolve → exit → scan → analyze → bet
- `_get_bankroll(mode)` — reads live USDC balance (live) or calculates from trades (demo)
- `_open_market_ids(mode)` — returns set of market questions with open positions

### `agent/scanner.py` — Market Discovery
Fetches active markets from Polymarket Gamma API and applies filters.

Filters applied:
- `MIN_VOLUME_24H` — minimum 24h trading volume
- `MIN_LIQUIDITY` — minimum order book depth
- `MIN/MAX_MARKET_PRICE` — skip extreme prices (< 6% or > 94%)
- `MIN/MAX_DAYS_TO_RESOLVE` — time window filter
- `BLACKLISTED_CATEGORIES` — skip categories with no edge

Statistical signal: markets in 50-60% YES price range are flagged as
`bet_no_signal=True` based on historical data showing actual YES resolution
rate of 44.7% in this range (n=13,967 markets).

### `agent/analyzer.py` — Edge Detection Engine
Two-layer probability estimation:

**Layer 1 — Statistical Prior:**
Logistic regression model trained on 19,624 resolved Polymarket markets.
Per-category calibration. Brier score improvement over naive baseline:
- `other`: 7.6% improvement (n=7,829)
- `geopolitik`: 17.9% improvement (n=135)
- `sports`: 0.1% improvement (n=6,077) — near-efficient market
- `crypto`: 1.5% improvement (n=4,092)

**Layer 2 — Agentic LLM Verification:**
LLM receives market context and autonomously calls tools to verify data.
Task: detect if there is NEW information not yet reflected in market price.
Output: `information_gap: true/false` + `gap_reason` + `confidence`.

### `agent/tools.py` — Agentic Tool Executors
Four tools available to LLM during analysis:

| Tool | Source | Use Case |
|------|--------|----------|
| `search_web(query)` | Tavily → NewsAPI fallback | Breaking news, geopolitik |
| `get_crypto_price(coin)` | CoinGecko (free) | BTC/ETH price lag detection |
| `get_sports_data(sport, team)` | ESPN API (free) | Injury reports, standings |
| `get_market_context(keyword)` | Gamma API | Related market prices |

### `agent/llm.py` — LLM Client
OpenAI-compatible client. Tested with MiMo v2.5 via Z.ai endpoint.

Key detail: MiMo is a reasoning model — response may be in `reasoning_content`
field rather than `content`. Both fields are checked.

Two modes:
- `chat(prompt)` — single call, no tools
- `chat_with_tools(prompt, tools)` — agentic loop, max 5 iterations, 45s timeout

Cost control: `LLM_DAILY_COST_LIMIT_USD` hard stops all LLM calls when reached.

### `agent/monitor.py` — Exit Management
Checks all open positions every cycle. Exit conditions (in priority order):

```
1. TAKE_PROFIT    → P&L ≥ +15% (EXIT_TAKE_PROFIT)
2. PARTIAL_EXIT   → P&L ≥ +20% → exit 50% of position
3. TRAILING_STOP  → P&L drops 5% below peak (TRAILING_STOP_PCT)
4. STOP_LOSS      → P&L ≤ -12% (EXIT_STOP_LOSS)
5. EVENT_DEADLINE → held longer than category time limit:
                    sports=4h, crypto=6h, geopolitik=24h, default=8h
```

P&L calculation is correct for both YES and NO bets using share-based math.

### `agent/executor.py` — Trade Execution
Demo mode: simulates execution, appends to `demo_trades.json`.
Live mode: submits order via Polymarket CLOB API using `py-clob-client`.

Every trade record includes full audit fields:
`trade_id`, `timestamp`, `market_question`, `category`, `side`,
`price_at_entry`, `size_usd`, `p_base`, `p_base_source`, `p_base_n`,
`tool_calls_log`, `information_gap`, `information_gap_reason`,
`confidence_at_bet`, `edge_at_bet`, `brier_score`.

### `agent/resolver.py` — Outcome Resolution
Checks open trades against Polymarket's resolved market list.
Calculates P&L, Brier score, and triggers evolution lesson generation.

### `agent/sizer.py` — Kelly Position Sizing
Implements fractional Kelly criterion:

```
kelly_fraction = (p_true - p_market) / (1 - p_market)  [for YES bets]
position_size  = bankroll × kelly_fraction × KELLY_FRACTION
position_size  = min(position_size, MAX_BET_SIZE)
position_size  = max(position_size, MIN_BET_SIZE)
```

### `agent/learner.py` — Performance Tracking
Tracks WR, Brier score, P&L per category. Generates `evolution_lessons.json`
— a summary of what the system has learned from past trades, injected into
LLM context for future analysis.

### `agent/bankroll.py` — Stepped Compounding
Adjusts Kelly multiplier based on win/loss streaks:
- After `WIN_STREAK_TO_INCREASE` consecutive wins → level up (larger bets)
- After `LOSS_STREAK_TO_DECREASE` consecutive losses → level down (smaller bets)

### `agent/research.py` — Macro Context
Fetches shared context once per cycle (not per market):
- BTC price + 24h change (CoinGecko)
- Fear & Greed index (alternative.me)
- Fed/FOMC market prices (Gamma API)
- Causal chain templates for geopolitical events

### `agent/osint.py` — Category Signal Aggregator
Fetches category-specific signals before LLM analysis:
- Sports: ESPN injuries + Vegas odds (Odds API)
- Crypto: CoinGecko price movement + Fear & Greed trend
- Geopolitik: OpenSky aircraft activity, vessel tracking
- General: NewsAPI + Reddit sentiment (when accessible)

---

## Data Schema

### `data/statistical_prior.json`
```json
{
  "total_markets": 19624,
  "categories": {
    "sports": {
      "50-60%": { "n": 5396, "yes_rate": 0.488 }
    }
  },
  "overall": {
    "50-60%": { "n": 13967, "yes_rate": 0.447 }
  },
  "entry_price_prior": { ... }
}
```

### `data/calibration_model.json`
```json
{
  "sports": {
    "n": 6077,
    "a": 1.02, "b": -0.01,
    "brier": 0.2175, "naive_brier": 0.2176,
    "improvement": 0.1
  }
}
```

### `data/demo_trades.json` — Trade Audit Trail
Each trade record (key fields):
```json
{
  "trade_id": "uuid",
  "timestamp": "ISO8601",
  "market_question": "Will X happen?",
  "category": "sports",
  "side": "NO",
  "price_at_entry": 0.58,
  "size_usd": 3.00,
  "p_base": 0.43,
  "p_base_source": "logistic:sports",
  "p_base_n": 6077,
  "tool_calls_log": [
    {"tool": "get_sports_data", "args": {...}, "result": "..."}
  ],
  "information_gap": false,
  "information_gap_reason": "",
  "confidence_at_bet": 0.65,
  "edge_at_bet": -0.15,
  "actual_outcome": "NO",
  "pnl": 2.41,
  "brier_score": 0.068,
  "exit_reason": "TAKE_PROFIT (+80%)"
}
```

---

## Configuration Reference

All behavior is controlled via `.env`. No code changes needed for tuning.

| Variable | Default | Effect |
|---|---|---|
| `AGENT_MODE` | `demo` | `demo` simulates, `live` executes real orders |
| `MIN_STAT_EDGE` | `0.08` | Minimum \|p_base - market_price\| to analyze |
| `MIN_STAT_EDGE_HIGH_RISK` | `0.10` | Higher bar for crypto/geopolitik/politics |
| `MIN_CONFIDENCE` | `0.55` | LLM confidence gate (global) |
| `MIN_CONFIDENCE_CRYPTO` | `0.60` | Per-category override |
| `EXIT_TAKE_PROFIT` | `0.15` | Exit at +15% P&L |
| `EXIT_STOP_LOSS` | `0.12` | Exit at -12% P&L |
| `TRAILING_STOP_PCT` | `0.05` | Trail 5% below peak |
| `KELLY_FRACTION` | `0.25` | Quarter Kelly (conservative) |
| `LLM_DAILY_COST_LIMIT_USD` | `2.0` | Hard stop on LLM spend |

---

## Extension Points

### Adding a New Category
1. Add keywords to `_infer_category()` in `agent/learner.py`
2. Add category-specific signals in `agent/osint.py`
3. Add `MIN_CONFIDENCE_<CATEGORY>` to `.env`
4. Run `agent/build_prior.py` to update calibration model with new data

### Switching LLM Provider
`agent/llm.py` uses OpenAI-compatible client. Change three `.env` vars:
```
AI_API_KEY=your_key
AI_BASE_URL=https://api.openai.com/v1
AI_MODEL=gpt-4o-mini
```
Note: if provider uses reasoning model (like MiMo), ensure `reasoning_content`
fallback is handled — see `chat_with_tools()` in `llm.py`.

### Adding Kalshi Cross-Platform Arbitrage
See `agent/arbitrage.py` for the existing arbitrage detection scaffold.
Kalshi REST API is compatible with the existing scanner pattern.
Key addition needed: `agent/kalshi.py` scanner + cross-market price comparator.

### Deploying to Production
```bash
# Copy systemd service files (already created)
cp tritan-agent.service /etc/systemd/system/
cp polymarket-web.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable tritan-agent polymarket-web
systemctl start tritan-agent polymarket-web
```

---

## Web Dashboard

Next.js 16 dashboard at `web/`. Provides:
- Real-time equity curve and P&L
- WR per category with Brier score vs baseline
- Open positions with entry price and current P&L
- Full trade log with audit trail
- Agent control (start/stop/scan)
- Settings editor (live `.env` updates)

API routes: `/api/stats`, `/api/agent`, `/api/settings`, `/api/account`

Access: SSH tunnel recommended for private deployment.
```bash
ssh -L 3001:localhost:3001 user@server -N
# then open http://localhost:3001
```
