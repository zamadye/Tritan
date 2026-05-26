# Market Analysis — 2026-05-17 14:15 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 9.0%
- **Days Left:** 3
- **Volume 24h:** $148,087
- **Liquidity:** $54,644

## Statistical Prior
- **p_base:** 1.8%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.1%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,093 (+0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,051 (+0.2% 24h) → neutral
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
- [Tue, 24 Mar 2026] Red Cross warns of renewed Iran attacks amid airspace closure concerns
- → With flight schedules and route networks being regularly updated, here's the latest news for passengers facing Dubai and Middle East flight disrupti

## LLM Decision
- **Action:** SKIP
- **Confidence:** 40%
- **p_true:** 1.8%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
No concrete evidence of imminent Iran airspace closure; Iran just reopened airspace (May 14-15); market pricing low; past decisions skip due to lack of evidence.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 40%<52%

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2025'})` → [Thu, 23 Apr 2026] Google News
[Mon, 02 Mar 2026] India extends airspace closure for Pakistan till M
- `search_web({'query': 'Iran reopens airspace May 2025'})` → [Mon, 30 Mar 2026] Google News
[Sun, 01 Mar 2026] Spain closes airspace to aircraft involved in Iran
- `search_web({'query': 'Iran airspace reopened May 14 2025'})` → [Sat, 28 Feb 2026] Google News
[Wed, 04 Mar 2026] US-Iran strikes: What flight cancellations mean fo
- `search_web({'query': 'Iran airspace closure today 2025'})` → [Thu, 15 Jan 2026] Google News
[Sun, 01 Mar 2026] Iran temporarily closes airspace with US attack 'i
- `search_web({'query': 'Iran airspace closure April 2026'})` → [Wed, 13 May 2026] Google News
[Thu, 30 Apr 2026] Middle East Flight Operations | Updates - SWISS Ne
- `search_web({'query': '"Iran airspace closed" April 2026'})` → [Sat, 25 Apr 2026] Google News
[Tue, 07 Apr 2026] 10 Powerful Signs of Hopeful Recovery: Iran Resume
- `search_web({'query': 'Iran US conflict April 2026'})` → [Sat, 16 May 2026] Google News
[Fri, 15 May 2026] Iran warns of readiness for war and economic costs

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*