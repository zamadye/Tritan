# Market Analysis — 2026-05-16 17:08 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 10.0%
- **Days Left:** 4
- **Volume 24h:** $81,018
- **Liquidity:** $45,594

## Statistical Prior
- **p_base:** 2.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,188 (-1.3% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,231 (-1.3% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 1.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** CROWD_BIAS
- **Catalyst Strength:** 0.60

### Reasoning
Special longshot strategy applies: YES at 10% (3-15% range) with NO specific evidence of imminent Iran airspace closure. News search found June 2025 airspace closure, not May deadline. Market is overpriced vs 2% base rate by 8 points - retail overpricing longshot due to geopolitical fear narrative. Fear & Greed at 31 (Fear) and BTC risk-off may be inflating anxiety-driven bets. No breaking news (<2h) or unreported data. Geopolitik pattern (87% WR) doesn't apply without catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=8%<10%

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2025 news'})` → [Thu, 23 Apr 2026] Google News
[Mon, 02 Mar 2026] India extends airspace closure for Pakistan till M
- `search_web({'query': '"Iran closes airspace" 2025 geopolitical'})` → [Wed, 14 Jan 2026] Google News
[Wed, 14 Jan 2026] U.S. Embassy in Qatar Issues Rare Security Alert A
- `get_market_context({'keyword': 'Iran airspace closure'})` → No related markets found for 'Iran airspace closure'

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*