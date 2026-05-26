# Market Analysis — 2026-05-21 12:56 UTC

## Market
- **Question:** Internationaux de Strasbourg: Jaqueline Cristian vs Daria Kasatkina
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 6
- **Volume 24h:** $343,377
- **Liquidity:** $58,603

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,213 (-0.4% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,213 (-0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: jaqueline cristian daria
- [Bing News]
- [Tue, 13 Jan 2026] internationaux strasbourg: jaqueline cristian daria
- → The quarterfinal of the Internationaux de Strasbourg pits Jaqueline Cristian, world No. 33, against Daria Kasatkina, world No. 62 and a qualifier. D
- [Fri, 15 May 2026] Cristian vs Kasatkina • 1/4 final • Strasbourg 2026
- → The Internationaux de Strasbourg takes place between 17-23 May in a WTA 500 tournament prior to the French Open. Elena Rybakina is defending champio
- [Wed, 01 Apr 2026] Internationaux de Strasbourg 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- → Emma Raducanu continued her impressive form on clay by surging past former world No 8 Daria Kasatkina at the Internationaux de Strasbourg. Raducanu,

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 56.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.50

### Reasoning
Strong statistical edge: Markets at 54% historically resolve YES only 44.7% of the time (n=13,967), indicating systematic overpricing of YES by ~9.3 percentage points. This creates a clear ~9 cent edge on NO at current 54% price. Additional negative signals: (1) Entry 50-60% range shows only 38% win rate from 16 trades, (2) No injury or form news found for either player via search, (3) Could not verify any catalyst supporting YES. Base rate comparison is ambiguous (56% base vs 54% market) but historical resolution data is the dominant signal. SPORTS category has strong 74% WR overall, but this specific price point underperforms. SKIP gate consideration: stat edge gap is ~9.3% which exceeds 5% threshold, justifying action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `search_web({'query': 'Jaqueline Cristian vs Daria Kasatkina Internationaux de Strasbourg 2025'})` → [Wed, 07 May 2025] Google News
[Thu, 21 May 2026] Internationaux de Strasbourg 2025 Scores | Latest 
- `search_web({'query': 'Daria Kasatkina injury 2025 form recent matches'})` → [Thu, 05 Mar 2026] Google News
[Mon, 22 Sep 2025] Surging Sebi...Korda One Of Those To Watch On Thur
- `search_web({'query': 'Jaqueline Cristian tennis 2025 results form'})` → [Fri, 17 Oct 2025] Google News
[Mon, 23 Mar 2026] Osaka withdraws from Japan Open with left thigh in
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Strasbourg tennis Kasatkina'})` → No related markets found for 'Strasbourg tennis Kasatkina'
- `search_web({'query': '"Internationaux de Strasbourg" 2025 draw Kasatkina Cristian'})` → [Wed, 20 May 2026] Google News
[Wed, 14 Jan 2026] Cristian vs. Kasatkina | Quarterfinals Internation
- `search_web({'query': 'Internationaux de Strasbourg 2025 tennis tournament results'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] The Official Home of the Women's Tennis Associatio

## Outcome
**✅ WIN** | P&L: $+0.49 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*