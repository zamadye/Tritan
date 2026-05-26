# Market Analysis — 2026-05-21 20:17 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $135,739
- **Liquidity:** $112,871

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,653 (+0.0% 24h) → neutral
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
Gap is exactly 5% (base rate 98% vs market 93%), which is at the gate threshold but not above it. No new injury news, cancellation risk, or breaking catalysts. Fight is confirmed and underway. Historical base rate supports Usyk winning, but the 5% gap does not provide sufficient edge to bet given fighting's inherent variance. Previous analyses also SKIPped with same reasoning.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `search_web({'query': 'Oleksandr Usyk vs Rico Verhoeven fight status update'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Oleksandr Usyk vs. Rico Verhoeven: What's the belt
- `search_web({'query': 'Glory in Giza Usyk Verhoeven injury news'})` → [Tue, 19 May 2026] Google News
[Thu, 21 May 2026] Verhoeven Vows to Beat Usyk in Giza as Atlas Dismi
- `get_market_context({'keyword': 'Usyk'})` → No related markets found for 'Usyk'
- `get_market_context({'keyword': 'Verhoeven'})` → No related markets found for 'Verhoeven'
- `search_web({'query': 'Usyk injury news May 2026'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Usyk vs. Verhoeven Start Time, Full Fight Card - Y
- `search_web({'query': 'Rico Verhoeven injury news May 2026'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] Usyk vs. Verhoeven Start Time, Full Fight Card - Y
- `get_odds({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': '"Glory in Giza" Polymarket'})` → No search results for: "Glory in Giza" Polymarket
- `search_web({'query': 'Usyk Verhoeven Glory Giza fight May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Heavyweight Richard Torrez Jr is Ready For 'The Mo
- `search_web({'query': 'Oleksandr Usyk Rico Verhoeven fight odds favorite'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Predicti
- `search_web({'query': 'Oleksandr Usyk vs Rico Verhoeven odds prediction Sports Illustrated'})` → [Thu, 21 May 2026] Google News
[Tue, 14 Apr 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Predicti
- `search_web({'query': 'Usyk vs Verhoeven who is favorite odds boxing kickboxing'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Predicti
- `get_market_context({'keyword': 'Glory Giza'})` → No related markets found for 'Glory Giza'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*