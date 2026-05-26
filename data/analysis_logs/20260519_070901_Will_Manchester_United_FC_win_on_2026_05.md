# Market Analysis — 2026-05-19 07:09 UTC

## Market
- **Question:** Will Manchester United FC win on 2026-05-24?
- **Category:** other
- **YES Price:** 29.0%
- **Days Left:** 5
- **Volume 24h:** $62,762
- **Liquidity:** $568,594

## Statistical Prior
- **p_base:** 24.5%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 4.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,007 (+0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,936 (+0.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: manchester united 2026-05-24
- [Bing News]
- [Thu, 14 May 2026] manchester united 2026-05-24
- → Carrick, closer than ever to being confirmed as United's permanent manager.
- [Tue, 12 May 2026] Manchester United Is Determined to Negotiate for Michael Carrick to Be Their Permanent Manager
- → Manchester United will reportedly look to sign 24-year-old AC Milan centre-back Strahinja Pavlovic in the summer transfer window.
- [Fri, 15 May 2026] Manchester United front-runners to sign Strahinja Pavlovic
- → The surgery is expected to rule him out of being selected for the Netherlands' World Cup campaign this summer.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 22.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** PRICING
- **Catalyst Strength:** 0.45

### Reasoning
Market at 29% YES is 5% above base rate of 24%, indicating crowd overconfidence. No concrete evidence found supporting Manchester United win on May 24. Longshot pricing in 10-40% range with negative gap suggests overvaluation. Pattern data shows 75% WR at this entry range historically, but negative gap indicates NO value.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `search_web({'query': 'Manchester United May 24 2026 match preview'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] Manchester United 3-2 Nottingham Forest: Bruno Fer
- `search_web({'query': 'Manchester United injury news May 2026'})` → [Fri, 15 May 2026] Google News
[Thu, 07 May 2026] Man United injury list: Players out, potential ret
- `get_odds({'sport': 'soccer_epl', 'team': 'Manchester United'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Manchester United'})` → No related markets found for 'Manchester United'
- `search_web({'query': 'Manchester United fixture schedule May 24 2026 Premier League'})` → [Thu, 09 Apr 2026] Google News
[Wed, 18 Jun 2025] Premier League 2025-26 fixtures: Dates, schedule, 
- `search_web({'query': 'Manchester United form May 2026 results'})` → [Wed, 13 May 2026] Google News
[Wed, 13 May 2026] Manchester United sets May 27 date for Q3 2026 fin
- `search_web({'query': 'Premier League matchday May 24 2026 fixtures schedule'})` → [Mon, 18 May 2026] Google News
[Thu, 07 May 2026] Premier League: TV schedule for Matchday 34 announ
- `search_web({'query': 'Manchester United last 5 matches results 2026'})` → [Sun, 03 May 2026] Google News
[Wed, 06 May 2026] Man Utd vs. Liverpool: Last Six Results in Histori
- `get_sports_data({'sport': 'nba', 'team': 'Manchester United'})` → No injury data found for nba Manchester United
- `search_web({'query': 'Manchester United vs who May 24 2026 Premier League final day'})` → [Thu, 07 May 2026] Google News
[Thu, 09 Apr 2026] 2025 Premier League TV Schedule: How to watch EPL 
- `search_web({'query': 'Manchester United Premier League position May 2026 standings'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': '"May 24" 2026 Manchester United Premier League fixture'})` → [Wed, 13 May 2026] Google News
[Tue, 12 May 2026] Premier League permutations: When could the title,
- `search_web({'query': 'Premier League final day 2025-26 season May 24'})` → [Sun, 17 May 2026] Google News
[Wed, 13 May 2026] Arsenal and Man City's remaining Premier League fi
- `search_web({'query': '"Manchester United" "May 24" 2026 match opponent'})` → [Wed, 22 Apr 2026] Google News
[Wed, 18 Jun 2025] How Chelsea’s Fixtures Compare to Man Utd, Aston V

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*