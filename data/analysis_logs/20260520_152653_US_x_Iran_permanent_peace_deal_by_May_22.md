# Market Analysis — 2026-05-20 15:26 UTC

## Market
- **Question:** US x Iran permanent peace deal by May 22, 2026?
- **Category:** geopolitik
- **YES Price:** 8.5%
- **Days Left:** 1
- **Volume 24h:** $874,448
- **Liquidity:** $48,833

## Statistical Prior
- **p_base:** 1.7%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 6.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,605 (+1.6% 24h) → risk-ON
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,605 (+1.6% 24h) → risk-ON

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%
- → Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls
- → Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally
- → Iran military strike → oil spike → global inflation → Fed hawkish

### Multi-Source
- [MULTI-SOURCE NEWS] 5 sources for: iran permanent peace deal 2026
- [Bing News]
- [Tue, 19 May 2026] iran permanent peace deal 2026
- → Trump told reporters at the White House that he had been just &quot;an hour away&quot; from relaunching Washington's attacks on Iran before postponi
- [Wed, 13 May 2026] US, Iran trade threats but Trump says Tehran wants peace deal
- → Israeli strikes on Iranian universities escalate tensions. Permanent peace deal by June 30, 2026 at 16.5% YES.
- [Wed, 13 May 2026] Israeli strikes on Iranian universities escalate conflict, impact peace deal prospects
- → Netanyahu secretly visits the UAE amid tensions with Iran. Permanent peace deal with Iran by June 30, 2026 at 16.5% YES.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 1.7%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL_NEGOTIATIONS
- **Catalyst Strength:** 0.60

### Reasoning
Breaking news from yesterday (May 18): Trump called off scheduled attack on Iran amid 'serious negotiations' toward peace deal. VP Vance discussing specific terms (uranium to Russia). However, news refers to 'truce' and 'ceasefire' negotiations, NOT a permanent peace deal. The 8% price already reflects some deal probability. With only 3 days left, going from active war to PERMANENT PEACE DEAL is an extremely high bar. No clear edge on the specific outcome. Geopolitics category has poor track record (11% WR).

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'US Iran peace deal negotiations 2025 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 21 Apr 2026] Vance responds to reports that US may send Iran's 
- `search_web({'query': 'Iran nuclear deal negotiations latest news May 2025'})` → [Tue, 24 Feb 2026] Google News
[Mon, 19 Jan 2026] A timeline of tensions over Iran's nuclear program
- `search_web({'query': 'US Iran diplomatic relations latest developments'})` → [Tue, 12 May 2026] Google News
[Sun, 03 May 2026] Iran War Costs Reverberate Domestically - Council 
- `get_market_context({'keyword': 'Iran deal'})` → No related markets found for 'Iran deal'
- `search_web({'query': 'Iran war ceasefire May 2026 status'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Trump calls off scheduled attack on Iran amid "ser
- `search_web({'query': '"peace deal" Iran May 22 2026 deadline'})` → [Mon, 18 May 2026] Google News
[Wed, 22 Apr 2026] Trump says media and Democrats would spin even Ira
- `get_market_context({'keyword': 'Iran ceasefire'})` → No related markets found for 'Iran ceasefire'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*