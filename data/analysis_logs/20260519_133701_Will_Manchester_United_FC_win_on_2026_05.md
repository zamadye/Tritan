# Market Analysis — 2026-05-19 13:37 UTC

## Market
- **Question:** Will Manchester United FC win on 2026-05-24?
- **Category:** other
- **YES Price:** 29.0%
- **Days Left:** 5
- **Volume 24h:** $62,724
- **Liquidity:** $556,579

## Statistical Prior
- **p_base:** 24.5%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 4.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,742 (-0.8% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,589 (-0.7% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: manchester united 2026-05-24
- [Bing News]
- [Thu, 14 May 2026] manchester united 2026-05-24
- → Carrick, closer than ever to being confirmed as United's permanent manager.
- [Sat, 16 May 2026] Manchester United Is Determined to Negotiate for Michael Carrick to Be Their Permanent Manager
- → The Premier League's packed Sunday slate begins with Manchester United hosting Nottingham Forest in a meeting at Old Trafford.
- [Fri, 15 May 2026] Manchester United vs. Nottingham Forest prediction, where to watch, time for Premier League match
- → The surgery is expected to rule him out of being selected for the Netherlands' World Cup campaign this summer.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 24.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market (29% YES) is exactly 5% above base rate (24%), not exceeding the 5% gate threshold. Match is 45 days away (Brighton vs Man United, May 24, 2026). No concrete information edge found - no injury data, no odds data, no specific form analysis available. Prior SKIP decisions at similar confidence levels. Crowd shows mild overconfidence but no verifiable catalyst to exploit. Pattern data (OTHER: 67% WR, Entry 20-30%: 75% WR) suggests opportunity exists in this category but current trade lacks the information asymmetry needed for a confident position.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'team': 'Manchester United', 'sport': 'mlb'})` → No injury data found for mlb Manchester United
- `get_odds({'sport': 'soccer_epl', 'team': 'Manchester United'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Manchester United'})` → No related markets found for 'Manchester United'
- `search_web({'query': 'Manchester United fixture May 24 2026'})` → [Thu, 09 Apr 2026] Google News
[Wed, 18 Jun 2025] Man Utd Break 24-Year Tradition With Announcement 
- `search_web({'query': 'Manchester United team news May 2026'})` → No search results for: Manchester United team news May 2026
- `search_web({'query': 'Manchester United Premier League fixture 24 May 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Premier League 2025-26 fixtures: Dates, schedule, 
- `search_web({'query': 'Manchester United results May 2026'})` → [Mon, 18 May 2026] Google News
[Fri, 15 May 2026] Manchester United 3-2 Nottingham Forest: Bruno Fer
- `search_web({'query': 'Manchester United May 24 2026 Premier League fixture'})` → [Tue, 19 May 2026] Google News
[Thu, 09 Apr 2026] How to get Manchester City vs Aston Villa tickets:
- `search_web({'query': 'Manchester United FA Cup Final 2026 date'})` → [Wed, 13 May 2026] Google News
[Sat, 16 May 2026] BBC to broadcast the FA Youth Cup final - Manchest
- `search_web({'query': '"Manchester United" "May 24" 2026'})` → [Fri, 01 May 2026] Google News
[Wed, 18 Jun 2025] How to watch Manchester United on TV in May 2026 -
- `search_web({'query': 'Premier League matchday 38 2025-26 fixtures'})` → [Mon, 18 May 2026] Google News
[Thu, 14 May 2026] Updated Premier League standings, remaining fixtur
- `search_web({'query': 'Brighton form 2025-26 season results'})` → [Mon, 18 May 2026] Google News
[Tue, 21 Apr 2026] Premier League 2025-26 table — Latest standings - 
- `search_web({'query': 'Manchester United form May 2026 results'})` → [Wed, 13 May 2026] Google News
[Tue, 19 May 2026] Manchester United sets May 27 date for Q3 2026 fin
- `get_market_context({'keyword': 'Brighton Manchester United'})` → No related markets found for 'Brighton Manchester United'
- `search_web({'query': 'Brighton vs Manchester United May 24 2026 preview'})` → [Tue, 19 May 2026] Google News
[Wed, 18 Jun 2025] Premier League 2025-26 fixtures: Dates, schedule, 
- `search_web({'query': 'Manchester United away record 2025-26 season'})` → [Sat, 16 May 2026] Google News
[Mon, 09 Feb 2026] Liverpool’s abysmal away record vs. PL top 9: ONE 
- `search_web({'query': 'Brighton home record 2025-26 season Premier League'})` → [Fri, 08 May 2026] Google News
[Wed, 31 Dec 2025] Mitoma equals record for Guinness Goal of the Mont
- `search_web({'query': 'Manchester United Premier League position April 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 27 Apr 2026] Premier League 2025-26 table — Latest standings - 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*