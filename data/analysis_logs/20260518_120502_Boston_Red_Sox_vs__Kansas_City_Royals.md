# Market Analysis — 2026-05-18 12:05 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $47,157
- **Liquidity:** $286,065

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,253 (-1.4% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,368 (-1.3% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- BOS @ ATL | Final | Atlanta Braves(home) 32-15 score:8 vs Boston Red Sox(away) 19-27 score:1
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: boston kansas city royals
- [Bing News]
- [Mon, 18 May 2026] boston kansas city royals
- → Here's how to watch Monday's Kansas City Royals vs Boston Red Sox game, including start times, TV channels, scores and how to stream.
- [Mon, 18 May 2026] Where to watch Boston Red Sox vs Kansas City Royals: TV channel, start time, streaming for May 18
- → Boston Red Sox (19-27, fifth in the AL East) vs. Kansas City Royals (20-27, fifth in the AL Central) Kansas City, Missouri; Monday, 7:40 p.m. EDT PI
- [Mon, 18 May 2026] Royals look to break 6-game skid, take on the Red Sox
- → While the Boston Red Sox continue to struggle, they have played well with Sonny Gray on the mound this season.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 51.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** HISTORICAL_PATTERN
- **Catalyst Strength:** 0.50

### Reasoning
Stat signal shows 6.3% edge for NO (markets at 51% resolve YES only 44.7% of time), suggesting crowd bias. However, no direct game-specific catalyst found, injury data is mixed, and past decisions on this exact market already identified the same stat edge yet chose SKIP due to 1% gap failing 5% gate threshold. The historical pattern is structural, not a true information edge for THIS specific game.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Carlos Narvaez (C): Day-To-Day
INJURY [boston red sox] Roman Anthony (LF): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] Matt Strahm (RP)
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals April 2025 prediction'})` → [Sun, 17 May 2026] Google News
[Tue, 21 Apr 2026] Cardinals predicted to land ex-Dodgers, Red Sox ve
- `search_web({'query': 'Red Sox Royals pitching matchup injury report 2025'})` → [Tue, 12 May 2026] Google News
[Thu, 02 Oct 2025] MLB Probable Pitchers Today: Full Starting Pitcher
- `get_market_context({'keyword': 'Red Sox Royals'})` → No related markets found for 'Red Sox Royals'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*