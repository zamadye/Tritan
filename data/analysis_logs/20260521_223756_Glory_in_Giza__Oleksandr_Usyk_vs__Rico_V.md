# Market Analysis — 2026-05-21 22:37 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $143,387
- **Liquidity:** $121,560

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,633 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,592 (+0.3% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: glory giza: oleksandr usyk rico
- [Bing News]
- [Thu, 21 May 2026] glory giza: oleksandr usyk rico
- → World Champion Oleksandr Usyk and GOAT of Kickboxing Rico Verhoeven make history as they face the pyramids for 'Glory in Giza.' ...
- [Thu, 21 May 2026] Oleksandr Usyk vs. Rico Verhoeven prediction, odds, pick for ‘Glory in Giza’ Boxing
- → Oleksandr Usyk and Rico Verhoeven will battle it out in Egypt on Saturday night.
- [Thu, 21 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Prediction
- → Oleksandr Usyk (24-0, 15 KOs) will defend his World Boxing Council (WBC) heavyweight title against former GLORY kickboxing champion Rico Verhoeven (

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 92.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Market at 93% YES (Usyk wins) vs base rate 98% for similar mismatches. The +5% gap suggests crowd gives Verhoeven ~7% chance vs historical 2% for similar underdogs. However, Verhoeven is NOT a typical crossover - he's a world-class kickboxing champion who trained with Peter Fury (Tyson Fury's camp) and experts like Eddie Hearn call him 'live in this fight.' WBA approved title defense. The base rate may overstate Usyk's edge here. No breaking news or injury reports shift the calculus. Previous decisions correctly identified no stat edge (gap=5% equals but doesn't exceed gate). True probability likely ~91-93%, making market fairly priced with no actionable edge either direction.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_odds({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_sports_data({'sport': 'nba', 'team': 'Usyk'})` → No injury data found for nba Usyk
- `search_web({'query': 'Oleksandr Usyk vs Rico Verhoeven boxing match odds 2025'})` → [Thu, 21 May 2026] Google News
[Sun, 17 May 2026] Tyson Fury vs Arslanbek Makhmudov odds, picks, bes
- `search_web({'query': 'Usyk Verhoeven Glory in Giza fight news June 2025'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Rico Verhoeven Closes Chapter of Life Ahead of His
- `search_web({'query': 'Usyk vs Rico Verhoeven boxing May 2026 prediction who will win'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Usyk vs Rico prediction: Who will win and how - Ba
- `get_market_context({'keyword': 'Usyk Verhoeven boxing Glory Giza'})` → No related markets found for 'Usyk Verhoeven boxing Glory Giza'
- `search_web({'query': '"Usyk vs Verhoeven" odds betting lines boxing 2026'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Usyk vs Verhoeven Odds &amp; Picks - Pyramids of G
- `search_web({'query': 'Rico Verhoeven boxing debut kickboxer transition record'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] The inside story of Rico Verhoeven's boxing rise i
- `search_web({'query': 'Usyk vs Verhoeven prediction Bad Left Hook May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Usyk vs Rico prediction: Who will win and how - Ba
- `search_web({'query': 'Rico Verhoeven boxing training Tyson Fury camp 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Usyk vs Verhoeven: Not the Crossover You Think - M
- `search_web({'query': 'Usyk vs Verhoeven betting odds sportsbook consensus May 22 2026'})` → No search results for: Usyk vs Verhoeven betting odds sportsbook consensus May 22 2026
- `search_web({'query': 'Odds Shark Usyk Verhoeven odds picks pyramids giza'})` → [Tue, 19 May 2026] Google News
[Thu, 21 May 2026] Usyk vs Verhoeven Odds &amp; Picks - Pyramids of G
- `search_web({'query': 'Usyk Verhoeven fight week news weigh-in injury update May 2026'})` → [Thu, 21 May 2026] Google News
[Fri, 15 May 2026] Usyk Downplays Size Gap as Verhoeven Talks Power i

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*