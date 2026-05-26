# Market Analysis — 2026-05-21 21:34 UTC

## Market
- **Question:** Toronto Blue Jays vs. New York Yankees
- **Category:** sports
- **YES Price:** 44.0%
- **Days Left:** 7
- **Volume 24h:** $194,101
- **Liquidity:** $486,151

## Statistical Prior
- **p_base:** 41.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,697 (+0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,711 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- NYM @ WSH | In Progress | Washington Nationals(home) 25-25 score:1 vs New York Mets(away) 21-28 score:2
- TOR @ NYY | Scheduled | New York Yankees(home) 30-20 score:0 vs Toronto Blue Jays(away) 22-27 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: toronto blue jays york yankees
- [Bing News]
- [Thu, 21 May 2026] toronto blue jays york yankees
- → Toronto Blue Jays (22-27, third in the AL East) vs. New York Yankees (30-20, second in the AL East) New York; Thursday, 7:05 p.m. EDT. PITCHING PROB
- [Thu, 21 May 2026] New York Yankees and Toronto Blue Jays meet in game 4 of series
- → Getty Jazz Chisholm Jr. #13 of the New York Yankees kneels during the fourth inning against the Toronto Blue Jays at Yankee Stadium on May 19, 2026 
- [Thu, 21 May 2026] New York Yankees Announce Jazz Chisholm Jr. Decision Before Blue Jays Game
- → The Toronto Blue Jays shared news regarding the pitching rotation ahead of a matchup against the New York Yankees on Thursday, May 21.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 48%
- **p_true:** 41.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Market gap of -3% (44% market vs 41% base rate) falls below the 5% threshold required for statistical edge. No verifiable catalyst or new information found. Previous decisions for same market resulted in SKIP. Injury data for both teams is already likely priced in.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Toronto Blue Jays'})` → INJURY [toronto blue jays] Jesus Sanchez (RF): Day-To-Day
INJURY [toronto blue jays] Shane Bieber (S
- `get_sports_data({'sport': 'mlb', 'team': 'New York Yankees'})` → INJURY [new york yankees] Trent Grisham (CF): Day-To-Day
INJURY [new york yankees] Jasson Dominguez 
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Toronto Blue Jays vs New York Yankees upcoming series 2025'})` → [Thu, 21 May 2026] Google News
[Thu, 09 Oct 2025] Toronto Blue Jays vs. New York Yankees prediction,
- `search_web({'query': 'Blue Jays Yankees series May 2025 injuries'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] MLB 2026 Buzz: Mariners’ J.P. Crawford Open To Mov
- `search_web({'query': 'Toronto Blue Jays vs New York Yankees 2025 season current series'})` → [Wed, 08 Oct 2025] Google News
[Wed, 08 Oct 2025] Toronto Blue Jays at New York Yankees Game Story, 
- `get_market_context({'keyword': 'Toronto Blue Jays'})` → No related markets found for 'Toronto Blue Jays'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*