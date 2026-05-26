# Market Analysis — 2026-05-17 09:32 UTC

## Market
- **Question:** Internationaux de Strasbourg, Qualification: Yulia Putintseva vs Oleksandra Oliynykova
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 6
- **Volume 24h:** $69,212
- **Liquidity:** $58,309

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,103 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,102 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- Will the Fed decrease interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg qualification: yulia putintseva
- [Bing News]
- [Sun, 22 Jun 2025] internationaux strasbourg qualification: yulia putintseva
- → Kazakhstan's Yulia Putintseva has found herself in hot water once again after a confrontation with Greece's Maria Sakkari following the pair's meeti
- [] Yulia Putintseva extends lengthy tennis rap sheet with fiery post-match exchange with Maria Sakkari
- [Metaculus]
- [] Will Bitcoin trade above $120,000 before August 1, 2026?
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 54.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.15

### Reasoning
No specific information asymmetry detected for this qualification match. Market price (53%) is essentially at statistical base rate (54%), with only +1% gap — below the 3% threshold required for statistical edge qualification. While the historical stat signal suggests markets at 53% resolve YES only 44.7% (n=13,967), this is a general pattern across all market categories, not specific evidence for this tennis match. No breaking news, injury reports, or unreported data found for either player. Oliynykova is a lower-ranked player (AO 2026 debut) but no current form differential identified to create genuine information asymmetry. Previous decision on identical market was SKIP (gate=FAIL). Without a specific catalyst today, the small price gap does not justify action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<3%

## Tool Calls
- `search_web({'query': 'Yulia Putintseva vs Oleksandra Oliynykova Strasbourg 2025 qualification'})` → [Sat, 22 Oct 2016] Google News
[Sun, 17 May 2026] Yulia Putintseva Stats, News, Pictures, Bio, Video
- `get_market_context({'keyword': 'Putintseva Strasbourg'})` → No related markets found for 'Putintseva Strasbourg'
- `search_web({'query': 'Oleksandra Oliynykova 2025 2026 tennis results form'})` → [Sun, 17 May 2026] Google News
[Sat, 17 Jan 2026] WTA Strasbourg Day 1 Predictions Including Sara Be
- `get_sports_data({'sport': 'nba'})` → INJURY [atlanta hawks] Keshon Gilbert (G): Out
INJURY [atlanta hawks] Jock Landale (C): Out
INJURY [
- `search_web({'query': 'Putintseva Oliynykova Strasbourg 2026 tennis odds prediction'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] H2H, prediction of Oleksandra Oliynykova vs Yulia 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*