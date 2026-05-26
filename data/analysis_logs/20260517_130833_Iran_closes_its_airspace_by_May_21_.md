# Market Analysis — 2026-05-17 13:08 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 12.0%
- **Days Left:** 3
- **Volume 24h:** $114,777
- **Liquidity:** $63,689

## Statistical Prior
- **p_base:** 3.0%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 9.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,374 (+0.4% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,287 (+0.4% 24h) → neutral
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
- **p_true:** 3.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=9%<10%

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2025'})` → [Thu, 23 Apr 2026] Google News
[Mon, 02 Mar 2026] India extends airspace closure for Pakistan till M
- `search_web({'query': 'Iran airspace ban flights 2025'})` → [Thu, 14 May 2026] Google News
[Wed, 11 Mar 2026] As Iran war jolts Air India, Lufthansa and Cathay 
- `get_market_context({'keyword': 'Iran airspace closure'})` → No related markets found for 'Iran airspace closure'
- `search_web({'query': 'Iran airspace status April 2025 flights'})` → [Sun, 01 Mar 2026] Google News
[Sat, 28 Feb 2026] Air fares could rise if Iran conflict lingers as c
- `search_web({'query': 'Iran US tensions airspace closure risk 2025'})` → [Tue, 20 Jan 2026] Google News
[Thu, 15 Jan 2026] Crisis in Iran: Elevated Airspace Risk – Internati
- `search_web({'query': '"Iran" "airspace" "closed" OR "open" April 2026'})` → [Fri, 15 May 2026] Google News
[Sat, 18 Apr 2026] Jordan Airspace Status After US-Iran Ceasefire: Wh
- `search_web({'query': 'Iran war US strikes airspace May 2026'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] The strike that changed the geometry of war - Al J
- `search_web({'query': 'Iran airspace closure status today April 2026'})` → [Wed, 13 May 2026] Google News
[Mon, 11 May 2026] Middle East Flight Operations | Updates - SWISS Ne
- `search_web({'query': 'US Iran ceasefire status April 2026'})` → [Tue, 12 May 2026] Google News
[Wed, 22 Apr 2026] Pakistan scrambles to salvage US-Iran diplomacy as
- `search_web({'query': 'Iran airspace reopening partial April 24 2026'})` → [Fri, 24 Apr 2026] Google News
[Sat, 18 Apr 2026] Kuwait reopens airspace for first time in two mont
- `search_web({'query': 'Iran ceasefire collapse airspace closure risk May 2026'})` → [Sun, 03 May 2026] Google News
[Fri, 15 May 2026] US blockade cripples Iranian economy despite fragi

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*