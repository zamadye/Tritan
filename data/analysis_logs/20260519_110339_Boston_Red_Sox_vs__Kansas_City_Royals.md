# Market Analysis — 2026-05-19 11:03 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $56,832
- **Liquidity:** $78,362

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,000 (+0.3% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,990 (+0.4% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- BOS @ KC | Final | Kansas City Royals(home) 20-28 score:1 vs Boston Red Sox(away) 20-27 score:3
- [SPORTS] Injuries:
- ?: James McCann — Out (Strain)
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: boston kansas city royals
- [Bing News]
- [Tue, 19 May 2026] boston kansas city royals
- → Here's how to watch Tuesday's Kansas City Royals vs Boston Red Sox game, including start times, TV channels, scores and how to stream.
- [Tue, 19 May 2026] Where to watch Boston Red Sox vs Kansas City Royals: TV channel, start time, streaming for May 19
- → Boston Red Sox (20-27, fifth in the AL East) vs. Kansas City Royals (20-28, fifth in the AL Central) Kansas City, Missouri; Tuesday, 7:40 p.m. EDT P
- [Tue, 19 May 2026] Red Sox face the Royals with 1-0 series lead
- → On Monday, the Royals fell short in a 3-1 loss to the Boston Red Sox at Kauffman Stadium. It was their sixth loss in seven games. The Royals had the

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Red Sox Royals'})` → No related markets found for 'Red Sox Royals'
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals 2025 game preview starting pitcher'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Royals Place All-Star Pitcher On Injured List Befo
- `search_web({'query': 'Boston Red Sox recent performance results May 2025'})` → [Tue, 05 May 2026] Google News
[Sat, 22 Nov 2025] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Royals All-Star pitcher injured list Red Sox series May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Royals place All-Star pitcher on injured list ahea
- `search_web({'query': 'Kansas City Royals injuries starting pitcher May 2026'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Royals Rotation Takes Another Hit Following Latest

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*