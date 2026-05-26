# Market Analysis — 2026-05-16 16:00 UTC

## Market
- **Question:** Will Cameron Young win the 2026 PGA Championship?
- **Category:** sports
- **YES Price:** 9.3%
- **Days Left:** 1
- **Volume 24h:** $74,639
- **Liquidity:** $17,294

## Statistical Prior
- **p_base:** 3.2%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 6.1%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,203 (-1.2% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,132 (-1.3% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [MULTI-SOURCE NEWS] 1 sources for: cameron young 2026 championship
- [Bing News]

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 5.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Tournament is already in progress at Aronimink (Round 2→3). Cameron Young is NOT among the leaders (McNealy/Smalley lead). The 9% YES price appears to efficiently reflect his actual live position. No information asymmetry, no crowd bias to exploit, no catalyst. In-play market with real-time data eliminates the edge that pre-tournament longshot strategies target.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Cameron Young 2026 PGA Championship'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] 2026 PGA Championship Round 2 takeaways: Cameron Y
- `search_web({'query': 'Cameron Young golf 2025 2026 recent results'})` → [Thu, 14 May 2026] Google News
[Mon, 11 May 2026] Golf Leaderboards: PGA Tour, LPGA Tour, LIV Golf, 
- `search_web({'query': 'Cameron Young PGA Championship 2026 Round 2 leaderboard position'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Round 2 notebook: Tight leaderboard sets up dramat
- `search_web({'query': '2026 PGA Championship Aronimink leaderboard Round 2'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] PGA Championship leaderboard, Round 2 updates: Mav
- `search_web({'query': '"Cameron Young" PGA Championship 2026 score position Round 2'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Round 2 notebook: Tight leaderboard sets up dramat
- `get_sports_data({'sport': 'nba', 'team': 'Cameron Young golfer'})` → No injury data found for nba Cameron Young golfer

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*