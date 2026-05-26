# Market Analysis — 2026-05-21 20:32 UTC

## Market
- **Question:** Will Arsenal win the 2025–26 Champions League?
- **Category:** other
- **YES Price:** 43.0%
- **Days Left:** 9
- **Volume 24h:** $158,470
- **Liquidity:** $831,215

## Statistical Prior
- **p_base:** 33.2%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 9.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,640 (+0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,627 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arsenal 2025–26 champions league
- [Bing News]
- [Tue, 19 May 2026] arsenal 2025–26 champions league
- → We have been crowned 2025/26 Premier League champions with a game to spare, after an incredible campaign in N5 has ended with us claiming our 14th t
- [Tue, 19 May 2026] Arsenal crowned 2025/26 Premier League champions
- → Arsenal were crowned champions of the 2025–26 Premier League season and will also look to win the Champions League.
- [Tue, 19 May 2026] Arsenal win Premier League before Champions League final: How many English teams have achieved ‘the double’?
- → Arsenal and Manchester City are battling for more than Premier League glory in 2025-26. With massive TV revenue, bonus payouts and Champions League 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 33.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 0%<52%

## Tool Calls
- `get_sports_data({'sport': 'nba', 'team': 'Arsenal'})` → No injury data found for nba Arsenal
- `get_odds({'sport': 'soccer_epl', 'team': 'Arsenal'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Arsenal Champions League'})` → No related markets found for 'Arsenal Champions League'
- `search_web({'query': 'Arsenal Champions League final 2025 2026 PSG'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Ousmane Dembele provides positive injury update ah
- `search_web({'query': 'Arsenal vs PSG Champions League final odds prediction May 2026'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] PSG vs Arsenal predictions: Champions League final
- `search_web({'query': 'Arsenal PSG team news injuries lineup May 2026'})` → [Tue, 05 May 2026] Google News
[Wed, 06 May 2026] Arsenal XI vs Atletico Madrid: Starting lineup, co
- `get_market_context({'keyword': 'PSG Champions League'})` → No related markets found for 'PSG Champions League'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*