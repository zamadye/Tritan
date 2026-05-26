# Market Analysis — 2026-05-17 14:04 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 9.0%
- **Days Left:** 3
- **Volume 24h:** $148,624
- **Liquidity:** $52,665

## Statistical Prior
- **p_base:** 1.8%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.1%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,206 (+0.3% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,131 (+0.3% 24h) → neutral
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
- **Confidence:** 40%
- **p_true:** 1.8%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.05

### Reasoning
No concrete evidence of imminent Iran airspace closure. Iran just reopened airspace (May 14-15). UAE fully lifted restrictions (May 11). 9% YES appears overpriced vs 2% base rate, but -7% gap insufficient (<10% threshold). Only 3 days left with no breaking catalyst. Market pricing reflects speculation, not verifiable edge. Geopolitik pattern strong (87% WR) but no actionable trade here.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 40%<52%

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2024'})` → [Wed, 13 May 2026] Google News
[Mon, 11 May 2026] Middle East Flight Operations | Updates - SWISS Ne
- `search_web({'query': 'Iran airspace open or closed May 2026'})` → [Tue, 05 May 2026] Google News
[Sun, 03 May 2026] UAE airspace fully reopens as flights set to retur
- `search_web({'query': '"Iran airspace" closed May 21 2026'})` → [Mon, 11 May 2026] Google News
[Sun, 03 May 2026] Dubai and Middle East flight disruption: the lates
- `search_web({'query': 'Iran airspace closure threat May 2026 news'})` → [Thu, 07 May 2026] Google News
[Wed, 06 May 2026] Trump shelved ‘Project Freedom’ after Saudis refus
- `search_web({'query': 'Iran airspace status today May 18 2026'})` → [Wed, 13 May 2026] Google News
[Sat, 18 Apr 2026] Middle East Flight Operations | Updates - SWISS Ne
- `get_market_context({'keyword': 'Iran airspace'})` → No related markets found for 'Iran airspace'
- `search_web({'query': 'Iran airspace closure reopening May 2026 latest'})` → [Tue, 05 May 2026] Google News
[Sun, 03 May 2026] UAE airspace fully reopens as flights set to retur

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*