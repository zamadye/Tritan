# Market Analysis — 2026-05-20 17:07 UTC

## Market
- **Question:** US x Iran permanent peace deal by May 22, 2026?
- **Category:** geopolitik
- **YES Price:** 6.2%
- **Days Left:** 1
- **Volume 24h:** $1,030,181
- **Liquidity:** $81,194

## Statistical Prior
- **p_base:** 1.0%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 5.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,242 (+0.5% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,222 (+0.5% 24h) → neutral

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
- [Wed, 13 May 2026] Israeli strikes on Iranian universities escalate conflict, impact peace deal prospects
- → Netanyahu secretly visits the UAE amid tensions with Iran. Permanent peace deal with Iran by June 30, 2026 at 16.5% YES.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 35%
- **p_true:** 1.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market expires TOMORROW (May 22) with NO evidence of imminent deal. Recent news (May 19-20) shows: (1) Trump turning to allies as 'deal proves elusive' - Guardian, (2) US threatening to hit Iran again while claiming Tehran wants deal - France 24, (3) Previous 21-hour talks in Pakistan FAILED with no agreement, (4) Iran's proposals rejected as 'insufficient' and 'unacceptable'. While YES at 6% may be slightly overpriced vs true probability (~2%), the edge is insufficient for a confident bet. Category performance is weak (11% WR from 9 trades), past decisions showed low confidence (35%, 45%), and the 1-day timeframe with negative news flow makes any last-minute permanent peace deal extremely improbable. No concrete catalyst exists for a breakthrough.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 35%<52%

## Tool Calls
- `search_web({'query': 'US Iran permanent peace deal negotiations May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 11 May 2026] Iran has responded to latest US peace proposal, Te
- `search_web({'query': 'Iran peace proposal Trump rejected unacceptable May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 11 May 2026] Iran's new offer is insufficient, risks war resump
- `search_web({'query': 'US Iran deal signed agreement May 22 2026'})` → [Wed, 20 May 2026] Google News
[Thu, 23 Apr 2026] War, latest news. Arab media: US-Iran deal being f
- `search_web({'query': 'US Iran peace deal negotiations collapse May 2026'})` → [Mon, 18 May 2026] Google News
[Tue, 05 May 2026] Pakistan’s mediation faces limits as Iran-US tensi
- `search_web({'query': '"US and Iran fail to agree" Vance May 2026'})` → [Tue, 05 May 2026] Google News
[Sun, 12 Apr 2026] U.S. And Iran Fail to Agree on Peace Deal After 21
- `get_market_context({'keyword': 'Iran peace deal'})` → No related markets found for 'Iran peace deal'
- `search_web({'query': 'Iran US last minute deal May 21 2026'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Trump sets days-long deadline for Iran deal as war
- `search_web({'query': 'Trump Iran deal deadline May 22 2026 news'})` → [Wed, 22 Apr 2026] Google News
[Wed, 22 Apr 2026] Trump extends ceasefire as uncertainty over U.S.-I
- `search_web({'query': 'Iran US peace deal May 19 20 21 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Trump turns to Middle East allies as deal to end I

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*