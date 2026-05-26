# Market Analysis — 2026-05-16 14:53 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 11.0%
- **Days Left:** 4
- **Volume 24h:** $75,900
- **Liquidity:** $50,863

## Statistical Prior
- **p_base:** 2.6%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 8.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,182 (-1.0% 24h) → neutral
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,139 (-1.2% 24h) → risk-OFF
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
- **p_true:** 12.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** BREAKING_NEWS
- **Catalyst Strength:** 0.75

### Reasoning
Active military strikes on Iranian territory are already occurring (US-Israel strikes on Iran reported). Multiple regional airspace closures already happening (Iraq, UAE restrictions). Historical pattern: when strikes hit Iranian territory, Iran has closed airspace defensively. The 11% price appears to lag the reality of an active conflict - the 3% base rate doesn't account for current military operations. With May 21 deadline and ongoing escalation, probability of Iranian airspace closure is significantly higher than current pricing suggests. Price gap of -8% from base rate suggests crowd hasn't fully priced in the active conflict scenario.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=8%<10%

## Tool Calls
- `search_web({'query': 'Iran airspace closed May 2025'})` → [Mon, 02 Mar 2026] Google News
[Mon, 30 Mar 2026] Why you shouldn’t cancel your flight as Iran strik
- `search_web({'query': 'Iran geopolitical tensions May 2025 airspace'})` → [Mon, 11 May 2026] Google News
[Tue, 03 Mar 2026] No Fly Zones: The Global Tensions Adding Hours To 
- `get_market_context({'keyword': 'Iran airspace'})` → No related markets found for 'Iran airspace'
- `search_web({'query': 'Iran US tensions nuclear negotiations May 2025'})` → [Tue, 24 Feb 2026] Google News
[Mon, 19 Jan 2026] A timeline of tensions over Iran's nuclear program
- `search_web({'query': 'Iran airspace closure threat Middle East escalation 2025'})` → [Sat, 28 Feb 2026] Google News
[Sat, 28 Feb 2026] Middle East escalation forces widespread flight su
- `get_market_context({'keyword': 'Iran war conflict'})` → No related markets found for 'Iran war conflict'
- `search_web({'query': 'Iran Israel war March 2026 airspace closure'})` → [Sun, 03 May 2026] Google News
[Mon, 16 Mar 2026] UAE lifts all air traffic restrictions introduced 
- `search_web({'query': 'Iran airspace closed today March 2026'})` → [Sun, 03 May 2026] Google News
[Mon, 02 Mar 2026] UAE lifts all air traffic restrictions introduced 

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*