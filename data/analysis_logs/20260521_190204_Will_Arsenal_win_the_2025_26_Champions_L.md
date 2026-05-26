# Market Analysis — 2026-05-21 19:02 UTC

## Market
- **Question:** Will Arsenal win the 2025–26 Champions League?
- **Category:** other
- **YES Price:** 43.0%
- **Days Left:** 9
- **Volume 24h:** $163,682
- **Liquidity:** $817,616

## Statistical Prior
- **p_base:** 33.2%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 9.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,462 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,670 (+0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arsenal 2025–26 champions league
- [Bing News]
- [Tue, 19 May 2026] arsenal 2025–26 champions league
- → We have been crowned 2025/26 Premier League champions with a game to spare, after an incredible campaign in N5 has ended with us claiming our 14th t
- [Tue, 19 May 2026] Arsenal crowned 2025/26 Premier League champions
- → Arsenal and Manchester City are battling for more than Premier League glory in 2025-26. With massive TV revenue, bonus payouts and Champions League 
- [Tue, 19 May 2026] 2025-26 Premier League prize money: How much will Arsenal make for winning the title?
- → Arsenal were crowned champions of the 2025–26 Premier League season and will also look to win the Champions League.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 33.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Champions League final between Arsenal and PSG is a single match between two elite teams. Market price of 43% for Arsenal seems reasonable given they're slight underdogs. No concrete evidence of mispricing found - no bookmaker odds data available, no injury reports, no tactical analysis to suggest edge. Past decision to skip at 45% confidence remains appropriate.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'soccer', 'team': 'Arsenal'})` → No injury data found for soccer Arsenal
- `get_odds({'sport': 'soccer_epl', 'team': 'Arsenal'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Champions League 2026 final Arsenal PSG'})` → No related markets found for 'Champions League 2026 final Arsenal PSG'
- `search_web({'query': 'Arsenal vs PSG Champions League final 2026 odds'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] PSG vs Arsenal predictions: Champions League final
- `search_web({'query': 'Arsenal PSG Champions League final May 2026 predictions winner'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] Champions League final predictions: Arsenal vs PSG
- `get_market_context({'keyword': 'PSG Champions League'})` → No related markets found for 'PSG Champions League'
- `search_web({'query': 'PSG vs Arsenal Champions League final odds betting May 21 2026'})` → [Thu, 21 May 2026] Google News
[Wed, 06 May 2026] How to get PSG Champions League Final 2026 tickets
- `search_web({'query': 'Arsenal vs PSG Champions League final 2026 who will win'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Is the Champions League final 2026 available to wa
- `search_web({'query': '"PSG vs Arsenal" Champions League final 2026 odds 50 50 favorite'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Champions League final predictions: Arsenal vs PSG
- `search_web({'query': 'ESPN PSG Arsenal Champions League final predictions odds winner'})` → [Thu, 07 May 2026] Google News
[Wed, 13 May 2026] Champions League final: PSG-Arsenal predictions, o

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*