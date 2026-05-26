# Market Analysis — 2026-05-17 13:23 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 12.0%
- **Days Left:** 3
- **Volume 24h:** $114,913
- **Liquidity:** $55,179

## Statistical Prior
- **p_base:** 3.0%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 9.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,248 (+0.5% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,206 (+0.4% 24h) → neutral
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
- **Confidence:** 50%
- **p_true:** 3.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL
- **Catalyst Strength:** 0.30

### Reasoning
Critical finding: Iran REOPENED its airspace on May 14-15 after a previous closure (Al Jazeera, May 14: 'Iran reopens airspace after closure to most flights amid US attack threats'). Currently operating with limited flights (IBT, May 17). Ceasefire fraying (Guardian, May 15: Trump calls Iran response 'totally unacceptable') but NOT yet collapsed. Market at 12% = 4x base rate (3%), indicating clear fear/narrative premium. P_true estimated ~6% — the reopening is a strong negative signal for re-closure, but geopolitical volatility provides some residual risk. Gap (~6%) falls below the 10% statistical edge threshold. No verifiable concrete evidence of imminent re-closure within 4 days. Situation too volatile for confident positioning despite identified crowd fear bias.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=9%<10%

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2025 news'})` → [Thu, 23 Apr 2026] Google News
[Mon, 02 Mar 2026] India extends airspace closure for Pakistan till M
- `search_web({'query': 'Iran airspace closure 2026 May 21 geopolitics'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Trump Says Iran Will Have 'A Very Bad Time' If Dea
- `search_web({'query': 'Iran airspace closure May 2026 military conflict'})` → [Sun, 17 May 2026] Google News
[Wed, 13 May 2026] Israeli military strikes on Doha, Tehran escalate 
- `search_web({'query': 'Iran airspace closed current status May 2026'})` → [Wed, 13 May 2026] Google News
[Sun, 03 May 2026] Middle East Flight Operations | Updates - SWISS Ne
- `search_web({'query': 'Iran military airspace closure flight restrictions May 2026'})` → [Mon, 11 May 2026] Google News
[Mon, 20 Apr 2026] No Fly Zones: The Global Tensions Adding Hours To 
- `search_web({'query': '"Iran airspace" closed OR closure 2026'})` → [Fri, 15 May 2026] Google News
[Thu, 15 Jan 2026] Israeli airstrikes hit southern Lebanon, escalatin
- `get_market_context({'keyword': 'Iran airspace'})` → No related markets found for 'Iran airspace'
- `search_web({'query': 'Al Jazeera Iran reopens airspace closure May 14 2026'})` → [Fri, 15 May 2026] Google News
[Fri, 01 May 2026] Finland ends drone alert amid regional fears of Uk
- `search_web({'query': 'Iran airspace status today May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] The Iran War Is Crippling One of the World’s Wealt
- `search_web({'query': 'Iran airspace reopening status flights restrictions May 2026'})` → [Tue, 05 May 2026] Google News
[Sun, 03 May 2026] UAE airspace fully reopens as flights set to retur
- `search_web({'query': 'Iran US ceasefire airspace May 2026'})` → [Sun, 10 May 2026] Google News
[Mon, 11 May 2026] US-Iran ceasefire under strain as Gulf states repo

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*