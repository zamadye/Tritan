# Market Analysis — 2026-05-21 20:19 UTC

## Market
- **Question:** Toronto Blue Jays vs. New York Yankees
- **Category:** sports
- **YES Price:** 44.0%
- **Days Left:** 7
- **Volume 24h:** $175,292
- **Liquidity:** $569,066

## Statistical Prior
- **p_base:** 41.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,653 (+0.0% 24h) → neutral
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
- → The Yankees and Blue Jays end a four game-series on Thursday night. Will New York win its first series in two weeks? How to watch and our prediction
- [Thu, 21 May 2026] What channel is Yankees vs Blue Jays today? Start time, where to watch
- → Here's a look at the Yankees lineup as they try to grab a series victory over the Blue Jays on Thursday, May 21.
- [Thu, 21 May 2026] Yankees announce lineup vs Blue Jays today with Ben Rice at leadoff
- → Getty Jazz Chisholm Jr. #13 of the New York Yankees kneels during the fourth inning against the Toronto Blue Jays at Yankee Stadium on May 19, 2026 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 42%
- **p_true:** 41.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
No actionable edge detected. Market gap of -3% (market at 44% vs base rate 41%) falls below the required 5% threshold gate. Injury situation is roughly balanced: Blue Jays missing Berrios (SP) and Bieber (SP) on IL; Yankees missing Gerrit Cole (SP) on IL - both teams have comparable rotation weaknesses. Search results indicate this is an ALDS playoff series, but no specific catalyst or breaking news provides a verifiable edge for either side. Prior identical decisions correctly SKIP'd for the same reason. Win rate for 40-50% entry zone is only 50%, offering no statistical advantage.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Toronto Blue Jays'})` → INJURY [toronto blue jays] Jesus Sanchez (RF): Day-To-Day
INJURY [toronto blue jays] Shane Bieber (S
- `get_sports_data({'sport': 'mlb', 'team': 'New York Yankees'})` → INJURY [new york yankees] Trent Grisham (CF): Day-To-Day
INJURY [new york yankees] Jasson Dominguez 
- `search_web({'query': 'Toronto Blue Jays vs New York Yankees upcoming game 2025'})` → [Sun, 07 Sep 2025] Google News
[Tue, 07 Oct 2025] Toronto Blue Jays at New York Yankees Game Story, 
- `search_web({'query': 'Blue Jays Yankees recent results series 2025'})` → [Sun, 07 Sep 2025] Google News
[Wed, 08 Oct 2025] Toronto Blue Jays at New York Yankees Game Story, 
- `get_market_context({'keyword': 'Blue Jays Yankees'})` → No related markets found for 'Blue Jays Yankees'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Blue Jays'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Yankees vs Blue Jays ALDS Game 3 preview predictions 2025'})` → [Wed, 08 Oct 2025] Google News
[Fri, 03 Oct 2025] Yankees vs. Blue Jays ALDS Game 4 Prediction, Odds
- `search_web({'query': 'Yankees Blue Jays ALDS Game 3 pitching matchup starting pitchers October 2025'})` → [Tue, 07 Oct 2025] Google News
[Sat, 04 Oct 2025] LIVE: Blue Jays-Yankees ALDS Game 3 (FS1) - MLB.co
- `search_web({'query': '"Blue Jays" "Yankees" ALDS Game 3 October 15 2025'})` → [Wed, 15 Oct 2025] Google News
[Wed, 15 Oct 2025] Big dingers in Seattle: Blue Jays power back into 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*