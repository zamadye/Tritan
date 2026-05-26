# Market Analysis — 2026-05-17 14:40 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 10.0%
- **Days Left:** 3
- **Volume 24h:** $153,164
- **Liquidity:** $50,054

## Statistical Prior
- **p_base:** 2.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,029 (-0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,965 (-0.2% 24h) → neutral
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
- **Confidence:** 45%
- **p_true:** 2.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL
- **Catalyst Strength:** 0.25

### Reasoning
Iran just REOPENED airspace May 14-15 per multiple sources; ceasefire holding (though Trump called it 'life support'); no concrete evidence of imminent new strikes or escalation that would force reclosure within 3 days. Base rate 2% vs 10% price suggests slight crowd overpricing, but edge is too small (~5-6 cents) and tail risk from sudden geopolitical escalation makes bet unattractive. Two prior decisions also SKIPped at 40% confidence. No new catalyst identified to justify entry.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2025'})` → [Thu, 23 Apr 2026] Google News
[Mon, 02 Mar 2026] India extends airspace closure for Pakistan till M
- `search_web({'query': 'Iran airspace closed flights May 2026'})` → [Fri, 15 May 2026] Google News
[Wed, 13 May 2026] Airlines cancel flights in response to Middle East
- `search_web({'query': 'Iran military conflict May 2026 latest news'})` → [Thu, 14 May 2026] Google News
[Fri, 15 May 2026] Iran Update Special Report, May 13, 2026 - Institu
- `search_web({'query': 'Iran airspace reopened May 15 2026'})` → [Sun, 10 May 2026] Google News
[Thu, 09 Apr 2026] Iran responds to U.S. ceasefire proposal, saying t
- `get_market_context({'keyword': 'Iran airspace'})` → No related markets found for 'Iran airspace'
- `search_web({'query': '"Iran" "airspace" "May 2026" ceasefire status update'})` → [Fri, 15 May 2026] Google News
[Mon, 11 May 2026] Middle East Travel Update (May 2026): Iran-Israel 
- `search_web({'query': 'Iran war ceasefire agreement May 2026 latest'})` → [Tue, 12 May 2026] Google News
[Thu, 14 May 2026] Iran War Updates: Trump Says Iran Must Make Deal o
- `search_web({'query': 'Iran military escalation May 18 2026'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Trump's 'Calm Before The Storm' Post Sparks Renewe
- `search_web({'query': 'Iran airspace closure threat May 2026'})` → [Sun, 03 May 2026] Google News
[Thu, 07 May 2026] Iran’s clerical divisions highlight airspace closu

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*