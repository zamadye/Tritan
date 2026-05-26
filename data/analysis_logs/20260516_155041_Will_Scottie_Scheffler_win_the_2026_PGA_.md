# Market Analysis — 2026-05-16 15:50 UTC

## Market
- **Question:** Will Scottie Scheffler win the 2026 PGA Championship?
- **Category:** sports
- **YES Price:** 20.0%
- **Days Left:** 1
- **Volume 24h:** $203,828
- **Liquidity:** $474,799

## Statistical Prior
- **p_base:** 11.1%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,201 (-1.2% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,064 (-1.5% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [MULTI-SOURCE NEWS] 1 sources for: scottie scheffler 2026 championship
- [Bing News]

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 11.1%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Tournament is IN PROGRESS (Round 2, May 15 2026). No specific information asymmetry identified - the 20% price likely already reflects Round 1 leaderboard position. Scheffler at 20% is ~2x his base rate (11%), but this premium is justified as the world's #1 golfer in an active major. This is NOT an obscure longshot (3-15% range) where crowd bias would apply - Scheffler is the consensus favorite. No breaking news, injury reports, or unusual performance data found that isn't already priced in. Only a statistical gap exists (-9% price vs base rate) with no identifiable catalyst today. Per rules: SKIP when only statistical gap with no specific catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Scottie Scheffler 2026 PGA Championship news'})` → [2026-05-15] 2026 PGA Championship Round 2 tee times & pairings — The 2026 PGA Tour season continues
- `search_web({'query': 'Scottie Scheffler PGA Championship 2026 standings score'})` → [2026-05-15] PGA Championship Leaderboard 2026: Golf Scores, Standings, Results From Each Round — Re
- `get_market_context({'keyword': 'PGA Championship golf'})` → No related markets found for 'PGA Championship golf'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*