# Market Analysis — 2026-05-20 18:00 UTC

## Market
- **Question:** US x Iran permanent peace deal by May 22, 2026?
- **Category:** geopolitik
- **YES Price:** 7.7%
- **Days Left:** 1
- **Volume 24h:** $1,028,822
- **Liquidity:** $74,153

## Statistical Prior
- **p_base:** 1.4%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 6.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,479 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,477 (+0.9% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%
- → Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls
- → Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally
- → Iran military strike → oil spike → global inflation → Fed hawkish

### Multi-Source
- [MULTI-SOURCE NEWS] 4 sources for: iran permanent peace deal 2026
- [Bing News]
- [Tue, 19 May 2026] iran permanent peace deal 2026
- → Trump told reporters at the White House that he had been just &quot;an hour away&quot; from relaunching Washington's attacks on Iran before postponi
- [Wed, 13 May 2026] US, Iran trade threats but Trump says Tehran wants peace deal
- → Israeli strikes on Iranian universities escalate tensions. Permanent peace deal by June 30, 2026 at 16.5% YES.
- [Mon, 18 May 2026] Israeli strikes on Iranian universities escalate conflict, impact peace deal prospects
- → US President Donald Trump said Tehran repeatedly expressed interest in signing an agreement but accused Iranian leaders of changing their position d

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 1.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** ONGOING_NEGOTIATIONS
- **Catalyst Strength:** 0.30

### Reasoning
Market expires tomorrow (May 22) with negotiations in 'final stages' but no concrete evidence of imminent signing. A permanent peace deal requires extensive formal documentation and cannot realistically be completed in 1 day. Current 8% price already reflects negotiation optimism; no clear edge to bet YES or NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'US Iran permanent peace deal May 2026 negotiations latest news'})` → [Mon, 18 May 2026] Google News
[Mon, 11 May 2026] Iran has responded to latest US peace proposal, Te
- `search_web({'query': 'Iran US peace deal latest May 19 2026 negotiations ceasefire'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] Trump says Iran attack on ‘hold’: What we know abo
- `get_market_context({'keyword': 'Iran US peace deal'})` → No related markets found for 'Iran US peace deal'
- `get_market_context({'keyword': 'Iran'})` → [YES=50% vol=$2,631,779] Will Trump say "Iran" during events with Xi Jinping?
- `search_web({'query': '"permanent peace deal" Iran US May 22 2026'})` → [Wed, 20 May 2026] Google News
[Fri, 01 May 2026] Prediction Markets Track Elon Musk's Tweet Volume 
- `search_web({'query': 'Trump Iran peace deal negotiations May 20 2026 Reuters'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Trump says negotiations with Iran in final stages,
- `search_web({'query': 'Iran US deal signing ceremony May 22 2026'})` → [Thu, 23 Apr 2026] Google News
[Wed, 22 Apr 2026] Trump Says Israel and Lebanon Agree to Extend Ceas

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*