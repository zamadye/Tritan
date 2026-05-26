# Market Analysis — 2026-05-21 19:53 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $124,746
- **Liquidity:** $109,430

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,551 (-0.0% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,617 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%

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
- **Confidence:** 65%
- **p_true:** 92.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Fight is confirmed by multiple sources with event week already launched. However, the 5% gap (base rate 98% vs YES 93%) does not exceed the >5% threshold required for a bet. No new catalyst has emerged since the last decision - all evidence is confirmatory of what was already priced in. With only 2 days left and no cancellation signals, the market is approximately correctly priced given normal risk premiums for live events.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_odds({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk Verhoeven'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_sports_data({'sport': 'nba', 'team': 'Usyk Verhoeven'})` → No injury data found for nba Usyk Verhoeven
- `search_web({'query': 'Oleksandr Usyk vs Rico Verhoeven Glory in Giza 2025'})` → [Sun, 17 May 2026] Google News
[Fri, 27 Feb 2026] Usyk vs Rico and more: Boxing schedule and preview
- `search_web({'query': 'Usyk Verhoeven fight confirmed date June 2025'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] ‘It kills him’: Tony Bellew says Tyson Fury hasn’t
- `get_market_context({'keyword': 'Usyk Verhoeven glory giza'})` → No related markets found for 'Usyk Verhoeven glory giza'
- `search_web({'query': 'Usyk vs Verhoeven fight cancellation news May 2025'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Boxing schedule - ESPN
[Mon, 18 May 2026] Boxing s
- `search_web({'query': 'Glory Giza boxing event status update'})` → [Wed, 20 May 2026] Google News
[Sun, 17 May 2026] ‘Glory in Giza’ boxing week launched at the Sphinx

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*