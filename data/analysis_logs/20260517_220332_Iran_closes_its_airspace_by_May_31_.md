# Market Analysis — 2026-05-17 22:03 UTC

## Market
- **Question:** Iran closes its airspace by May 31?
- **Category:** geopolitik
- **YES Price:** 41.0%
- **Days Left:** 13
- **Volume 24h:** $184,234
- **Liquidity:** $141,736

## Statistical Prior
- **p_base:** 26.0%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 15.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,363 (+0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,333 (+0.2% 24h) → neutral
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
- **p_true:** 18.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** CEASEFIRE_FRAGILITY
- **Catalyst Strength:** 0.30

### Reasoning
Iran reopened airspace May 14-15 (just days ago), no concrete evidence of imminent new closure. YES at 41% is overpriced vs base rate 26% and historical pattern showing 40-50% entry range has only 9% WR. While ceasefire is fragile ('life support'), no direct catalyst for closure in 13-day window. Fear sentiment likely inflating YES price.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2024'})` → [Wed, 13 May 2026] Google News
[Sat, 02 May 2026] Middle East Flight Operations | Updates - SWISS Ne
- `search_web({'query': 'Iran airspace reopening May 2024'})` → [Wed, 13 May 2026] Google News
[Thu, 07 May 2026] Middle East Flight Operations | Updates - SWISS Ne
- `search_web({'query': 'Iran airspace status today May 2026'})` → [Mon, 27 Apr 2026] Google News
[Sun, 17 May 2026] Middle East Airspace – Current Operational Picture
- `get_market_context({'keyword': 'Iran airspace closure'})` → No related markets found for 'Iran airspace closure'
- `search_web({'query': '"Iran airspace" May 2026 ceasefire'})` → [Wed, 13 May 2026] Google News
[Sun, 03 May 2026] Iran threatens US retaliation as Trump considers e
- `get_market_context({'keyword': 'Iran'})` → [YES=50% vol=$2,310,408] Will Reza Pahlavi lead Iran in 2026?
- `search_web({'query': 'Iran US ceasefire status May 2026 latest'})` → [Sun, 17 May 2026] Google News
[Mon, 11 May 2026] Trump Says 'Clock Is Ticking' For Iran - Radio Fre
- `search_web({'query': 'Iran airspace threat escalation May 2026'})` → [Tue, 07 Apr 2026] Google News
[Mon, 16 Mar 2026] Middle East Conflict: Situational Updates and Impl
- `search_web({'query': '"Iran airspace" closed May 18 2026'})` → [Fri, 15 May 2026] Google News
[Sat, 18 Apr 2026] Israel, US consider renewed military attacks on Ir
- `search_web({'query': 'Iran ceasefire collapse airspace closure threat 2026'})` → [Mon, 04 May 2026] Google News
[Mon, 27 Apr 2026] Iran attacks UAE; U.S. says it sank boats in Strai

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*