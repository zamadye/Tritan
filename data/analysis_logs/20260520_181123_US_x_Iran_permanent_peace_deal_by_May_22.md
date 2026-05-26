# Market Analysis — 2026-05-20 18:11 UTC

## Market
- **Question:** US x Iran permanent peace deal by May 22, 2026?
- **Category:** geopolitik
- **YES Price:** 10.4%
- **Days Left:** 1
- **Volume 24h:** $1,041,926
- **Liquidity:** $48,300

## Statistical Prior
- **p_base:** 2.3%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 8.1%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,455 (+0.8% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,462 (+0.8% 24h) → neutral

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
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 1.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL_NEGOTIATION
- **Catalyst Strength:** 0.20

### Reasoning
Market expires TOMORROW with no concrete evidence of deal signing. News shows negotiations 'in final stages' BUT: (1) Iran's offer deemed 'insufficient' per senior US official, (2) Iran says peace talks 'unreasonable' after Israeli strikes, (3) Conflicting messages from both sides, (4) Trump simultaneously threatening military action. 'Permanent peace deal' is an extremely high bar - not just ceasefire. Base rate 2% vs 10% price = 5x overpricing. Previous decisions correctly SKIPPED with 45% conf - I have stronger evidence now that NO deal will be finalized by May 22. The 75% WR on 10-20% entries does NOT apply here because base rate is only 2%, making the YES side a longshot with no verification of progress toward completion.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `get_market_context({'keyword': 'Iran peace deal'})` → No related markets found for 'Iran peace deal'
- `search_web({'query': 'US Iran peace deal negotiations May 2026 latest'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Trump says negotiations with Iran in final stages,
- `search_web({'query': 'US Iran nuclear deal deadline May 22 2026 agreement status'})` → [Tue, 05 May 2026] Google News
[Tue, 24 Feb 2026] U.S., Iran and Israel Agree to Cease-Fire - The Ne
- `search_web({'query': '"permanent peace deal" Iran United States 2026'})` → [Sun, 17 May 2026] Google News
[Tue, 19 May 2026] Trump hints at military action against Iran, impac
- `search_web({'query': 'Iran US deal signed today May 2026'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Trump says US may strike Iran again but that Tehra
- `search_web({'query': 'Iran deal signed today May 21 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Horoscope Tomorrow, May 21, 2026: Your zodiac insi
- `search_web({'query': 'Iran US negotiations today May 2026 status'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] Trump calls off scheduled attack on Iran amid "ser

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*