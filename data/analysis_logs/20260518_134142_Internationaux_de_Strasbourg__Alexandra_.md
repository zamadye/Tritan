# Market Analysis — 2026-05-18 13:41 UTC

## Market
- **Question:** Internationaux de Strasbourg: Alexandra Eala vs Oleksandra Oliynykova
- **Category:** sports
- **YES Price:** 72.0%
- **Days Left:** 6
- **Volume 24h:** $287,426
- **Liquidity:** $64,797

## Statistical Prior
- **p_base:** 80.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,121 (-1.5% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,943 (-1.7% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: alexandra eala oleksandra
- [Bing News]
- [Sun, 17 May 2026] internationaux strasbourg: alexandra eala oleksandra
- → ALEX Eala drew Ukraine’s Oleksandra Oliynykova in the opening round of the WTA 500 Internationaux de Strasbourg - her fifth tournament of the clay s
- [Sun, 17 May 2026] Eala draws world No. 68 Oliynykova in final French Open tuneup
- → Filipina tennis star Alex Eala will play Ukraine's Oleksandra Oliynykova in the first round of the Internationaux de Strasbourg, a WTA 500 tournamen
- [Sun, 17 May 2026] Tennis: Alex Eala to play Ukraine's Oliynykova in first round of Strasbourg Open
- → MANILA, Philippines — Alex Eala begins her campaign at the Internationaux de Strasbourg with a first-round clash against Ukrainian qualifier Oleksan

## LLM Decision
- **Action:** YES
- **Confidence:** 58%
- **p_true:** 86.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MISPRICING
- **Catalyst Strength:** 0.65

### Reasoning
Market underprices Eala's win probability by 8 percentage points (72% vs 80% base rate from n=6,077). Eala is ranked WTA #38 and coming off strong Italian Open run, facing lower-ranked Oliynykova (Top 100). No injury concerns found for either player. The 8% gap exceeds the 5% threshold for statistical edge, but confidence is moderate due to lack of breaking news or direct catalyst - this is primarily a base rate/statistical value bet.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `get_market_context({'keyword': 'Alexandra Eala'})` → No related markets found for 'Alexandra Eala'
- `search_web({'query': 'Alexandra Eala vs Oleksandra Oliynykova Strasbourg 2025'})` → [Thu, 19 Mar 2026] Google News
[Fri, 20 Mar 2026] Alex Eala’s 2025 Miami Open run: A Recap - GMA Net
- `search_web({'query': 'Oleksandra Oliynykova tennis 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 19 Jan 2026] Fresh off an incredible run at the Italian Open, F
- `search_web({'query': 'Eala Strasbourg Open 2025 Oliynykova'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Fresh off an incredible run at the Italian Open, F
- `search_web({'query': 'Alex Eala ranking 2026 form recent results'})` → [Fri, 13 Mar 2026] Google News
[Thu, 19 Mar 2026] Alex Eala faces potential ranking drop at the Miam
- `search_web({'query': 'Alex Eala injury news May 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 10 May 2026] Mother dead, 2 children injured in Rodriguez, Riza
- `search_web({'query': 'Oleksandra Oliynykova ranking 2026 recent results'})` → [Thu, 05 Feb 2026] Google News
[Sat, 17 Jan 2026] Oliynykova saves 21 break points in Cluj-Napoca; t

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*