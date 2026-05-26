# Market Analysis — 2026-05-21 20:05 UTC

## Market
- **Question:** Toronto Blue Jays vs. New York Yankees
- **Category:** sports
- **YES Price:** 44.0%
- **Days Left:** 7
- **Volume 24h:** $173,486
- **Liquidity:** $563,906

## Statistical Prior
- **p_base:** 41.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,667 (+0.1% 24h) → neutral
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
- **Confidence:** 42%
- **p_true:** 41.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
No actionable edge. Market gap of -3% is below 5% threshold. Both teams have comparable injury situations (Blue Jays: Bieber/Berrios; Yankees: Cole). No breaking news or direct catalyst identified. Past analyses of this matchup yielded same conclusion.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Blue Jays'})` → INJURY [toronto blue jays] Jesus Sanchez (RF): Day-To-Day
INJURY [toronto blue jays] Shane Bieber (S
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Trent Grisham (CF): Day-To-Day
INJURY [new york yankees] Jasson Dominguez 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Yankees'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb', 'team': 'Blue Jays'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Toronto Blue Jays vs New York Yankees injury report April 2025'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Toronto Blue Jays vs. New York Yankees prediction,
- `search_web({'query': 'New York Yankees vs Toronto Blue Jays odds 2025'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Yankees vs Blue Jays Prediction, Odds, Moneyline, 
- `get_market_context({'keyword': 'Blue Jays Yankees'})` → No related markets found for 'Blue Jays Yankees'
- `search_web({'query': 'Blue Jays vs Yankees starting pitchers May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Where to watch Toronto Blue Jays vs. New York Yank
- `search_web({'query': 'Blue Jays Yankees head to head 2026 season'})` → [Mon, 18 May 2026] Google News
[Thu, 21 May 2026] 5 key series to watch this week - MLB.com
[Tue, 19
- `search_web({'query': '"Blue Jays" "Yankees" prediction May 21 2026 picks'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Blue Jays vs Yankees Prediction, Odds &amp; Home R
- `search_web({'query': 'DraftKings Network Blue Jays Yankees prediction May 21 2026 starting pitchers'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*