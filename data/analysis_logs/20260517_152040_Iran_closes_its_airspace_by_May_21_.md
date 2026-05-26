# Market Analysis — 2026-05-17 15:20 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 10.0%
- **Days Left:** 3
- **Volume 24h:** $151,762
- **Liquidity:** $55,908

## Statistical Prior
- **p_base:** 2.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,071 (-0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,936 (-0.2% 24h) → neutral
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
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Iran just reopened airspace May 14-15; ceasefire holding; no evidence of imminent new closure; market slightly overpriced (10% vs ~6% true prob) but geopolitical tail risk + short 3-day window = insufficient conviction for BET_NO; past decisions correctly identified low confidence

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2025 latest news'})` → [Thu, 23 Apr 2026] Google News
[Mon, 02 Mar 2026] India extends airspace closure for Pakistan till M
- `search_web({'query': 'Iran airspace closure May 21 2025'})` → [Wed, 13 May 2026] Google News
[Fri, 24 Apr 2026] Middle East Flight Operations | Updates - SWISS Ne
- `search_web({'query': 'Iran airspace closed May 2025 conflict tensions'})` → [Thu, 29 Jan 2026] Google News
[Fri, 13 Jun 2025] US-Iran tensions soar: What do both sides want? - 
- `get_market_context({'keyword': 'Iran airspace'})` → No related markets found for 'Iran airspace'
- `get_market_context({'keyword': 'Iran'})` → [YES=50% vol=$1,757,544] Will Trump say "Iran" during events with Xi Jinping?
- `search_web({'query': 'Iran airspace closure today May 2025'})` → [Wed, 13 May 2026] Google News
[Mon, 30 Mar 2026] Middle East Flight Operations | Updates - SWISS Ne
- `search_web({'query': 'Iran war May 2025 latest news'})` → [Wed, 13 May 2026] Google News
[Thu, 23 Apr 2026] UK inflation: What is the rate and why are prices 

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*