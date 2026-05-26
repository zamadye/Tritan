# Market Analysis — 2026-05-21 21:46 UTC

## Market
- **Question:** Toronto Blue Jays vs. New York Yankees
- **Category:** sports
- **YES Price:** 44.0%
- **Days Left:** 7
- **Volume 24h:** $195,595
- **Liquidity:** $484,866

## Statistical Prior
- **p_base:** 41.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,700 (+0.2% 24h) → neutral
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
- → New York Yankees outfielder Trent Grisham shared a positive injury update after leaving Wednesday’s game against the Toronto Blue Jays with knee dis

## LLM Decision
- **Action:** SKIP
- **Confidence:** 48%
- **p_true:** 41.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market gap of -3% (44% YES vs 41% base rate) remains below the 5% statistical threshold required for an edge. Both teams have significant pitching injuries: Blue Jays missing Bieber and Berrios (2 starters on IL), Yankees missing Gerrit Cole (ace on IL) - roughly neutral impact. Odds API unavailable to verify bookmaker consensus. No breaking news or concrete catalyst found to tilt this matchup. Previous decisions on identical market correctly identified same gap issue. Entry at 44% with only 50% historical WR in this price range adds additional risk. Recommend SKIP until gap widens or injury/catalyst information emerges.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Blue Jays'})` → INJURY [toronto blue jays] Jesus Sanchez (RF): Day-To-Day
INJURY [toronto blue jays] Shane Bieber (S
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Trent Grisham (CF): Day-To-Day
INJURY [new york yankees] Jasson Dominguez 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Blue Jays'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Blue Jays vs Yankees June 2025 series preview pitching matchup'})` → [Thu, 29 Jan 2026] Google News
[Mon, 20 Oct 2025] Yankees, Blue Jays meet in power-packed AL Divisio
- `search_web({'query': 'Blue Jays Yankees 2026 June series'})` → [Tue, 09 Sep 2025] Google News
[Wed, 21 Jan 2026] Yankees vs. Blue Jays (Jun 14, 2026) Live Score - 
- `get_market_context({'keyword': 'Blue Jays Yankees'})` → No related markets found for 'Blue Jays Yankees'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*