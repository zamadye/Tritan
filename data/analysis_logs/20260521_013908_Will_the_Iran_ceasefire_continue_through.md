# Market Analysis — 2026-05-21 01:39 UTC

## Market
- **Question:** Will the Iran ceasefire continue through June 15?
- **Category:** geopolitik
- **YES Price:** 52.0%
- **Days Left:** None
- **Volume 24h:** $16,194
- **Liquidity:** $22,390

## Statistical Prior
- **p_base:** 40.6%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 11.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,762 (+1.5% 24h) → risk-ON
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,802 (+1.7% 24h) → risk-ON
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
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
- [Wed, 20 May 2026] Iran war live: Tehran says no surrender to US, diplomacy ‘wiser’ than war
- [Wed, 20 May 2026] How AIPAC channels millions through shell PACs ahead of US midterms
- [The Guardian]
- [Tue, 19 May 2026] Rubio criticizes WHO’s Ebola response as US continues sweeping public health cuts

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 34.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL_FRAGILITY
- **Catalyst Strength:** 0.65

### Reasoning
Market overprices YES at 52% vs base rate 41% (gap: -11%) and stat signal 44.7% (n=13,967). Direct recent evidence (April 20, 2026) describes ceasefire as 'tenuous' and 'on the verge of collapse.' Oil markets rose 6% on collapse fears. Past similar Iran ceasefire markets resolved NO. The crowd has not fully priced in the fragility of the ceasefire, creating a statistical edge on the NO side.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Iran ceasefire June 15 2025'})` → [Mon, 06 Apr 2026] Google News
[Fri, 09 Jan 2026] Türkiye, Egypt, Pakistan seek Iran’s return to US 
- `search_web({'query': 'Iran ceasefire latest news June 2026'})` → [Wed, 01 Apr 2026] Google News
[Mon, 06 Apr 2026] Trump Seeks Deal With Iran to End War - Arms Contr
- `get_market_context({'keyword': 'Iran ceasefire'})` → No related markets found for 'Iran ceasefire'
- `get_market_context({'keyword': 'Iran war'})` → No related markets found for 'Iran war'
- `search_web({'query': 'Iran war ceasefire status June 2026'})` → [Tue, 21 Apr 2026] Google News
[Thu, 23 Apr 2026] Last Rounds? Status of Key Munitions at the Iran W
- `search_web({'query': 'Iran ceasefire collapse June 2026'})` → [Thu, 09 Apr 2026] Google News
[Mon, 20 Apr 2026] An Already Tenuous Ceasefire in Iran Hovers on the
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $77,802.00 | 24h: +1.70%

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*