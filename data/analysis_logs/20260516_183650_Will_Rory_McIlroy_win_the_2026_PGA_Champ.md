# Market Analysis — 2026-05-16 18:36 UTC

## Market
- **Question:** Will Rory McIlroy win the 2026 PGA Championship?
- **Category:** sports
- **YES Price:** 13.8%
- **Days Left:** 1
- **Volume 24h:** $97,617
- **Liquidity:** $18,509

## Statistical Prior
- **p_base:** 6.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,163 (-1.2% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,117 (-1.4% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [MULTI-SOURCE NEWS] 1 sources for: rory mcilroy 2026 championship
- [Bing News]

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 5.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** CROWD_BIAS
- **Catalyst Strength:** 0.65

### Reasoning
Multi-outcome market (150+ golfer field) where McIlroy at 14% is overpriced due to brand recognition. Search results show Scheffler leading, not McIlroy. No specific evidence McIlroy is in contention. Retail bettors systematically overprice popular golfers in tournament markets. Base rate is 6%, and 14% requires clear evidence of strong form which is absent.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `get_sports_data({'sport': 'nba', 'team': 'McIlroy'})` → No injury data found for nba McIlroy
- `search_web({'query': 'Rory McIlroy 2024 2025 performance wins injuries'})` → [Wed, 08 Apr 2026] Google News
[Wed, 08 Apr 2026] Masters: Why is no one talking about Rory McIlroy 
- `search_web({'query': 'Rory McIlroy recent tournament results 2026'})` → [Fri, 15 May 2026] Google News
[Wed, 13 May 2026] Round 1 notebook: Scottie Scheffler among leaders 

## Outcome
**✅ WIN** | P&L: $+0.16 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*