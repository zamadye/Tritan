# TRITAN Configuration Reference

All configuration is via `.env` file. Copy `.env.example` to `.env` and fill in values.

---

## Required — Polymarket Credentials

| Variable | Description |
|----------|-------------|
| `POLYGON_PRIVATE_KEY` | Your wallet private key (0x...) |
| `POLYGON_WALLET_ADDRESS` | Your SAFE wallet address |
| `POLY_API_KEY` | Polymarket API key |
| `POLY_API_SECRET` | Polymarket API secret |
| `POLY_API_PASSPHRASE` | Polymarket API passphrase |
| `SIGNATURE_TYPE` | Set to `3` for SAFE wallets (POLY_1271) |

---

## Agent Mode

| Variable | Default | Description |
|----------|---------|-------------|
| `AGENT_MODE` | `live` | `live` or `demo` |
| `DRY_RUN` | `false` | `true` = analyze but don't execute orders |

---

## Scanning

| Variable | Default | Description |
|----------|---------|-------------|
| `MIN_VOLUME_24H` | `2000` | Minimum 24h volume ($) to consider a market |
| `MIN_LIQUIDITY` | `500` | Minimum liquidity ($) |
| `MIN_MARKET_PRICE` | `0.03` | Minimum YES price (3¢) |
| `MAX_MARKET_PRICE` | `0.97` | Maximum YES price (97¢) |
| `MIN_DAYS_TO_RESOLVE` | `1` | Minimum days until market resolves |
| `MAX_DAYS_TO_RESOLVE` | `30` | Maximum days until market resolves |
| `MAX_MARKETS_TO_SCAN` | `200` | Max markets per scan cycle |
| `SCAN_INTERVAL_ACTIVE_MINUTES` | `3` | Scan interval (minutes) |
| `PREFERRED_CATEGORIES` | `sports,geopolitik,other` | Priority categories |

---

## Statistical Gate

| Variable | Default | Description |
|----------|---------|-------------|
| `MIN_STAT_EDGE` | `0.05` | Min gap between base rate and market price |
| `MIN_STAT_EDGE_SPORTS` | `0.03` | Sports-specific threshold (lower = more bets) |
| `MIN_STAT_EDGE_HIGH_RISK` | `0.05` | Crypto/geo/politics threshold |

---

## LLM Analysis

| Variable | Default | Description |
|----------|---------|-------------|
| `MIN_CONFIDENCE` | `0.52` | Minimum LLM confidence to bet |
| `LLM_TIMEOUT_SECONDS` | `35` | Per-call LLM timeout |
| `LLM_DAILY_COST_LIMIT_USD` | `3.0` | Max daily LLM spend |

---

## Position Sizing

| Variable | Default | Description |
|----------|---------|-------------|
| `MIN_BET_SIZE` | `1.00` | Minimum bet size ($) |
| `MAX_BET_SIZE` | `3.00` | Maximum bet size ($) |
| `MAX_OPEN_POSITIONS` | `10` | Max simultaneous open positions |
| `MAX_OPEN_PER_CATEGORY` | `3` | Max positions per category |

---

## Exit Management

| Variable | Default | Description |
|----------|---------|-------------|
| `EXIT_TAKE_PROFIT` | `0.20` | Hard TP at +20% P&L |
| `EXIT_STOP_LOSS` | `0.20` | SL at -20% P&L (non-sports only) |
| `TRAILING_STOP_PCT` | `0.08` | Trailing stop: 8% from peak |
| `EXIT_MAX_HOURS` | `24` | Max hold time for long-dated markets |

---

## Data APIs

| Variable | Description |
|----------|-------------|
| `ODDS_API_KEY` | The Odds API key (sports bookmaker odds) |
| `METACULUS_API_KEY` | Metaculus API token (community predictions) |
| `CRYPTOQUANT_API_KEY` | CryptoQuant API key (crypto on-chain data) |
| `NEWS_API_KEY` | NewsAPI key (fallback news source) |
| `GNEWS_API_KEY` | GNews API key (fallback news source) |

---

## Fine-Tuning

| Variable | Default | Description |
|----------|---------|-------------|
| `EVAL_INTERVAL_TRADES` | `30` | Run fine-tune evaluation every N trades |
| `ENABLE_EVENT_SCANNER` | `false` | Enable multi-outcome event scanner |
