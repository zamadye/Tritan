# Market Analysis — 2026-05-16 15:53 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 10.0%
- **Days Left:** 4
- **Volume 24h:** $77,751
- **Liquidity:** $55,282

## Statistical Prior
- **p_base:** 2.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,201 (-1.2% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,206 (-1.2% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Google News RSS
- 6 articles found:
- [NewsAPI] Six dead as Russia launches over 800 drones at Ukraine: Volodymyr Zelenskyy accuses Russia of attempting to ov
- [NewsAPI] Expensive jet fuel is reshaping the global aviation map: Route cuts and rising t: Travelers are paying a high 
- [NewsAPI] Israeli strikes on Iranian universities escalate conflict, impact peace deal pro: The escalation reduces peace
- [NewsAPI] Iran closes Strait of Hormuz amid US-Israel conflict escalation: The closure of the Strait of Hormuz exacerbat

## LLM Decision
- **Action:** YES
- **Confidence:** 65%
- **p_true:** 18.2%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** BREAKING_NEWS
- **Catalyst Strength:** 0.90

### Reasoning
Active US-Iran war creates fundamentally different conditions than the 2% base rate (peacetime). Regional airspace already disrupted—Spain closed airspace to US planes, airlines suspending Middle East flights. Iran closing its own airspace during active conflict is standard wartime procedure. Market at 10% dramatically underweights ongoing military conflict.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=8%<10%

## Tool Calls
- `search_web({'query': 'Iran airspace closure 2025'})` → [2026-05-15] Singapore Airlines defends its decision to invest in loss-making Air India: ‘We know th
- `search_web({'query': 'Iran US tensions May 2025'})` → [2026-05-15] Xi-Trump Summit Disappoints as Oil Bulls Regain Momentum — Oil prices surged $7 this we
- `get_market_context({'keyword': 'Iran airspace'})` → No related markets found for 'Iran airspace'
- `search_web({'query': 'Iran airspace closed war US military 2026'})` → [2026-05-15] Baku on the Edge of the Abyss: Why a War with Iran Could Destroy Azerbaijan — In March 
- `search_web({'query': 'Iran airspace restrictions flights May 2026'})` → [2026-05-12] Has Air India cancelled all international flights until July 2026? Here’s the truth beh
- `search_web({'query': 'Iran closed airspace war 2026 flights banned'})` → [Mon, 30 Mar 2026] Google News
[Mon, 11 May 2026] Spain closes airspace to US planes involved in war
- `search_web({'query': 'Iran airspace status today May 15 2026'})` → [2026-05-15] Xi’s threat to Trump cements Taiwan as top US-China risk — Xi’s assertion that interfer

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*