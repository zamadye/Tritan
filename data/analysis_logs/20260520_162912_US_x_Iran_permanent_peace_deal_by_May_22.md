# Market Analysis — 2026-05-20 16:29 UTC

## Market
- **Question:** US x Iran permanent peace deal by May 22, 2026?
- **Category:** geopolitik
- **YES Price:** 6.0%
- **Days Left:** 1
- **Volume 24h:** $995,226
- **Liquidity:** $79,497

## Statistical Prior
- **p_base:** 1.0%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,139 (+0.8% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,139 (+0.8% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
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
- [Mon, 18 May 2026] Israeli strikes on Iranian universities escalate conflict, impact peace deal prospects
- → US President Donald Trump said Tehran repeatedly expressed interest in signing an agreement but accused Iranian leaders of changing their position d

## LLM Decision
- **Action:** SKIP
- **Confidence:** 35%
- **p_true:** 1.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** DIPLOMATIC_BREAKTHROUGH
- **Catalyst Strength:** 0.15

### Reasoning
Market expires TOMORROW with negotiations still incomplete. Iran's latest offer deemed 'insufficient' by US officials. 'Permanent peace deal' is far more comprehensive than current diplomatic efforts (one-page hostilities plan). No concrete evidence of imminent deal signing. 6% price appropriately reflects slim last-minute breakthrough chance. Previous SKIP decisions validated. Geopolitik track record weak (11% WR). No actionable edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 35%<52%

## Tool Calls
- `search_web({'query': 'US Iran peace deal negotiations May 2026 latest news'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Trump says negotiations with Iran in final stages,
- `search_web({'query': 'Trump Iran nuclear deal negotiations May 22 2026'})` → [Tue, 19 May 2026] Google News
[Fri, 15 May 2026] Donald Trump delays Iran strike, says nuclear deal
- `get_market_context({'keyword': 'Iran peace deal'})` → No related markets found for 'Iran peace deal'
- `search_web({'query': '"peace deal" Iran US negotiations breakthrough May 2026'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Trump claims planned attack on Iran postponed afte
- `search_web({'query': 'Iran nuclear agreement timeline permanent deal 2026'})` → [Fri, 15 May 2026] Google News
[Thu, 07 May 2026] ‘20 years is enough’: Trump puts a timeline on lim

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*