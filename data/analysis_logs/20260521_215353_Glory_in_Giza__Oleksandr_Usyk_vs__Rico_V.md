# Market Analysis — 2026-05-21 21:53 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $143,212
- **Liquidity:** $119,304

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,596 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,688 (+0.2% 24h) → neutral
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
- **Confidence:** 65%
- **p_true:** 92.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Usyk (undisputed boxing champion) vs Verhoeven (kickboxer making boxing debut) is a massive mismatch. True probability ~97-99%. Market YES=93% vs crowd base=98% shows 5% gap, but: (1) No new information or catalyst since previous SKIP decisions - no injuries, weight cuts, or withdrawal news; (2) Gap of exactly 5% fails to exceed 5% gate threshold; (3) No bookmaker odds available to confirm edge; (4) Eddie Hearn's 'not a pushover' comment is promotional hype, not substantive. Boxing mismatches at this level rarely produce exploitable edges. Consistent with previous SKIP decisions on identical market.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `search_web({'query': 'Oleksandr Usyk vs Rico Verhoeven Glory in Giza fight update'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] He's live in this fight: Eddie Hearn says Rico Ver
- `search_web({'query': 'Usyk Verhoeven boxing match news 2025'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Boxing schedule - ESPN
[Tue, 14 Apr 2026] Rico Ver
- `search_web({'query': 'Usyk Verhoeven injury report May 2026'})` → [Thu, 21 May 2026] Google News
[Fri, 15 May 2026] Usyk arrived at the press conference with Verhoeve
- `search_web({'query': 'Glory in Giza fight card undercard updates'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] Heavyweight Richard Torrez Jr is Ready For 'The Mo
- `get_sports_data({'sport': 'boxing', 'team': 'Usyk'})` → No injury data found for boxing Usyk
- `get_sports_data({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk'})` → No injury data found for mma_mixed_martial_arts Usyk
- `get_odds({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Usyk Verhoeven'})` → No related markets found for 'Usyk Verhoeven'
- `get_market_context({'keyword': 'Glory in Giza'})` → No related markets found for 'Glory in Giza'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*