# Market Analysis — 2026-05-21 00:35 UTC

## Market
- **Question:** Will the Iran ceasefire continue through June 7?
- **Category:** geopolitik
- **YES Price:** 59.0%
- **Days Left:** None
- **Volume 24h:** $18,837
- **Liquidity:** $25,438

## Statistical Prior
- **p_base:** 51.1%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,616 (+1.3% 24h) → risk-ON
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,647 (+1.4% 24h) → risk-ON
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
- **p_true:** 43.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.70

### Reasoning
Market at 59% overprices YES vs historical base rate (51%) and stat signal (44.7% at this price, n=13,967). News shows negotiations in flux with uncertainty, not concrete evidence of continuation. Pattern from similar Iran geopolitical markets indicates systematic overpricing of YES outcomes.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Iran ceasefire latest news June 2025'})` → [Fri, 10 Apr 2026] Google News
[Sun, 01 Mar 2026] New tensions emerge before US-Iran war ceasefire t
- `search_web({'query': 'Iran US ceasefire negotiations June 2026 status'})` → [Fri, 08 May 2026] Google News
[Mon, 27 Apr 2026] U.S. launches "self-defense strikes" on Iran, says
- `search_web({'query': '"Iran ceasefire" June 2026'})` → [Sat, 16 May 2026] Google News
[Mon, 27 Apr 2026] Oil markets may face moment of truth in June. Brac
- `get_market_context({'keyword': 'Iran ceasefire'})` → No related markets found for 'Iran ceasefire'
- `search_web({'query': 'Iran US conflict ceasefire status May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Trump calls off scheduled attack on Iran amid "ser
- `search_web({'query': 'Iran ceasefire expires June 2026'})` → [Tue, 21 Apr 2026] Google News
[Fri, 24 Apr 2026] U.S. delays new round of negotiations with Iran as
- `search_web({'query': 'Iran ceasefire negotiations latest news May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Trump says willing to wait for a few days to get '

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*