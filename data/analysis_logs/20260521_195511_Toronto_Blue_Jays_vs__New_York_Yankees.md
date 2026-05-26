# Market Analysis — 2026-05-21 19:55 UTC

## Market
- **Question:** Toronto Blue Jays vs. New York Yankees
- **Category:** sports
- **YES Price:** 43.0%
- **Days Left:** 7
- **Volume 24h:** $173,395
- **Liquidity:** $559,166

## Statistical Prior
- **p_base:** 39.6%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,551 (-0.0% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,677 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- [SPORTS] Recent games:
- NYM @ WSH | Scheduled | Washington Nationals(home) 25-25 score:0 vs New York Mets(away) 21-28 score:0
- TOR @ NYY | Scheduled | New York Yankees(home) 30-20 score:0 vs Toronto Blue Jays(away) 22-27 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: toronto blue jays york yankees
- [Bing News]
- [Thu, 21 May 2026] toronto blue jays york yankees
- → Getty Jazz Chisholm Jr. #13 of the New York Yankees kneels during the fourth inning against the Toronto Blue Jays at Yankee Stadium on May 19, 2026 
- [Thu, 21 May 2026] New York Yankees Announce Jazz Chisholm Jr. Decision Before Blue Jays Game
- → Trey Yesavage outpitched Cam Schlittler in a marquee matchup between young aces, and the Toronto Blue Jays edged the New York Yankees 2-1 on Wednesd
- [Thu, 21 May 2026] Trey Yesavage outduels Cam Schlittler in marquee matchup as Blue Jays top Yankees 2-1
- → The Toronto Blue Jays shared news regarding the pitching rotation ahead of a matchup against the New York Yankees on Thursday, May 21.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 39.6%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
No actionable edge. Market gap of 3% is below 5% threshold. Both teams have comparable injury situations (starting pitchers on IL). No verifiable catalyst or breaking news to create price inefficiency. Previous identical markets correctly skipped.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Blue Jays'})` → INJURY [toronto blue jays] Jesus Sanchez (RF): Day-To-Day
INJURY [toronto blue jays] Shane Bieber (S
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Trent Grisham (CF): Day-To-Day
INJURY [new york yankees] Jasson Dominguez 
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Toronto Blue Jays vs New York Yankees game today news'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Trey Yesavage, Blue Jays get best of Cam Schlittle
- `search_web({'query': 'Blue Jays Yankees series preview injury update'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Fantasy baseball: Mets, Yankees ready to reshape r
- `get_market_context({'keyword': 'Blue Jays'})` → No related markets found for 'Blue Jays'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*