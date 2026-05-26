# Market Analysis — 2026-05-21 21:06 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $142,404
- **Liquidity:** $118,303

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,650 (+0.0% 24h) → neutral
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
Gap is exactly 5% (98% base vs 93% market), which sits at the gate threshold but doesn't exceed it. Usyk is an elite boxer (former undisputed cruiserweight and heavyweight champion) facing Rico Verhoeven, a kickboxing champion making his boxing debut. While Usyk should win decisively (p_true ~97%), no new catalyst, injury news, or breaking information was found to justify a bet. The 5% edge is minimal, and past decisions for this same market also chose SKIP at this threshold. Fight is confirmed for May 23 with no cancellations or issues detected.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_market_context({'keyword': 'Usyk Verhoeven Glory Giza'})` → No related markets found for 'Usyk Verhoeven Glory Giza'
- `search_web({'query': 'Usyk vs Rico Verhoeven Glory in Giza fight news'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Usyk vs Rico prediction: Who will win and how - Ba
- `search_web({'query': 'Oleksandr Usyk Rico Verhoeven weigh-in results injury update 2026'})` → [Fri, 08 May 2026] Google News
[Mon, 06 Apr 2026] Boxing Schedule - Boxing Insider
[Fri, 06 Feb 2026
- `search_web({'query': 'Usyk Verhoeven fight cancelled May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Usyk vs Rico prediction: Who will win and how - Ba
- `search_web({'query': 'Oleksandr Usyk recent fights 2025 2026 record'})` → [Wed, 06 May 2026] Google News
[Fri, 27 Feb 2026] Men's boxing P4P rankings: New No. 1; Benavidez on
- `search_web({'query': 'Oleksandr Usyk last fight result 2025'})` → [Sat, 19 Jul 2025] Google News
[Thu, 04 Dec 2025] Oleksandr Usyk: Biography, record, fights and more
- `get_odds({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*