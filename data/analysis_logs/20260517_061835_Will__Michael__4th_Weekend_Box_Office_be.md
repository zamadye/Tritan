# Market Analysis — 2026-05-17 06:18 UTC

## Market
- **Question:** Will "Michael" 4th Weekend Box Office be greater than 25m?
- **Category:** other
- **YES Price:** 60.0%
- **Days Left:** 1
- **Volume 24h:** $41,845
- **Liquidity:** $3,929

## Statistical Prior
- **p_base:** 44.6%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 15.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,156 (-0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,080 (-1.1% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [MULTI-SOURCE NEWS] 2 sources for: "michael" weekend office greater than
- [Bing News]

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 44.6%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 0%<52%

## Tool Calls
- `search_web({'query': 'Michael Jackson biopic 4th weekend box office 2025'})` → [Fri, 15 May 2026] Google News
[Sun, 26 Apr 2026] Michael North America Box Office: How Much More It
- `get_market_context({'keyword': 'Michael box office'})` → No related markets found for 'Michael box office'
- `search_web({'query': '"Michael" movie box office week 3 week 4 drop 2026'})` → [Wed, 13 May 2026] Google News
[Tue, 12 May 2026] Weekend Preview: Coin Flip for the Top Spot as DEV
- `search_web({'query': 'Michael Jackson movie box office total gross domestic 2026'})` → [Sat, 16 May 2026] Google News
[Mon, 11 May 2026] ‘Michael’ Has Better Dance Moves Than ‘The Devil’ 
- `search_web({'query': '"Michael" 4th weekend box office $27 million May 2026'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] ‘Michael’ Has Better Dance Moves Than ‘The Devil’ 

## Outcome
**❌ LOSS** | P&L: $-0.17 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*