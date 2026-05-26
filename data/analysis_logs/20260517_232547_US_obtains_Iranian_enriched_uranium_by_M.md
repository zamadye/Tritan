# Market Analysis — 2026-05-17 23:25 UTC

## Market
- **Question:** US obtains Iranian enriched uranium by May 31?
- **Category:** geopolitik
- **YES Price:** 6.0%
- **Days Left:** 13
- **Volume 24h:** $383,445
- **Liquidity:** $404,892

## Statistical Prior
- **p_base:** 1.0%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,829 (-0.5% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,876 (-0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%
- → Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls
- → Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally
- → Iran military strike → oil spike → global inflation → Fed hawkish

### Multi-Source
- [MULTI-SOURCE NEWS] 4 sources for: obtains iranian enriched uranium
- [Bing News]
- [Sat, 16 May 2026] obtains iranian enriched uranium
- → Iran rejects the transfer of enriched uranium, citing distrust of the US. US obtaining Iranian enriched uranium by May 31 at 5.5% YES.
- [Tue, 12 May 2026] Iran rejects enriched uranium transfer, citing distrust of US
- → In the “Iran’s Enriched Uranium Surrender” market, YES shares are currently priced at 46%, up from 42% a day ago. In the “US Obtains Iranian Enriche
- [Sun, 19 Apr 2026] Iran rejects US demands for uranium surrender, tensions rise
- → Transporting nuclear material from the country would involve extracting material from nuclear sites that have been turned to rubble by American and 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 1.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL_NEGOTIATION
- **Catalyst Strength:** 0.50

### Reasoning
US has demanded 400 kg uranium as part of ceasefire (directly relevant), but negotiations are stalled ('life support'), active conflict ongoing, only 13 days remain for deal + physical transfer. Market at 6% (6x base rate) already accounts for deal possibility. No clear edge - market appears fairly priced given stalled negotiations and time constraints.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'US obtain Iranian enriched uranium 2025'})` → [Mon, 11 May 2026] Google News
[Wed, 29 Apr 2026] What will happen to Iran's nuclear material? - DW.
- `search_web({'query': 'Iran nuclear deal uranium enrichment negotiations May 2025'})` → [Tue, 24 Feb 2026] Google News
[Sat, 18 Apr 2026] A timeline of tensions over Iran's nuclear program
- `get_market_context({'keyword': 'Iran uranium nuclear'})` → No related markets found for 'Iran uranium nuclear'
- `search_web({'query': 'Iran uranium transfer US negotiations May 2026 latest'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] US outlines 5 conditions for Iran deal: Report - A
- `search_web({'query': 'Iran nuclear talks progress uranium stockpile removal 2026'})` → [Mon, 11 May 2026] Google News
[Thu, 07 May 2026] Trump Says Cease-Fire With Iran on 'Life Support' 
- `search_web({'query': '"uranium transfer" US Iran conditions May 2026 ceasefire'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Uranium Transfer, Nuclear Limits: US Sets 5 Condit
- `search_web({'query': 'Iran US ceasefire status May 17 2026 latest'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Trump Says 'Clock Is Ticking' For Iran - Radio Fre
- `search_web({'query': 'Trump 400 kg uranium Iran transfer deal timeline deadline'})` → [Sun, 19 Apr 2026] Google News
[Thu, 26 Feb 2026] The Strait of Hormuz keeps markets on edge as ceas
- `search_web({'query': 'Iran war ceasefire status progress May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Trump Says 'Clock Is Ticking' For Iran - Radio Fre

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*