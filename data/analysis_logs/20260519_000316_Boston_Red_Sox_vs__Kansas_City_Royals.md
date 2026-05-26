# Market Analysis — 2026-05-19 00:03 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 6
- **Volume 24h:** $174,673
- **Liquidity:** $35,375

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,966 (-0.6% 24h) → neutral
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,037 (-0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- BOS @ KC | In Progress | Kansas City Royals(home) 20-27 score:0 vs Boston Red Sox(away) 19-27 score:0
- [SPORTS] Injuries:
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: boston kansas city royals
- [Bing News]
- [Mon, 18 May 2026] boston kansas city royals
- → The Kansas City Royals and Boston Red Sox will open this week’s series in Missouri at 6:10 p.m. ET rather than 6:40 p.m. ET “out of an abundance of 
- [Mon, 18 May 2026] Royals change time of Monday’s Red Sox game due to threat of severe weather
- → The Royals are scheduled to kick off their 9-game homestand with a series opener against Boston at The K on Monday night.
- [Mon, 18 May 2026] With eye on weather, Royals move up Monday game time for series opener vs. Red Sox
- → Kris Bubic was expected to start Game 2 of the Kansas City Royals’ series against the Boston Red Sox at Kauffman Stadium. But they will need to star

## LLM Decision
- **Action:** SKIP
- **Confidence:** 48%
- **p_true:** 51.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE_IDENTIFIED
- **Catalyst Strength:** 0.20

### Reasoning
Stat signal suggests YES overpriced (44.7% vs 51%) with n=13,967, but gap=1% fails 5% gate. No concrete catalyst identified — starting pitchers unknown, no breaking news. Previous decisions for same market both SKIP. Entry zone 50-60% has only 40% historical WR. Royals missing two SPs but impact unclear without lineup confirmation.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_sports_data({'sport': 'mlb', 'team': 'Royals'})` → INJURY [kansas city royals] Kris Bubic (SP): 15-Day-IL
INJURY [kansas city royals] Cole Ragans (SP):
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals 2025 game preview predictions'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Red Sox vs. Royals: Prediction, Lineups, How to Wa
- `search_web({'query': 'Boston Red Sox recent form results May 2025'})` → [Mon, 18 May 2026] Google News
[Thu, 31 Jul 2025] Where to watch Boston Red Sox vs Kansas City Royal
- `get_market_context({'keyword': 'Red Sox Royals baseball'})` → No related markets found for 'Red Sox Royals baseball'
- `search_web({'query': 'Kansas City Royals injury news May 2025 Cole Ragans update'})` → [Sat, 16 May 2026] Google News
[Fri, 08 May 2026] Latest Royals injuries &amp; transactions - MLB.co
- `search_web({'query': 'Boston Red Sox starting pitcher today 2025'})` → [Sat, 16 May 2026] Google News
[Mon, 20 Apr 2026] Fantasy Baseball Reliever Depth Chart - ESPN
[Fri,

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*