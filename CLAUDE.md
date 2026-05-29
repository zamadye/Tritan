# TRITAN — Claude Code Knowledge Base

## Project Overview
Polymarket autonomous trading bot. Python agent + Next.js dashboard. Runs on PRoot/Termux (Android).

## Current State (2026-05-29)
- **Branch:** `sandbox/fixes`
- **Mode:** LIVE with DRY_RUN=true
- **Blocker:** Telkomsel blocks `gamma-api.polymarket.com` (internetbaik redirect). Need VPN or VPS outside Indonesia.
- **SDK:** Migrated to `polymarket-client` (new) with fallback to `py-clob-client` (legacy). Both SDKs auto-detected.

## Architecture
```
agent/core.py       → Main loop: scan → analyze → size → execute
agent/scanner.py    → Fetch markets from Gamma API
agent/analyzer.py   → LLM probability estimation (Xiaomi MiMo)
agent/sizer.py      → Kelly Criterion position sizing
agent/executor.py   → Trade execution (demo/live)
agent/monitor.py    → Auto-exit: TP/SL/trailing stop
agent/resolver.py   → Resolve settled markets
agent/sync_live.py  → Sync CLOB trades to live_trades.json
agent/learner.py    → Log-based learning, evolution lessons
agent/bankroll.py   → Stepped compounding, streak tracking
agent/research.py   → Macro context, news aggregation
agent/osint.py      → Twitter OSINT, fear/greed index
agent/tools.py      → Agentic tool executor for LLM
agent/patterns.py   → Pattern library from resolved trades

web/                → Next.js dashboard (PM2 managed)
web/app/api/stats/  → Stats API (merges agent + sync trades)
web/app/api/account/→ Account API (balance + portfolio)
web/app/api/agent/  → Agent control (start/stop/switch mode)
```

## Key Environment Variables (.env)
```
AGENT_MODE=live          # demo or live
DRY_RUN=true             # true = simulated orders
POLYGON_PRIVATE_KEY=0x...
POLYGON_WALLET_ADDRESS=0x...
SIGNATURE_TYPE=0         # 0=EOA, 1=POLY_PROXY, 2=POLY_GNOSIS_SAFE
AI_API_KEY=...           # Xiaomi MiMo LLM key
AI_BASE_URL=...          # LLM endpoint
EXIT_TAKE_PROFIT=0.20
EXIT_STOP_LOSS=0.20
TRAILING_STOP_PCT=0.08
MIN_BET_SIZE=1.00
MAX_BET_SIZE=2.00
KELLY_FRACTION=0.50
LIVE_BANKROLL=26.67
```

## SDK Migration (Phase 0.2 — DONE)
All agent files support both new `polymarket-client` and legacy `py-clob-client`:
- **Detection:** `hasattr(client, "place_market_order")` → new SDK
- **core.py:** `_build_clob_client()` tries SecureClient first, falls back to ClobClient
- **executor.py:** `execute_trade()` branches on SDK type
- **monitor.py:** `_execute_sell_order()` branches on SDK type
- **sync_live.py:** `sync_live_trades()` handles Paginator vs dict
- **Doc:** `PYSDK_MIGRATION.md` has full API mapping

## Network Issue
Telkomsel (Indonesian ISP) intercepts HTTPS to `gamma-api.polymarket.com`:
```
HTTP/1.0 302 Moved Temporarily
Location: https://internetbaik.telkomsel.com/block?orig_url=https://gamma-api.polymarket.com
```
Even with SSL verification disabled, connection is intercepted. **Solution:** VPN or VPS outside Indonesia.

## Commands
```bash
# Run agent (demo)
AGENT_MODE=demo .venv/bin/python main.py run

# Run agent (live, dry run)
AGENT_MODE=live DRY_RUN=true .venv/bin/python main.py run

# Dashboard
pm2 start web/.next/standalone/server.js --name tritan-dashboard

# Git push (needs token)
git remote set-url origin https://zamadye:<TOKEN>@github.com/zamadye/Tritan.git
git push origin sandbox/fixes
git remote set-url origin https://github.com/zamadye/Tritan.git  # clean token
```

## Upgrade Roadmap (from ROADMAP.md)
- **Phase 0:** Infrastructure fix (VPN) + SDK migration ✅
- **Phase 1:** Wang Transform pricing (oracle3)
- **Phase 2:** Multi-model ensemble (4 LLMs)
- **Phase 3:** Arbitrage (8 strategies) + hedge discovery
- **Phase 4:** Whale signal + resolution sniper
- **Phase 5:** WebSocket + chat interface

## Rules
1. Never break working code — test before changing
2. Use `.env` for all config, never hardcode
3. All agent files must work with both old and new SDK
4. Demo mode must work without network (Gamma API)
5. Indonesian user — communicate in Indonesian
