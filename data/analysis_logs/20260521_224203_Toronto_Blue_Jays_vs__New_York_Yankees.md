# Market Analysis — 2026-05-21 22:42 UTC

## Market
- **Question:** Toronto Blue Jays vs. New York Yankees
- **Category:** sports
- **YES Price:** 44.0%
- **Days Left:** 7
- **Volume 24h:** $212,388
- **Liquidity:** $566,468

## Statistical Prior
- **p_base:** 41.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,633 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,500 (+0.2% 24h) → neutral
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
- → Getty Jazz Chisholm Jr. #13 of the New York Yankees kneels during the fourth inning against the Toronto Blue Jays at Yankee Stadium on May 19, 2026 
- [Thu, 21 May 2026] New York Yankees Announce Jazz Chisholm Jr. Decision Before Blue Jays Game
- → New York Yankees outfielder Trent Grisham shared a positive injury update after leaving Wednesday’s game against the Toronto Blue Jays with knee dis
- [Thu, 21 May 2026] NY Yankees’ Trent Grisham provides encouraging injury update after scare vs Blue Jays
- → New York Yankees right fielder Aaron Judge made an announcement.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 41.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_REPORT_BALANCED
- **Catalyst Strength:** 0.20

### Reasoning
Market gap of 3% remains below 5% threshold. Both teams have comparable injuries (Blue Jays missing Bieber/Berrios, Yankees missing Cole). No concrete catalyst or new information to justify a bet. Past decisions correctly skipped this exact market twice.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Toronto Blue Jays'})` → INJURY [toronto blue jays] Jesus Sanchez (RF): Day-To-Day
INJURY [toronto blue jays] Shane Bieber (S
- `get_sports_data({'sport': 'mlb', 'team': 'New York Yankees'})` → INJURY [new york yankees] Trent Grisham (CF): Day-To-Day
INJURY [new york yankees] Jasson Dominguez 
- `search_web({'query': 'Toronto Blue Jays vs New York Yankees 2025 injury report'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] NY Yankees’ Trent Grisham provides encouraging inj
- `search_web({'query': 'New York Yankees vs Toronto Blue Jays recent results 2025'})` → [Wed, 08 Oct 2025] Google News
[Sat, 04 Oct 2025] Toronto Blue Jays at New York Yankees Game Story, 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Blue Jays'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb', 'team': 'Yankees'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Blue Jays Yankees'})` → No related markets found for 'Blue Jays Yankees'
- `search_web({'query': 'Toronto Blue Jays vs New York Yankees May 21 2026 pitching matchup'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Toronto Blue Jays vs. New York Yankees - Live Scor
- `search_web({'query': '"Blue Jays vs Yankees" May 21 2026 starting pitcher'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Blue Jays vs Yankees Prediction, Best Bets &amp; H

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*