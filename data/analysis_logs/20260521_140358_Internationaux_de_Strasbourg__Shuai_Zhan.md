# Market Analysis — 2026-05-21 14:03 UTC

## Market
- **Question:** Internationaux de Strasbourg: Shuai Zhang vs Emma Navarro
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $116,589
- **Liquidity:** $71,928

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,074 (-0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,984 (-0.1% 24h) → neutral
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
- **Confidence:** 48%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.30

### Reasoning
Stat signal indicates market overprices YES (57% price vs 44.7% historical resolution at this level), but multiple factors prevent action: (1) Entry zone 50-60% has historically poor WR of only 38% from 16 trades, (2) Gap is narrow (+3% market vs base rate), (3) No concrete injury/form info found via search - only generic tournament previews, (4) Previous similar Zhang/Navarro market was also skipped at 45% confidence. While crowd bias exists (market overprices YES), the combination of weak entry zone track record and absence of verifiable catalyst makes this below the 55% confidence threshold for action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_market_context({'keyword': 'Shuai Zhang Emma Navarro'})` → No related markets found for 'Shuai Zhang Emma Navarro'
- `search_web({'query': 'Internationaux de Strasbourg 2025 Shuai Zhang Emma Navarro match preview'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Internationaux de Strasbourg presented by Mammotio
- `search_web({'query': 'Emma Navarro Shuai Zhang 2026 WTA Strasbourg draw prediction'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] WTA Strasbourg Quarterfinal Predictions Including 
- `search_web({'query': 'Shuai Zhang form 2026 WTA results recent matches'})` → [Sat, 31 Jan 2026] Google News
[Wed, 22 Apr 2026] Reunited and it feels so good! Mertens and Zhang w
- `search_web({'query': 'Emma Navarro form 2026 WTA results recent matches clay court'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] The Official Home of the Women's Tennis Associatio
- `search_web({'query': '"Shuai Zhang" "Emma Navarro" Strasbourg 2026 quarterfinal'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] WTA Strasbourg Quarterfinal Predictions Including 
- `search_web({'query': 'Zhang vs Navarro Strasbourg 2026 preview prediction odds'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] WTA Strasbourg Quarterfinal Predictions Including 

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*