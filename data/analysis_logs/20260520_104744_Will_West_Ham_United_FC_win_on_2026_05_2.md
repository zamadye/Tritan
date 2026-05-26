# Market Analysis — 2026-05-20 10:47 UTC

## Market
- **Question:** Will West Ham United FC win on 2026-05-24?
- **Category:** other
- **YES Price:** 54.0%
- **Days Left:** 4
- **Volume 24h:** $75,805
- **Liquidity:** $607,128

## Statistical Prior
- **p_base:** 40.4%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 13.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,473 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,473 (+0.9% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: west united 2026-05-24
- [Bing News]
- [] west united 2026-05-24
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 30.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.75

### Reasoning
Stat signal shows clear overpricing: markets at 54% historically resolve YES only 44.7% (n=13,967), creating ~9.3% edge for NO. Leeds are 'flying' per recent reports with 3-5-2 system working well. Entry range 50-60% has only 33% WR historically from 9 trades. Home advantage for West Ham exists but Leeds strong form and statistical overpricing make NO the value side.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `get_sports_data({'sport': 'soccer', 'team': 'West Ham'})` → No injury data found for soccer West Ham
- `get_odds({'sport': 'soccer_epl', 'team': 'West Ham'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'West Ham United May 24 2026 match fixture'})` → [Wed, 20 May 2026] Google News
[Wed, 18 Jun 2025] Premier League 2025-26 fixtures: Dates, schedule, 
- `search_web({'query': 'West Ham United recent form May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Newcastle vs West Ham Prediction, Betting Pick, La
- `search_web({'query': '"May 24" West Ham United 2026'})` → [Wed, 20 May 2026] Google News
[Fri, 15 May 2026] Premier League 2025-26 fixtures: Dates, schedule, 
- `get_market_context({'keyword': 'West Ham'})` → No related markets found for 'West Ham'
- `search_web({'query': 'West Ham vs Leeds May 24 2026 preview'})` → [Fri, 15 May 2026] Google News
[Mon, 18 May 2026] West Ham vs. Leeds (May 24, 2026) Live Score - ESP
- `search_web({'query': 'West Ham United injury news May 2026'})` → [Mon, 18 May 2026] Google News
[Fri, 08 May 2026] Newcastle United issue official Sandro Tonali inju
- `search_web({'query': 'West Ham United form 2025-26 season standings'})` → [Sun, 17 May 2026] Google News
[Thu, 19 Feb 2026] Man Utd top scorers 2025/26: Who is leading the cl
- `search_web({'query': 'Leeds United form May 2026'})` → [Mon, 11 May 2026] Google News
[Mon, 18 May 2026] Tottenham Hotspur v Leeds United: Key stats and ta
- `search_web({'query': '"West Ham vs Leeds" "May 24" betting odds prediction'})` → [Tue, 19 May 2026] Google News
[Sat, 04 Apr 2026] Premier League Relegation Odds 2025-26: Tottenham 
- `search_web({'query': 'Premier League May 24 2026 results'})` → [Wed, 20 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 fixtures: Dates, schedule, 
- `search_web({'query': 'West Ham vs Leeds predictions team news betting tips odds Racing Post May 13'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Premier League predictions, football betting tips 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*