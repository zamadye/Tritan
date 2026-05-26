# Market Analysis — 2026-05-21 19:10 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $63,674
- **Liquidity:** $181,042

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,374 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,374 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: glory giza: oleksandr usyk rico
- [Bing News]
- [Thu, 21 May 2026] glory giza: oleksandr usyk rico
- → Oleksandr Usyk and Rico Verhoeven will battle it out in Egypt on Saturday night.
- [Thu, 21 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Prediction
- → Oleksandr Usyk (24-0, 15 KOs) will defend his World Boxing Council (WBC) heavyweight title against former GLORY kickboxing champion Rico Verhoeven (
- [Tue, 19 May 2026] Watch Usyk vs. Rico final press conference video, LIVE stream updates!
- → Not since the days of Napoleon have the Pyramids seen a fight like this. On Saturday, unified heavyweight champion Oleksandr Usyk puts his WBC title

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 92.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** CONFIRMATION
- **Catalyst Strength:** 0.70

### Reasoning
Fight confirmed by multiple independent sources (BBC, ESPN, Sky Sports, etc.) with no cancellation/injury reports. Only 2 days left. Historical base rate of 98% vs market price of 93% suggests ~4% edge. Usyk actively promoting event. Fear sentiment may be causing underpricing.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk'})` → No injury data found for mma_mixed_martial_arts Usyk
- `get_odds({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Oleksandr Usyk Rico Verhoeven Glory in Giza fight date 2025'})` → [Sun, 17 May 2026] Google News
[Thu, 21 May 2026] How to Watch Oleksandr Usyk vs Rico Verhoeven: Dat
- `search_web({'query': 'Usyk Verhoeven boxing match news June 2025'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Rico Verhoeven Closes Chapter of Life Ahead of His
- `get_market_context({'keyword': 'Usyk Verhoeven'})` → No related markets found for 'Usyk Verhoeven'
- `search_web({'query': 'Usyk Verhoeven fight confirmed Giza Egypt 2025'})` → [Sun, 17 May 2026] Google News
[Tue, 19 May 2026] Usyk vs Rico and more: Boxing schedule and preview
- `search_web({'query': 'Usyk Verhoeven fight cancellation news'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] 'Not a fake fight' - Usyk on Verhoeven &amp; helpi
- `get_market_context({'keyword': 'boxing Giza'})` → No related markets found for 'boxing Giza'
- `search_web({'query': '"Usyk" "Verhoeven" weigh-in Giza May 2026'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Usyk vs Rico: Date, UK time, ringwalk, radio, unde
- `search_web({'query': 'Oleksandr Usyk injury status May 2026'})` → [Sun, 17 May 2026] Google News
[Wed, 20 May 2026] Jake Paul targets late-2026 return but admits boxi
- `get_market_context({'keyword': 'boxing fight happen'})` → No related markets found for 'boxing fight happen'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*