# Market Analysis — 2026-05-21 18:18 UTC

## Market
- **Question:** Will the Iran ceasefire continue through June 30?
- **Category:** geopolitik
- **YES Price:** 52.0%
- **Days Left:** None
- **Volume 24h:** $17,065
- **Liquidity:** $12,707

## Statistical Prior
- **p_base:** 40.6%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 11.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,644 (+0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,590 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%
- → Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls
- → Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally
- → Iran military strike → oil spike → global inflation → Fed hawkish

### Multi-Source
- [MULTI-SOURCE NEWS] 5 sources for: iran ceasefire continue through june
- [Bing News]
- [] iran ceasefire continue through june
- [Al Jazeera]
- [Thu, 21 May 2026] US-Iran diplomacy picks up: What’s the latest?
- [Thu, 21 May 2026] Maths behind Hormuz toll: Is paying Iran for transit cheaper than blockade?
- [The Guardian]
- [Thu, 21 May 2026] Macron under pressure over reparatory justice for France’s role in slave trade

## LLM Decision
- **Action:** NO
- **Confidence:** 62%
- **p_true:** 36.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_BIAS
- **Catalyst Strength:** 0.60

### Reasoning
Market overprices YES at 52% vs historical resolution rate of 44.7% (n=13,967) and base rate 41%. No positive catalyst found; talks failing and US re-arming during ceasefire suggest fragility. Past similar markets decided NO. Geopolitical category weak (21% WR).

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Iran ceasefire latest news June 2025'})` → [Fri, 10 Apr 2026] Google News
[Sun, 01 Mar 2026] New tensions emerge before US-Iran war ceasefire t
- `search_web({'query': 'Iran ceasefire extension June 30 2025'})` → [Thu, 07 May 2026] Google News
[Wed, 08 Apr 2026] Iran urges UN members not to support ‘provocative’
- `search_web({'query': 'Iran ceasefire news April 2025'})` → [Fri, 24 Apr 2026] Google News
[Tue, 14 Apr 2026] As U.S. re-arms during Iran ceasefire, long-term c
- `search_web({'query': 'US Iran ceasefire talks 2025'})` → [Wed, 06 May 2026] Google News
[Sat, 25 Apr 2026] Iran Nuclear Talks: Three Lessons From the War for
- `get_market_context({'keyword': 'Iran ceasefire'})` → No related markets found for 'Iran ceasefire'
- `get_market_context({'keyword': 'Iran war'})` → No related markets found for 'Iran war'
- `get_market_context({'keyword': 'Iran conflict'})` → No related markets found for 'Iran conflict'
- `get_market_context({'keyword': 'ceasefire'})` → No related markets found for 'ceasefire'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*