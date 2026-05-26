# Market Analysis — 2026-05-21 21:29 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $142,856
- **Liquidity:** $118,432

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,697 (+0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,679 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: glory giza: oleksandr usyk rico
- [Bing News]
- [Thu, 21 May 2026] glory giza: oleksandr usyk rico
- → World Champion Oleksandr Usyk and GOAT of Kickboxing Rico Verhoeven make history as they face the pyramids for 'Glory in Giza.' ...
- [Thu, 21 May 2026] Oleksandr Usyk vs. Rico Verhoeven prediction, odds, pick for ‘Glory in Giza’ Boxing
- → Oleksandr Usyk and Rico Verhoeven took a long, long look at each other during the first faceoff for Saturday's crossover boxing match.
- [Thu, 21 May 2026] Video: Oleksandr Usyk vs. Rico Verhoeven press conference faceoff lingers
- → Oleksandr Usyk and Rico Verhoeven will battle it out in Egypt on Saturday night.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 92.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Usyk (undisputed boxing champion) is overwhelmingly favored vs kickboxer Verhoeven making boxing debut. Market at 93% vs 98% base rate gives only 5% gap - exactly at the decision gate threshold, not exceeding it. Two prior analyses on this identical market reached the same SKIP conclusion. No new catalyst or breaking information has emerged. While the crowd may be slightly underpricing Usyk, the edge is too thin and speculative to bet against the gate rule.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_odds({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_sports_data({'sport': 'nfl'})` → No injury data found for nfl 
- `search_web({'query': 'Oleksandr Usyk vs Rico Verhoeven Glory in Giza fight prediction odds 2025'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Predicti
- `search_web({'query': 'Usyk vs Verhoeven odds boxing match Glory 2026'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Rico Verhoeven Closes Chapter of Life Ahead of His
- `get_market_context({'keyword': 'Usyk Verhoeven Glory Giza'})` → No related markets found for 'Usyk Verhoeven Glory Giza'
- `search_web({'query': 'Oleksandr Usyk boxing record 2025 2026'})` → [Wed, 10 Dec 2025] Google News
[Thu, 22 Jan 2026] 2025 boxing top 100: Crawford, Inoue, Usyk lead ra
- `search_web({'query': '"Usyk vs Verhoeven" "May 23" fight odds prediction boxing'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Usyk vs Verhoeven Odds &amp; Picks - Pyramids of G
- `search_web({'query': 'Rico Verhoeven boxing debut record professional boxer'})` → [Tue, 19 May 2026] Google News
[Sun, 17 May 2026] Usyk vs Rico: Date, UK time, ringwalk, radio, unde

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*