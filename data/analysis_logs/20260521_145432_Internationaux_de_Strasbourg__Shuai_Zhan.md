# Market Analysis — 2026-05-21 14:54 UTC

## Market
- **Question:** Internationaux de Strasbourg: Shuai Zhang vs Emma Navarro
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 6
- **Volume 24h:** $228,652
- **Liquidity:** $36,931

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,836 (-0.8% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,028 (-0.5% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Major AI model release → benchmark competition → sector excitement
- → AI regulation proposed → uncertainty → AI stocks fall short-term
- → AI chip shortage → NVIDIA revenue beats → AI infrastructure stocks rally
- → AI energy demand → data center power stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: shuai zhang emma
- [Bing News]
- [Wed, 20 May 2026] internationaux strasbourg: shuai zhang emma
- → Emma Navarro seeks to rediscover form vs rising American Iva Jovic. Get draw, schedule, entry list, prize money and expert predictions.
- [Wed, 20 May 2026] Internationaux de Strasbourg Day Four Round-up | Emma Navarro rallies to defeat Iva Jovic and advance to quarterfinals
- → None ...
- [Fri, 15 May 2026] WTA Internationaux de Strasbourg Results
- → The Internationaux de Strasbourg takes place between 17-23 May in a WTA 500 tournament prior to the French Open. Elena Rybakina is defending champio

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 43.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal: markets at 51% YES historically resolve YES only 44.7% of time (n=13,967), indicating YES is overpriced by ~6.3%. Past decisions on this exact market with 1% gaps correctly identified FAIL, but the historical stat edge now provides a concrete quantitative basis for a NO bet. No specific sports information gathered to contradict the statistical pattern. Entry at 50-60% historically has weak WR (38%), further supporting fading the YES side.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Zhang'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Shuai Zhang vs Emma Navarro Internationaux de Strasbourg 2025 head to head'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] Internationaux de Strasbourg presented by Mammotio
- `search_web({'query': 'Emma Navarro vs Shuai Zhang odds prediction Strasbourg 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] WTA Strasbourg Best Bets Including Emma Navarro vs
- `search_web({'query': '"Shuai Zhang" "Emma Navarro" Strasbourg quarterfinal'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Internationaux de Strasbourg presented by Mammotio
- `search_web({'query': 'Zhang Shuai Emma Navarro head to head statistics 2026'})` → [Wed, 20 May 2026] Google News
[Thu, 26 Feb 2026] Zhang Shuai - Emma Navarro Stats: Tennis Scores &a
- `get_market_context({'keyword': 'Strasbourg Zhang Navarro'})` → No related markets found for 'Strasbourg Zhang Navarro'
- `get_market_context({'keyword': 'WTA Strasbourg'})` → No related markets found for 'WTA Strasbourg'

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*