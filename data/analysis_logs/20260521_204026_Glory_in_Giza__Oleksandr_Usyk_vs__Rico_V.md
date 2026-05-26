# Market Analysis — 2026-05-21 20:40 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $138,917
- **Liquidity:** $125,139

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,673 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,632 (+0.1% 24h) → neutral
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
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Gap is exactly 5% (base 98% vs market 93%), which sits at gate threshold but not above it. Usyk is undisputed heavyweight boxing champion moving DOWN in competition to face kickboxer Rico Verhoeven under boxing rules—massive structural advantage. No injury news, no cancellation signals, fight confirmed for May 21. Market appears efficiently priced given Verhoeven's elite striking background creates some (minimal) uncertainty. No concrete catalyst to exploit the marginal edge. Previous decisions correctly flagged same 5% gap as insufficient. Sports pattern WR=76% is strong but requires edge above threshold.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_odds({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk Verhoeven'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Usyk vs Verhoeven Glory in Giza May 21 2025 latest news'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Usyk vs Rico prediction: Who will win and how - Ba
- `search_web({'query': 'Glory in Giza Usyk Verhoeven fight confirmed tomorrow'})` → [Thu, 21 May 2026] Google News
[Sun, 17 May 2026] Oleksandr Usyk vs. Rico Verhoeven: How to watch in
- `search_web({'query': 'Usyk injury news Verhoeven injury update fight'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Alistair Overeem believes Rico Verhoeven grudge fi
- `get_market_context({'keyword': 'Usyk Verhoeven Glory in Giza'})` → No related markets found for 'Usyk Verhoeven Glory in Giza'
- `search_web({'query': 'Usyk vs Verhoeven odds boxing heavyweight 2026'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Rico Verhoeven Closes Chapter of Life Ahead of His
- `search_web({'query': 'Usyk vs Verhoeven betting odds who is favored'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Predicti

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*