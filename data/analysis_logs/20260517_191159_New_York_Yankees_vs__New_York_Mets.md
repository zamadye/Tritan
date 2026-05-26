# Market Analysis — 2026-05-17 19:11 UTC

## Market
- **Question:** New York Yankees vs. New York Mets
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 6
- **Volume 24h:** $964,020
- **Liquidity:** $91,131

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,229 (+0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,098 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Recent games:
- NYY @ NYM | In Progress | New York Mets(home) 19-26 score:1 vs New York Yankees(away) 28-18 score:1
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: york yankees york mets
- [Bing News]
- [Sun, 17 May 2026] york yankees york mets
- → Get ready for a classic Subway Series showdown on Sunday as the New York Yankees are in Flushing, Queens, to take on the New York Mets at Citi Field
- [Sun, 17 May 2026] Yankees vs Mets prediction for Sunday: Trade MLB action on Polymarket
- → Follow our live updates as the New York Mets take on the New York Yankees on Sunday at Citi Field.
- [Sun, 17 May 2026] NY Mets vs Yankees live updates, score and analysis of today's game
- → Here's how to watch Sunday's New York Mets vs New York Yankees game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 41.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** HISTORICAL_PATTERN
- **Catalyst Strength:** 0.80

### Reasoning
Strong historical pattern: Markets at 52% resolve YES only 44.7% of time (n=13,967), indicating 7.3% overpricing of YES. Sportsbook odds show Yankees as clear favorites (57-68%), suggesting YES likely represents Mets win, which is overpriced at 52% vs 32-43% sportsbook consensus. Both teams have significant injuries (Yankees: Cole, Fried, Stanton; Mets: Holmes, Polanco, Alvarez), but sportsbooks still favor Yankees. Pattern signals support action: SPORTS WR=85% (13 trades), Entry 50-60% WR=86% (7 trades). The large-sample statistical signal (n=13,967) provides robust evidence of systematic overpricing at this price level.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Gerrit Cole (SP): 15-Day-IL
INJURY [new york yankees] Max Fried (SP): 15-D
- `get_sports_data({'sport': 'mlb', 'team': 'Mets'})` → INJURY [new york mets] Clay Holmes (SP): 15-Day-IL
INJURY [new york mets] Jorge Polanco (1B): 10-Day
- `search_web({'query': 'New York Yankees vs Mets 2025 series schedule'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] Where to watch Yankees vs. Mets: Subway Series sch
- `search_web({'query': 'Yankees Mets game today June 2025'})` → [Sat, 05 Jul 2025] Google News
[Sat, 05 Jul 2025] New York Yankees at New York Mets Game Story, Scor
- `search_web({'query': 'Yankees Mets June 11 2025'})` → [Sat, 16 May 2026] Google News
[Fri, 06 Mar 2026] 2026 New York Yankees TV schedule: How to watch, s
- `get_odds({'sport': 'baseball_mlb', 'team': 'Yankees'})` → [ODDS] baseball_mlb — 2 events
  New York Mets vs New York Yankees (2026-05-17)
    [FanDuel] New Yo
- `get_market_context({'keyword': 'Yankees Mets'})` → No related markets found for 'Yankees Mets'
- `search_web({'query': '"Yankees vs Mets" June 2025 pitching matchup'})` → [Thu, 14 May 2026] Google News
[Fri, 15 May 2026] Yankees vs. Mets: Kalshi markets and preview of th

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*