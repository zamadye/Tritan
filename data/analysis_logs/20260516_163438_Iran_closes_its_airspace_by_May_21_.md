# Market Analysis — 2026-05-16 16:34 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 10.0%
- **Days Left:** 4
- **Volume 24h:** $77,757
- **Liquidity:** $50,030

## Statistical Prior
- **p_base:** 2.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,273 (-1.2% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,250 (-1.3% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 2.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** CROWD_BIAS
- **Catalyst Strength:** 0.15

### Reasoning
Iran airspace closure is priced at 10% vs 2% base rate without specific catalyst. This is a classic overpriced longshot in multi-outcome geopolitical market. No breaking news, no imminent military action, no diplomatic breakdown specific to this timeframe. Retail traders likely overpricing dramatic but unlikely scenario.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=8%<10%

## Tool Calls
- `search_web({'query': 'Iran airspace closed May 2025'})` → [Mon, 02 Mar 2026] Google News
[Tue, 03 Mar 2026] Why you shouldn’t cancel your flight as Iran strik
- `get_market_context({'keyword': 'Iran airspace'})` → No related markets found for 'Iran airspace'
- `search_web({'query': 'Iran US tensions May 2025 latest news'})` → [Tue, 24 Feb 2026] Google News
[Sat, 16 May 2026] A timeline of tensions over Iran's nuclear program
- `search_web({'query': 'Iran nuclear deal negotiations May 2025 airspace'})` → [Thu, 29 Jan 2026] Google News
[Sun, 30 Nov 2025] US-Iran tensions soar: What do both sides want? - 

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*