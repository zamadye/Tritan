# Market Analysis — 2026-05-21 19:15 UTC

## Market
- **Question:** Toronto Blue Jays vs. New York Yankees
- **Category:** sports
- **YES Price:** 44.0%
- **Days Left:** 7
- **Volume 24h:** $169,530
- **Liquidity:** $602,000

## Statistical Prior
- **p_base:** 41.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,374 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,493 (+0.2% 24h) → neutral
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
- → Trey Yesavage outpitched Cam Schlittler in a marquee matchup between young aces, and the Toronto Blue Jays edged the New York Yankees 2-1 on Wednesd
- [Thu, 21 May 2026] Trey Yesavage outduels Cam Schlittler in marquee matchup as Blue Jays top Yankees 2-1
- → Getty Jazz Chisholm Jr. #13 of the New York Yankees kneels during the fourth inning against the Toronto Blue Jays at Yankee Stadium on May 19, 2026 
- [Thu, 21 May 2026] New York Yankees Announce Jazz Chisholm Jr. Decision Before Blue Jays Game
- → The Toronto Blue Jays, ranked third in the AL East with a 22-27 record, face the New York Yankees, who are second in the AL East with a 30-20 record

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 41.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Injuries cancel out (Blue Jays: Bieber/Berrios; Yankees: Cole). Gap only 3% (<5% threshold). No concrete edge or new catalyst identified. Historical pattern shows 50% WR for entry 40-50% range (small sample). Market appears efficient.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Blue Jays'})` → INJURY [toronto blue jays] Jesus Sanchez (RF): Day-To-Day
INJURY [toronto blue jays] Shane Bieber (S
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Trent Grisham (CF): Day-To-Day
INJURY [new york yankees] Jasson Dominguez 
- `search_web({'query': 'Toronto Blue Jays vs New York Yankees upcoming series 2025'})` → [Thu, 09 Oct 2025] Google News
[Thu, 29 Jan 2026] Blue Jays prove they're top dog, clinch ALCS berth
- `search_web({'query': 'Yankees Blue Jays injuries latest news 2025'})` → [Mon, 18 May 2026] Google News
[Thu, 21 May 2026] Series Preview: Blue Jays face Yankees for first t
- `get_market_context({'keyword': 'Blue Jays Yankees'})` → No related markets found for 'Blue Jays Yankees'
- `search_web({'query': 'Blue Jays vs Yankees Polymarket prediction market'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Memorial Day Week Polymarket promo code “SILIVE” a
- `get_odds({'sport': 'baseball_mlb', 'team': 'Blue Jays'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*