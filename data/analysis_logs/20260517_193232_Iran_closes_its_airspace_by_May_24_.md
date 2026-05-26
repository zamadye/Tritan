# Market Analysis — 2026-05-17 19:32 UTC

## Market
- **Question:** Iran closes its airspace by May 24?
- **Category:** geopolitik
- **YES Price:** 30.0%
- **Days Left:** 6
- **Volume 24h:** $261,708
- **Liquidity:** $60,529

## Statistical Prior
- **p_base:** 14.5%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 15.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,215 (+0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,193 (-0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
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
- **p_true:** 10.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL_STATUS_QUO
- **Catalyst Strength:** 0.60

### Reasoning
Iran reopened airspace May 14-15, ceasefire holding, no evidence of imminent new closure. YES at 30% overpriced vs. 15% base rate. Similar market already decided NO with 65% confidence.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2025'})` → [Mon, 27 Apr 2026] Google News
[Mon, 02 Mar 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Iran airspace closed May 24 2025 prediction'})` → [Mon, 27 Apr 2026] Google News
[Fri, 08 May 2026] Middle East Airspace – Current Operational Picture
- `get_market_context({'keyword': 'Iran airspace'})` → No related markets found for 'Iran airspace'
- `search_web({'query': 'Iran airspace open ceasefire May 2025 latest news'})` → [Thu, 09 Apr 2026] Google News
[Wed, 08 Apr 2026] Iran accuses U.S. of violating ceasefire as Israel
- `search_web({'query': 'Iran airspace status May 2025 geopolitical situation'})` → [Mon, 09 Mar 2026] Google News
[Wed, 18 Feb 2026] 7th U.S. service member dies in war with Iran; Moj

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*