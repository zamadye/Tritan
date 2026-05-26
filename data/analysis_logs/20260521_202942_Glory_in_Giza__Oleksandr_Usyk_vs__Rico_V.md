# Market Analysis — 2026-05-21 20:29 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $138,147
- **Liquidity:** $110,636

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,640 (+0.2% 24h) → neutral
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
- **Catalyst Type:** NONE_IDENTIFIED
- **Catalyst Strength:** 0.30

### Reasoning
Fight confirmed by multiple recent sources (MMA Mania, Radio Times, Sports Illustrated) for May 21 - just 2 days away. Travel uncertainty from March appears resolved. Market at 93% vs base rate 98% = 5% gap, exactly at decision gate threshold but not above it. No cancellation/injury news found. Prior decisions on this same market also skipped at same gap. Without verifiable catalyst explaining why market discounts below base rate, cannot confirm edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_odds({'sport': 'mma_mixed_martial_arts'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Oleksandr Usyk vs Rico Verhoeven Glory in Giza fight news'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Usyk vs Rico prediction: Who will win and how - Ba
- `search_web({'query': 'Usyk Rico Verhoeven injury cancellation latest update'})` → [Tue, 31 Mar 2026] Google News
[Tue, 14 Apr 2026] Usyk ‘100% looking at plan B’ due to travel uncert
- `search_web({'query': 'Usyk travel uncertainty Verhoeven fight plan B'})` → [Tue, 31 Mar 2026] Google News
[Tue, 24 Mar 2026] Usyk ‘100% looking at plan B’ due to travel uncert
- `search_web({'query': '"100% looking at plan B" Usyk Verhoeven'})` → [Tue, 31 Mar 2026] Google News
[Tue, 31 Mar 2026] Usyk ‘100% looking at plan B’ due to travel uncert
- `search_web({'query': 'Rico Verhoeven fight could be moved Glory in Giza'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Predicti
- `get_market_context({'keyword': 'Glory in Giza'})` → No related markets found for 'Glory in Giza'
- `get_market_context({'keyword': 'Usyk'})` → No related markets found for 'Usyk'
- `get_market_context({'keyword': 'Rico Verhoeven'})` → No related markets found for 'Rico Verhoeven'
- `search_web({'query': 'Glory in Giza Usyk Verhoeven May 2026 fight confirmed'})` → [Mon, 18 May 2026] Google News
[Thu, 21 May 2026] Usyk vs. Verhoeven Start Time, Full Fight Card - M

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*