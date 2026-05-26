# Market Analysis — 2026-05-21 20:53 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $139,330
- **Liquidity:** $121,626

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,661 (+0.0% 24h) → neutral
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
- **Catalyst Strength:** 0.00

### Reasoning
No verifiable edge exists. Gap is exactly 5% (98% base vs 93% market), which sits AT the threshold but NOT above it. Fight confirmed for May 23 at Pyramids of Giza with multiple recent sources (BBC, ESPN, Sports Illustrated, Yahoo Sports). No injury reports found for either Usyk or Verhoeven. Usyk appears to be training normally (Joshua training camp partnership noted). The 93% pricing for a heavyweight boxing champion vs a kickboxer is reasonable. Previous SKIP decisions on this same market correctly identified the lack of edge. No catalyst or information asymmetry detected.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_odds({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Usyk Verhoeven'})` → No related markets found for 'Usyk Verhoeven'
- `search_web({'query': 'Oleksandr Usyk Rico Verhoeven fight date 2025'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] ‘It kills him’: Tony Bellew says Tyson Fury hasn’t
- `search_web({'query': 'Glory in Giza Usyk Verhoeven May 2025'})` → [Sun, 17 May 2026] Google News
[Fri, 27 Feb 2026] How to Watch Oleksandr Usyk vs Rico Verhoeven: Dat
- `search_web({'query': 'Usyk Verhoeven odds betting'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Predicti
- `search_web({'query': 'Usyk injury May 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Usyk vs. Verhoeven Start Time, Full Fight Card - Y
- `search_web({'query': 'Usyk condition training camp'})` → [Tue, 24 Mar 2026] Google News
[Thu, 14 May 2026] Anthony Joshua Back In Training Camp With Oleksand

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*