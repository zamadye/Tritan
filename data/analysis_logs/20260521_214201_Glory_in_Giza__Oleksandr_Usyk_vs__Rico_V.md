# Market Analysis — 2026-05-21 21:42 UTC

## Market
- **Question:** Glory in Giza: Oleksandr Usyk vs. Rico Verhoeven
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 2
- **Volume 24h:** $142,881
- **Liquidity:** $119,255

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,700 (+0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,688 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: glory giza: oleksandr usyk rico
- [Bing News]
- [] glory giza: oleksandr usyk rico
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 92.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Usyk is an overwhelming favorite (undisputed champion) versus Rico Verhoeven, a kickboxer making his boxing debut. The market underprices YES by 5% (93% vs 98% base rate), aligning with the 5% gate threshold but offering no clear statistical edge. No new injury or cancellation news found; fight is scheduled for May 22, 2026. Past similar markets were skipped due to the gap being exactly at the gate threshold.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `search_web({'query': 'Oleksandr Usyk vs Rico Verhoeven Glory in Giza fight news'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Usyk vs Rico prediction: Who will win and how - Ba
- `search_web({'query': 'Usyk vs Verhoeven odds betting prediction 2026'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Usyk vs Verhoeven Odds &amp; Picks - Pyramids of G
- `get_market_context({'keyword': 'Usyk Verhoeven'})` → No related markets found for 'Usyk Verhoeven'
- `get_odds({'sport': 'mma_mixed_martial_arts', 'team': 'Usyk'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Usyk vs Verhoeven fight date May 2026 latest news'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Usyk vs. Verhoeven Start Time, Full Fight Card - Y
- `search_web({'query': 'Usyk injury update May 2026'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Usyk vs. Verhoeven Start Time, Full Fight Card - Y
- `search_web({'query': 'Rico Verhoeven injury withdrawal May 2026'})` → [Thu, 21 May 2026] Google News
[Sat, 16 May 2026] Concerning Carlos Alcaraz injury update as doctors

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*