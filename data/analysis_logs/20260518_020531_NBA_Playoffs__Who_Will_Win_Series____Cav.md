# Market Analysis — 2026-05-18 02:05 UTC

## Market
- **Question:** NBA Playoffs: Who Will Win Series? - Cavaliers vs. Pistons 
- **Category:** sports
- **YES Price:** 91.0%
- **Days Left:** 3
- **Volume 24h:** $98,267
- **Liquidity:** $9,731

## Statistical Prior
- **p_base:** 97.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 6.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,046 (-0.9% 24h) → neutral
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,077 (-0.9% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- CLE @ DET | In Progress | Detroit Pistons(home) 60-22 score:69 vs Cleveland Cavaliers(away) 52-30 score:92
- [SPORTS] Injuries:
- ?: Keshon Gilbert — Out (Surgery)
- ?: Jock Landale — Out (Sprain)
- ?: Jayson Tatum — Out (Soreness)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: playoffs: series cavaliers pistons
- [Bing News]
- [Sun, 17 May 2026] playoffs: series cavaliers pistons
- → What channel is Detroit Pistons vs Cleveland Cavaliers on today? How to watch, stream NBA playoffs Game 7 on TV, streaming on Sunday, May 17, 2026.
- [Sun, 17 May 2026] What channel is Cavaliers vs Pistons on? How to watch Game 7 Sunday
- → Live updates from Little Caesars Arena as the Detroit Pistons and Cleveland Cavaliers battle in Game 7 for a trip to the Eastern Conference finals.
- [Sun, 17 May 2026] Live Updates From Game 7 As Pistons, Cavaliers Battle for Spot in the Eastern Conference Finals
- → The Cleveland Cavaliers play against the Detroit Pistons in game 7 of their NBA Playoff series today. The series finale is scheduled to begin at 7 p

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 92.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 0%<52%

## Tool Calls
- `get_sports_data({'sport': 'nba', 'team': 'cavaliers'})` → INJURY [cleveland cavaliers] Larry Nance Jr. (F): Out
- `get_sports_data({'sport': 'nba', 'team': 'pistons'})` → No injury data found for nba pistons
- `get_odds({'sport': 'basketball_nba'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Cavaliers vs Pistons NBA playoffs series 2025'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Starting 5: Cavs-Pistons Game 7 tips on Prime, MVP
- `search_web({'query': 'Cavaliers Pistons Game 7 odds 2025'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Cavaliers vs. Pistons Game 7 Pick: 2025-26 NBA Pla
- `search_web({'query': '"Cavaliers vs Pistons" Game 7 injuries 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Cavaliers vs Pistons Prediction, Picks &amp; Odds 
- `get_market_context({'keyword': 'Cavaliers Pistons NBA playoffs'})` → No related markets found for 'Cavaliers Pistons NBA playoffs'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*