# Market Analysis — 2026-05-21 16:55 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $143,355
- **Liquidity:** $195,048

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,972 (-0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,097 (-0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Tommy Henry — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and the Atlanta Bra
- [Thu, 21 May 2026] Atlanta Braves beat Miami Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → The Atlanta Braves have scored a combined 17 runs since being blown out earlier this week ...
- [Thu, 21 May 2026] Braves Throttle Marlins Again, Close in on Another Series Win
- → Here's how to watch Thursday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% resolve YES only 44.7% of the time, indicating 12.3% overpricing of YES. Recent 9-1 Braves blowout win likely inflating public confidence (recency bias). No matchup-specific evidence (injuries roughly equivalent, no star player absences) contradicts the base rate pattern. Past SKIP decisions focused on the wrong metric (3% gap vs base rate) rather than the powerful 12.3% edge from the stat signal. Entry range 50-60% has poor WR (44%), but the stat signal sample (n=13,967) is far more reliable than pattern sample (n=18).

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `search_web({'query': 'Atlanta Braves vs Miami Marlins May 2025 series preview'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Braves dominate Marlins in 9-1 laugher of a win - 
- `search_web({'query': 'Braves Marlins pitching matchup odds MLB 2025'})` → [Thu, 26 Mar 2026] Google News
[Wed, 15 Apr 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins probable pitchers May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Atlanta Braves recent form record 2026'})` → [Mon, 18 May 2026] Google News
[Thu, 23 Apr 2026] 2026 MLB Standings and Records: Regular Season - M
- `get_market_context({'keyword': 'Braves Marlins MLB'})` → No related markets found for 'Braves Marlins MLB'
- `search_web({'query': '"Braves vs Marlins" May 2026 prediction odds'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Braves vs Marlins Prediction, Picks &amp; Odds for
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'
- `get_sports_data({'sport': 'mlb'})` → INJURY [arizona diamondbacks] Derek Law (RP): Day-To-Day
INJURY [arizona diamondbacks] Tommy Henry (

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*