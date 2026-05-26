# Market Analysis — 2026-05-21 03:25 UTC

## Market
- **Question:** Iran closes its airspace by May 27?
- **Category:** geopolitik
- **YES Price:** 25.0%
- **Days Left:** 5
- **Volume 24h:** $60,347
- **Liquidity:** $43,371

## Statistical Prior
- **p_base:** 10.4%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 14.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,892 (+1.8% 24h) → risk-ON
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,914 (+1.7% 24h) → risk-ON
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%
- → Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls
- → Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally
- → Iran military strike → oil spike → global inflation → Fed hawkish

### Multi-Source
- [MULTI-SOURCE NEWS] 4 sources for: iran closes airspace
- [Bing News]
- [Mon, 18 May 2026] iran closes airspace
- → Trump discusses resuming combat operations against Iran. Iran closes its airspace by May 31 at 39.5% YES; US invasion of Iran before 2027 at 31.5% Y
- [Thu, 15 Jan 2026] Trump discusses resuming combat operations against Iran with security team
- → TEMPO.CO, Jakarta - Iran temporarily closed its airspace to all flights except international flights to and from Iran with official permission on We
- [Wed, 20 May 2026] Iran Closes Airspace Amid Rising Protests and Regional Tensions
- → Congress advances a resolution to limit Trump's war powers on Iran. War declaration by December 31, 2026 at 6.5% YES.

## LLM Decision
- **Action:** NO
- **Confidence:** 63%
- **p_true:** 4.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL
- **Catalyst Strength:** 0.35

### Reasoning
Market overpriced at 25% vs 10% base rate with -15% gap. No direct evidence Iran will close airspace by May 27; news shows regional conflict but airlines resuming flights suggests openings not closures. Geopolitical category has 9% WR historically. 5 days remaining with no imminent catalyst. True probability estimated at ~13%, making NO the value bet.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Iran airspace closure 2025 May restrictions'})` → [Mon, 11 May 2026] Google News
[Mon, 27 Apr 2026] Middle East - The Latest News on Mobility and Trav
- `search_web({'query': 'Iran airspace closed to flights today 2026'})` → [Mon, 27 Apr 2026] Google News
[Mon, 18 May 2026] Middle East Airspace – Current Operational Picture
- `get_market_context({'keyword': 'Iran airspace'})` → No related markets found for 'Iran airspace'
- `get_market_context({'keyword': 'Iran geopolitical'})` → No related markets found for 'Iran geopolitical'
- `get_market_context({'keyword': 'Iran war'})` → No related markets found for 'Iran war'
- `get_market_context({'keyword': 'Iran'})` → [YES=50% vol=$2,848,574] Will Trump say "Iran" during events with Xi Jinping?
- `get_market_context({'keyword': 'Middle East conflict'})` → No related markets found for 'Middle East conflict'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*