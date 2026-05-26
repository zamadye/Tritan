# Market Analysis — 2026-05-19 07:22 UTC

## Market
- **Question:** Will Manchester United FC win on 2026-05-24?
- **Category:** other
- **YES Price:** 29.0%
- **Days Left:** 5
- **Volume 24h:** $62,766
- **Liquidity:** $568,865

## Statistical Prior
- **p_base:** 24.5%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 4.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,013 (+0.2% 24h) → neutral
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
- **p_true:** 24.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Market at 29% YES is 5% above base rate of 24%. Brighton in 'flailing form' while United's Bruno Fernandes having excellent season. However, no concrete bookmaker odds to compare, and the 5% gap is exactly at threshold. Evidence is moderate but not strong enough to identify clear mispricing. Previous decision was also SKIP with similar reasoning.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'sport': 'nba', 'team': 'Manchester United'})` → No injury data found for nba Manchester United
- `get_odds({'sport': 'soccer_epl', 'team': 'Manchester United'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Manchester United May 24 2026 fixture match'})` → [Wed, 18 Jun 2025] Google News
[Thu, 09 Apr 2026] Premier League fixtures schedule 2025-26 in full -
- `search_web({'query': 'Manchester United last match 2025-2026 season results'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Premier League 2025-26 table — Latest standings - 
- `get_market_context({'keyword': 'Manchester United'})` → No related markets found for 'Manchester United'
- `search_web({'query': 'Manchester United Premier League fixture May 24 2026'})` → [Wed, 18 Jun 2025] Google News
[Thu, 09 Apr 2026] Premier League fixtures schedule 2025-26 in full -
- `search_web({'query': 'Manchester United form 2026 season results wins losses'})` → [Tue, 19 May 2026] Google News
[Mon, 09 Mar 2026] AFC Bournemouth vs Manchester City: Premier League
- `search_web({'query': 'Premier League 2025-26 season last matchday date May 2026'})` → [Wed, 21 Jan 2026] Google News
[Fri, 15 May 2026] 2025/26 Champions League: Teams, format, dates, dr
- `search_web({'query': '"Manchester United" "May 24" OR "24 May" 2026 match'})` → [Wed, 18 Jun 2025] Google News
[Thu, 09 Apr 2026] Brighton vs. Man United (May 24, 2026) Live Score 
- `search_web({'query': 'Brighton vs Manchester United May 24 2026 odds preview'})` → [Sat, 16 May 2026] Google News
[Thu, 14 May 2026] Leeds vs. Brighton prediction, odds, Premier Leagu
- `search_web({'query': 'Brighton form 2026 Premier League results'})` → [Fri, 13 Feb 2026] Google News
[Tue, 21 Apr 2026] Fabian Hurzeler feels ‘no pressure’ from Brighton 
- `search_web({'query': 'Manchester United away form 2026 Premier League'})` → [Tue, 19 May 2026] Google News
[Sun, 17 May 2026] Bruno Fernandes is Manchester United’s player of t

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*