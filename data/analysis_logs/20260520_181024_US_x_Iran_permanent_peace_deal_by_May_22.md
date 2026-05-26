# Market Analysis — 2026-05-20 18:10 UTC

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
- **Action:** SKIP
- **Confidence:** 42%
- **p_true:** 2.3%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL_NEGOTIATION_DEADLINE
- **Catalyst Strength:** 0.30

### Reasoning
Market expires TOMORROW (May 22) with YES at 10%. Latest news (May 20) shows negotiations are 'in final stages' per Trump, but NO deal has been signed or announced. Past decisions correctly identified this as uncertain (45% conf). While a deal COULD be announced imminently, there is no concrete evidence it will be completed by deadline. The 10% YES price already reflects appropriate skepticism given 'final stage' uncertainty. BET_NO edge is only ~2-3% (p_true=7% vs 10% price) which is too thin after transaction costs. No verifiable edge exists—just speculation on last-minute negotiations. GEOPOLITIK pattern shows weak 11% WR overall. SKIP due to insufficient evidence and minimal expected value.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 42%<52%

## Tool Calls
- `search_web({'query': 'US Iran permanent peace deal May 22 2026 negotiations latest'})` → [Wed, 06 May 2026] Google News
[Mon, 11 May 2026] US, Iran said closing in on framework for permanen
- `search_web({'query': 'US Iran deal final stages May 2026 signing today'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Trump says negotiations with Iran in final stages,
- `get_market_context({'keyword': 'Iran peace deal'})` → No related markets found for 'Iran peace deal'
- `search_web({'query': '"US Iran" deal signed May 22 2026 announcement today'})` → [Wed, 20 May 2026] Google News
[Thu, 23 Apr 2026] War, latest news. Arab media: US-Iran deal being f
- `search_web({'query': 'Iran nuclear deal deadline May 22 2026'})` → [Tue, 19 May 2026] Google News
[Wed, 22 Apr 2026] Trump Grants Iran Two-to-Three Day Extension for N
- `search_web({'query': 'Trump Iran deal today May 21 2026 announcement'})` → [Tue, 05 May 2026] Google News
[Tue, 21 Apr 2026] U.S. And Iran Fail to Agree on Peace Deal After 21
- `search_web({'query': 'Iran peace deal negotiations final stages May 2026 status update'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Trump says negotiations with Iran in final stages,

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*