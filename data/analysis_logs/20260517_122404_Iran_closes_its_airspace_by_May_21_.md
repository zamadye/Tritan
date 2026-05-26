# Market Analysis — 2026-05-17 12:24 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 11.0%
- **Days Left:** 3
- **Volume 24h:** $110,311
- **Liquidity:** $79,920

## Statistical Prior
- **p_base:** 2.6%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 8.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,404 (+0.6% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,334 (+0.5% 24h) → neutral
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
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 1.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** CROWD_BIAS
- **Catalyst Strength:** 0.68

### Reasoning
Multi-outcome geopolitical market with YES at 11% longshot price, no specific breaking news or unreported data indicates imminent airspace closure. Crowd systematically overprices rare geopolitical events; base rate of 3% suggests true probability closer to 5%. Fear sentiment elevated but no catalyst to trigger closure by May 21.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=8%<10%

## Tool Calls
- `search_web({'query': 'Iran airspace closure 2025 latest news'})` → [Thu, 15 Jan 2026] Google News
[Sat, 28 Feb 2026] Iran temporarily closes airspace with US attack 'i
- `search_web({'query': 'Iran US tensions May 2025 airspace military'})` → [Thu, 29 Jan 2026] Google News
[Wed, 04 Feb 2026] US-Iran tensions soar: What do both sides want? - 
- `get_market_context({'keyword': 'Iran airspace closure'})` → No related markets found for 'Iran airspace closure'
- `search_web({'query': 'Iran airspace closure May 2025 geopolitical tensions'})` → [Mon, 11 May 2026] Google News
[Tue, 03 Mar 2026] No Fly Zones: The Global Tensions Adding Hours To 
- `search_web({'query': 'Iran flight bans airspace restrictions current status'})` → [Tue, 17 Mar 2026] Google News
[Tue, 10 Mar 2026] What Travelers Need to Know About Middle East Flig
- `search_web({'query': 'Iran US military tensions May 15 2025'})` → [Wed, 06 May 2026] Google News
[Tue, 24 Feb 2026] Collection: Iran, Israel and the United States at 
- `search_web({'query': 'Iran airspace closed today 2025'})` → [Thu, 15 Jan 2026] Google News
[Tue, 03 Mar 2026] Iran temporarily closes airspace with US attack 'i

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*