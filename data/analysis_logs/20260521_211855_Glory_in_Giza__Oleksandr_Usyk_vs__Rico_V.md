# Market Analysis — 2026-05-21 21:18 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $142,856
- **Liquidity:** $118,401

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,698 (+0.0% 24h) → neutral
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
- **Confidence:** 65%
- **p_true:** 92.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Market underprices Usyk by 5% (93% vs 98% base rate), but the gap sits exactly at the 5% gate threshold without exceeding it. Two previous decisions correctly identified this threshold issue. Limited upside (7% gain) with no new catalyst or injury reports. While Usyk is heavily favored as an undisputed boxing champion vs a kickboxer, the risk/reward ratio doesn't justify a bet at this threshold.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_odds({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_sports_data({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk'})` → No injury data found for mma_mixed_martial_arts Usyk
- `get_market_context({'keyword': 'Usyk Verhoeven Glory Giza'})` → No related markets found for 'Usyk Verhoeven Glory Giza'
- `search_web({'query': 'Usyk vs Rico Verhoeven Glory in Giza 2025 fight result'})` → [Sun, 17 May 2026] Google News
[Fri, 27 Feb 2026] Usyk vs Rico and more: Boxing schedule and preview
- `search_web({'query': 'Oleksandr Usyk Glory kickboxing debut rules'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Usyk vs Rico: Date, UK time, ringwalk, radio, unde
- `search_web({'query': 'Usyk vs Verhoeven prediction odds favorite heavyweight 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Usyk vs Rico prediction: Who will win and how - Ba
- `search_web({'query': 'Rico Verhoeven record kickboxing boxing Usyk'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Predicti
- `search_web({'query': 'Usyk vs Verhoeven betting odds sportsbook favorite percentage'})` → [Mon, 18 May 2026] Google News
[Wed, 21 Jan 2026] Best Boxing Betting Apps &amp; Sites for Usyk vs. 
- `search_web({'query': 'Usyk Verhoeven injury news training camp 2026'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] Heavyweight Richard Torrez Jr is Ready For 'The Mo

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*