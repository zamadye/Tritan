# Market Analysis — 2026-05-16 15:06 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 11.0%
- **Days Left:** 4
- **Volume 24h:** $75,900
- **Liquidity:** $50,273

## Statistical Prior
- **p_base:** 2.6%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 8.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,093 (-1.4% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,173 (-1.1% 24h) → risk-OFF
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
- **Catalyst Strength:** 0.65

### Reasoning
Classic longshot overpricing pattern: YES at 11% vs 3% base rate with no specific catalyst for Iran closing its OWN airspace. Recent news shows regional escalation (UAE restricting airspace after Iranian attacks, Israeli strikes in Lebanon), but this involves OTHER countries reacting to Iran's offensive operations—not Iran closing its own airspace. Crowd is applying narrative bias from general Iran-Israel conflict tension to a specific outcome that has no direct evidence. The 8-point premium above base rate reflects retail overpricing of a longshot based on 'something dramatic might happen' rather than specific indicators. No information gap identified—no leaked intel, no diplomatic signals, no military posture changes suggesting imminent airspace closure. Framework trigger: longshot at 3-15% with no specific evidence favors BET_NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=8%<10%

## Tool Calls
- `search_web({'query': 'Iran closes airspace May 21 2025'})` → [Fri, 22 Aug 2025] Google News
[Sun, 22 Jun 2025] Iran briefly closes western airspace for military 
- `search_web({'query': '"Iran airspace" "May 21" 2026'})` → [Thu, 23 Apr 2026] Google News
[Thu, 15 Jan 2026] U.S. State Department urges citizens to leave Iran
- `search_web({'query': 'Iran airspace closure 2026'})` → [Fri, 15 May 2026] Google News
[Tue, 05 May 2026] Israeli airstrikes hit southern Lebanon, escalatin

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*