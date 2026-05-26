# Market Analysis — 2026-05-16 16:46 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 10.0%
- **Days Left:** 4
- **Volume 24h:** $77,756
- **Liquidity:** $49,149

## Statistical Prior
- **p_base:** 2.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,233 (-1.3% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,123 (-1.4% 24h) → risk-OFF
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
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
No breaking news or imminent catalyst for Iran to close airspace by May 21. Historical base rate is 2% (n=135), but market is pricing at 10% - a 5x overvaluation. This appears to be crowd bias: retail overpricing a dramatic but unlikely geopolitical longshot. Iran only closes airspace during active conflicts, and no such trigger exists currently.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=8%<10%

## Tool Calls
- `search_web({'query': 'Iran closes airspace May 2025 news'})` → [Mon, 30 Mar 2026] Google News
[Mon, 02 Mar 2026] Spain closes airspace to aircraft involved in Iran
- `search_web({'query': '"Iran airspace" closure May 21 2025'})` → [Fri, 08 May 2026] Google News
[Sat, 02 May 2026] Iran Airspace Closure Bets Surge - StartupHub.ai
[
- `search_web({'query': '"Iran Airspace Closure Bets Surge" May 2026'})` → [Fri, 08 May 2026] Google News
[] Iran Airspace Closure Bets Surge - StartupHub.ai

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*