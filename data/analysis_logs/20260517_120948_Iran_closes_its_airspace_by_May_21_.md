# Market Analysis — 2026-05-17 12:09 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 11.0%
- **Days Left:** 3
- **Volume 24h:** $110,793
- **Liquidity:** $77,274

## Statistical Prior
- **p_base:** 2.6%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 8.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,381 (+0.4% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,375 (+0.4% 24h) → neutral
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
- **Confidence:** 0%
- **p_true:** 2.6%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=8%<10%

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2025'})` → [Mon, 02 Mar 2026] Google News
[Tue, 20 Jan 2026] Why you shouldn’t cancel your flight as Iran strik
- `search_web({'query': 'Iran Middle East airspace restrictions latest news'})` → [Thu, 14 May 2026] Google News
[Thu, 14 May 2026] Iran war fallout forces Singapore Airlines-backed 
- `get_market_context({'keyword': 'Iran airspace'})` → No related markets found for 'Iran airspace'
- `search_web({'query': 'Iran airspace closure 2025 latest developments'})` → [Thu, 15 Jan 2026] Google News
[Wed, 01 Apr 2026] Iran temporarily closes airspace with US attack 'i
- `search_web({'query': 'Iran US tensions airspace closure risk'})` → [Sun, 03 May 2026] Google News
[Mon, 04 May 2026] Iran’s clerical divisions highlight airspace closu
- `search_web({'query': 'Iran airspace closure May 2025 news'})` → [Thu, 23 Apr 2026] Google News
[Mon, 02 Mar 2026] India extends airspace closure for Pakistan till M
- `search_web({'query': 'Iran tensions May 2025 Middle East'})` → [Tue, 24 Feb 2026] Google News
[Fri, 06 Mar 2026] A timeline of tensions over Iran's nuclear program

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*