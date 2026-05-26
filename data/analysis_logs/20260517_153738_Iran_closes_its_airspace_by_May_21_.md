# Market Analysis — 2026-05-17 15:37 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 12.0%
- **Days Left:** 3
- **Volume 24h:** $155,887
- **Liquidity:** $54,253

## Statistical Prior
- **p_base:** 3.0%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 9.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,992 (-0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,006 (-0.2% 24h) → neutral
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
- **Catalyst Type:** RECENT_REOPENING
- **Catalyst Strength:** 0.70

### Reasoning
Iran REOPENED airspace May 14-15 (3-4 days ago) and ceasefire is holding with no evidence of imminent new closure. Only 3 days left until May 21. Market overpricing YES at 12% vs base rate 3% due to fear sentiment (Fear&Greed=27), but direct evidence points to airspace remaining open. Strong case for NO given recent reopening makes immediate re-closure highly unlikely.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2024 news'})` → [Wed, 13 May 2026] Google News
[Mon, 11 May 2026] Middle East Flight Operations | Updates - SWISS Ne
- `search_web({'query': 'Iran closes airspace recent developments'})` → [Mon, 27 Apr 2026] Google News
[Sun, 03 May 2026] Middle East Airspace – Current Operational Picture
- `get_market_context({'keyword': 'Iran airspace closure'})` → No related markets found for 'Iran airspace closure'
- `search_web({'query': 'Iran airspace status today 2025'})` → [Mon, 27 Apr 2026] Google News
[Mon, 02 Mar 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Iran Israel conflict May 2025 ceasefire'})` → [Fri, 15 May 2026] Google News
[Wed, 08 Apr 2026] Israel-Hamas War (Gaza Conflict) | Explanation, Su
- `search_web({'query': 'Iran airspace May 18 2025'})` → [Wed, 13 May 2026] Google News
[Wed, 18 Jun 2025] Middle East Flight Operations | Updates - SWISS Ne
- `search_web({'query': 'Iran Israel war May 2025 latest'})` → [Fri, 15 May 2026] Google News
[Wed, 06 May 2026] Israel-Hamas War (Gaza Conflict) | Explanation, Su
- `search_web({'query': 'Iran airspace reopening May 14 2025'})` → [Mon, 27 Apr 2026] Google News
[Sat, 28 Feb 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Iran Israel ceasefire May 2025 latest news'})` → [Sat, 16 May 2026] Google News
[Tue, 10 Mar 2026] BBC Learning English - Learning English from the N
- `get_market_context({'keyword': 'Iran'})` → [YES=50% vol=$1,736,761] Will Trump say "Iran" during events with Xi Jinping?
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $78,004.00 | 24h: -0.24%

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*