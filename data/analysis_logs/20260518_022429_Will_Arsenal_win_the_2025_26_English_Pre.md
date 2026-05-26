# Market Analysis — 2026-05-18 02:24 UTC

## Market
- **Question:** Will Arsenal win the 2025–26 English Premier League?
- **Category:** other
- **YES Price:** 82.0%
- **Days Left:** 8
- **Volume 24h:** $78,793
- **Liquidity:** $59,410

## Statistical Prior
- **p_base:** 63.7%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 18.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,041 (-1.0% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,098 (-0.9% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arsenal 2025–26 english premier league
- [Bing News]
- [Tue, 05 May 2026] arsenal 2025–26 english premier league
- → Manchester City were held to a 3‑3 draw by Everton in the English Premier League, leaving Pep Guardiola’s side five points behind leaders Arsenal wi
- [Fri, 17 Apr 2026] EPL 2025-26 Points Table: When Can Arsenal Win Premier League Title – Check State Of Play After Everton Vs Man City Draw
- → The English Premier League 2025-26 title race comes down to Arsenal’s visit to Manchester City at the Etihad on Sunday. Let’s analyse where the matc
- [Sun, 17 May 2026] Man City Vs Arsenal Match Prediction: Where Will The Premier League Title Clash Be Won Or Lost?
- → Arsenal return to the Emirates for their final home match of the 2025/26 Premier League season as they host Burnley for a match with massive title s

## LLM Decision
- **Action:** SKIP
- **Confidence:** 48%
- **p_true:** 63.7%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** TITLE_RACE_UNCERTAINTY
- **Catalyst Strength:** 0.35

### Reasoning
Two-horse race with 2 games remaining; Arsenal has advantage after Fulham win but still described as neck-and-neck. Market at 82% may be slightly overpriced given uncertainty, but no concrete evidence to justify a NO bet. Base rate (64%) vs market (82%) gap suggests crowd skepticism, but insufficient direct catalyst for actionable edge. Pattern shows info gap trades only 50% WR.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 48%<52%

## Tool Calls
- `get_odds({'sport': 'soccer_epl', 'team': 'Arsenal'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Arsenal Premier League title race 2025-26 standings May 2026'})` → [Sun, 17 May 2026] Google News
[Thu, 14 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Arsenal Manchester City Premier League title decider remaining fixtures'})` → [Tue, 05 May 2026] Google News
[Fri, 17 Apr 2026] Premier League title race: Fixtures, state of play
- `search_web({'query': 'Premier League standings May 17 2026 Arsenal Manchester City points'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Arsenal Premier League title 2026 games remaining fixtures schedule'})` → [Sun, 17 May 2026] Google News
[Tue, 05 May 2026] Arsenal and Man City's remaining Premier League fi
- `search_web({'query': 'Arsenal Manchester City Premier League points table May 2026 who is leading'})` → [Sun, 17 May 2026] Google News
[Wed, 13 May 2026] How Arsenal or Man City can clinch Premier League 
- `search_web({'query': 'Premier League 2025-26 final standings table latest'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 table — Latest standings - 
- `get_market_context({'keyword': 'Arsenal Premier League title'})` → No related markets found for 'Arsenal Premier League title'
- `search_web({'query': '"Arsenal" "Premier League" "title" "May 2026" "games left" standings points'})` → [Thu, 14 May 2026] Google News
[Sat, 02 May 2026] Man City 3-0 Crystal Palace, Premier League: Hosts
- `search_web({'query': 'Arsenal Man City Premier League title race May 17 2026 who is winning'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] The earliest dates Arsenal or Man City could win t
- `search_web({'query': 'Premier League table after matchday 36 2026 standings points'})` → [Tue, 12 May 2026] Google News
[Mon, 11 May 2026] Premier League predictions: West Ham vs Arsenal, L
- `search_web({'query': '"Arsenal" points "82" OR "83" OR "84" OR "85" "Manchester City" points Premier League 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 20 Apr 2026] Premier League table since Man Utd appointed Micha
- `search_web({'query': 'Arsenal Premier League title permutations clinch May 2026'})` → [Wed, 13 May 2026] Google News
[Fri, 15 May 2026] Premier League permutations: When could the title,

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*