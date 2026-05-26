# Market Analysis — 2026-05-17 11:16 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 10.0%
- **Days Left:** 3
- **Volume 24h:** $110,860
- **Liquidity:** $70,650

## Statistical Prior
- **p_base:** 2.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,379 (+0.5% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,363 (+0.3% 24h) → neutral
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
- **p_true:** 2.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** CROWD_BIAS
- **Catalyst Strength:** 0.30

### Reasoning
Special longshot strategy applies: YES at 10% (3-15% range) with NO specific evidence of imminent airspace closure. Regional tensions exist but UAE already lifted restrictions (May 11), suggesting de-escalation. Iran closing its own airspace is distinct from other nations' airspace restrictions over Iranian territory. No breaking news or unreported catalyst justifies 5x base rate pricing (10% vs 2%). Crowd overpricing longshot in geopolitical market without imminent trigger.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=8%<10%

## Tool Calls
- `search_web({'query': 'Iran airspace closure news May 2024 2025'})` → [Wed, 13 May 2026] Google News
[Sat, 16 May 2026] Middle East Flight Operations | Updates - SWISS Ne
- `search_web({'query': '"Iran closes its airspace" May 21 prediction market'})` → [Fri, 08 May 2026] Google News
[Thu, 07 May 2026] Iran Airspace Closure Bets Surge - StartupHub.ai
[
- `search_web({'query': 'Iran airspace closure status May 16 2026'})` → [Sat, 16 May 2026] Google News
[Sun, 03 May 2026] Middle East Air Travel Chaos Escalates as Emirates

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*