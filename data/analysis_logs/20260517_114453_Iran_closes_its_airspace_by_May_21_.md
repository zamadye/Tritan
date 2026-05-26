# Market Analysis — 2026-05-17 11:44 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 10.0%
- **Days Left:** 3
- **Volume 24h:** $105,782
- **Liquidity:** $73,066

## Statistical Prior
- **p_base:** 2.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,351 (+0.3% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,377 (+0.3% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%
- → Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls
- → Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally
- → Iran military strike → oil spike → global inflation → Fed hawkish

### Multi-Source
- [MULTI-SOURCE NEWS] 5 sources for: iran closes airspace
- [Bing News]
- [Thu, 15 Jan 2026] iran closes airspace
- → TEMPO.CO, Jakarta - Iran temporarily closed its airspace to all flights except international flights to and from Iran with official permission on We
- [Sun, 03 May 2026] Iran Closes Airspace Amid Rising Protests and Regional Tensions
- → Red Cross warns of renewed Iran attacks amid airspace closure concerns. Iran closes its airspace by May 8 at 14.5% YES, by May 31 at 39% YES.
- [Tue, 05 May 2026] Red Cross warns of renewed Iran attacks amid airspace closure concerns
- → The market for “Iran closes its airspace by May 8?” is currently priced at 15.5% YES, down from 20% over the past 24 hours. The market for “Iran clo

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 12.2%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** BREAKING_NEWS
- **Catalyst Strength:** 0.75

### Reasoning
Clear information asymmetry: March 17 report explicitly mentions 'Middle East Airspace Closures in April 2026' — directly before the May 21 deadline. Combined with January 2026 precedent (Iran airspace shutdown) and elevated US-Iran tensions (Fear index 27, deteriorating). The crowd is underpricing this longshot due to recency bias from quick re-openings and low historical base rate (2%), ignoring current elevated geopolitical conditions and imminent reported closures.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=8%<10%

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2025'})` → [Mon, 02 Mar 2026] Google News
[Tue, 20 Jan 2026] Why you shouldn’t cancel your flight as Iran strik
- `search_web({'query': 'Iran airspace closure March 2026'})` → [Fri, 15 May 2026] Google News
[Sun, 03 May 2026] Israeli airstrikes hit southern Lebanon, escalatin
- `search_web({'query': '"Iran airspace" closed 2026'})` → [Fri, 15 May 2026] Google News
[Wed, 14 Jan 2026] Israeli airstrikes hit southern Lebanon, escalatin

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*