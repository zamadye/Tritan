# Market Analysis — 2026-05-21 22:07 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $143,337
- **Liquidity:** $119,818

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,577 (+0.3% 24h) → neutral
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
- **Confidence:** 62%
- **p_true:** 92.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** MISMATCH_RECOGNITION
- **Catalyst Strength:** 0.40

### Reasoning
Oleksandr Usyk (undisputed heavyweight champion) vs Rico Verhoeven (kickboxer making boxing debut) remains a massive mismatch. Market at 93% vs base rate 98% gives only 5% gap - exactly at threshold, not above. Past decisions correctly identified this as SKIP territory. New data point: Verhoeven had stoppage win on boxing debut, slightly increasing his probability from ~2% to ~4%, but market still prices him at 7%. Edge has narrowed from ~5% to ~3-4%, falling below the 5% gate. No injuries, no breaking news, fight is 2 days away. While crowd may be overvaluing Verhoeven's kickboxing credentials (crowd_bias=true), the remaining edge is insufficient to justify a bet given the small margin and imminent timeline.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `search_web({'query': 'Usyk vs Verhoeven odds betting'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Predicti
- `search_web({'query': 'Usyk Verhoeven boxing match news latest'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Usyk vs Rico prediction: Who will win and how - Ba
- `get_sports_data({'sport': 'mma_mixed_martial_arts', 'team': 'usyk'})` → No injury data found for mma_mixed_martial_arts usyk
- `get_market_context({'keyword': 'Usyk Verhoeven'})` → No related markets found for 'Usyk Verhoeven'
- `search_web({'query': 'Usyk vs Verhoeven odds sportsbook betting lines'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Predicti
- `search_web({'query': 'Usyk Verhoeven fight odds prediction'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Oleksandr Usyk vs Rico Verhoeven Odds and Predicti
- `search_web({'query': '"Usyk vs Verhoeven" odds moneyline'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Usyk vs Verhoeven Odds &amp; Picks - Pyramids of G
- `get_odds({'sport': 'mma_mixed_martial_arts'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Oleksandr Usyk Rico Verhoeven fight preview who will win'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Usyk vs Rico prediction: Who will win and how - Ba
- `search_web({'query': 'Usyk vs Verhoeven boxing match weigh-in training camp'})` → [Wed, 20 May 2026] Google News
[Sat, 16 May 2026] Oleksandr Usyk makes one change in training camp a
- `search_web({'query': 'Oleksandr Usyk training camp changes Verhoeven fight motivation'})` → [Wed, 20 May 2026] Google News
[] Oleksandr Usyk reveals plan to help Anthony Joshua finally silence
- `search_web({'query': 'Rico Verhoeven boxing debut experience heavyweight'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Usyk vs Verhoeven: 5 boxers who found success in k
- `search_web({'query': '"Usyk vs Verhoeven" odds 2026 moneyline favorite'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Usyk vs Verhoeven Odds &amp; Picks - Pyramids of G
- `search_web({'query': 'Rico Verhoeven boxing record debut win'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Usyk vs Rico prediction: Who will win and how - Ba
- `search_web({'query': 'Usyk Verhoeven boxing odds -1500 -2000 favorite underdog'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Rico Verhoeven Closes Chapter of Life Ahead of His
- `search_web({'query': 'Usyk motivated for Verhoeven fight champion mindset'})` → [Tue, 21 Apr 2026] Google News
[] Oleksandr Usyk v Rico Verhoeven: Big questions ahead of heavyweigh

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*