# Market Analysis — 2026-05-21 20:03 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $135,137
- **Liquidity:** $112,579

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,667 (+0.1% 24h) → neutral
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
- **Catalyst Type:** NEWS_CONFIRMATION
- **Catalyst Strength:** 0.30

### Reasoning
Fight is confirmed by multiple sources with no cancellation or injury news. Market price (93%) is slightly below historical base rate (98%), but the 5% gap is too small to provide a statistical edge after market fees. Past decisions for this same market indicate SKIP due to lack of edge. No new information or catalysts suggest the market is mispriced.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `search_web({'query': 'Usyk Rico Verhoeven Glory in Giza fight'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Predicti
- `search_web({'query': 'Usyk Verhoeven fight confirmed 2026'})` → [Wed, 20 May 2026] Google News
[Thu, 14 May 2026] Usyk vs Verhoeven: Start time, undercard and how t
- `search_web({'query': 'Usyk injury fight Verhoeven'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Heavyweight Richard Torrez Jr is Ready For 'The Mo
- `search_web({'query': 'Usyk Verhoeven fight cancelled'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Oleksandr Usyk vs. Rico Verhoeven: What's the belt
- `search_web({'query': 'Usyk weight cut Verhoeven fight week'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Usyk vs Rico prediction: Who will win and how - Ba
- `get_market_context({'keyword': 'Usyk Verhoeven'})` → No related markets found for 'Usyk Verhoeven'
- `get_market_context({'keyword': 'Glory in Giza'})` → No related markets found for 'Glory in Giza'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*