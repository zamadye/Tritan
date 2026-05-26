# Market Analysis — 2026-05-19 07:49 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 7
- **Volume 24h:** $54,413
- **Liquidity:** $77,187

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,188 (+0.4% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,190 (+0.3% 24h) → neutral

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
- [Mon, 18 May 2026] boston kansas city royals
- → On Monday, the Royals fell short in a 3-1 loss to the Boston Red Sox at Kauffman Stadium. It was their sixth loss in seven games. The Royals had the
- [Tue, 19 May 2026] Royals’ losing ways return in series-opening defeat against Red Sox: what happened
- → Sonny Gray allowed a run and struck out a season-high nine while pitching into the seventh inning, Willson Contreras clubbed a two-run homer, and th
- [Mon, 18 May 2026] Gray's strong outing leads Red Sox past Royals 3-1
- → The Royals are scheduled to kick off their 9-game homestand with a series opener against Boston at The K on Monday night.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 53.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_REPORT
- **Catalyst Strength:** 0.40

### Reasoning
Royals All-Star pitcher Kris Bubic placed on IL (elbow soreness) was scheduled starter - this is a direct catalyst favoring Red Sox YES. However: (1) Stat signal from 13,967 historical markets at 52% shows YES resolves only 44.7% - strong evidence market overprices YES by ~7%; (2) Gap between market (52%) and base rate (53%) is only 1%, failing the 5% gate threshold; (3) Bubic IL news appears already incorporated into the 52% price; (4) Entry zone 50-60% has historically poor 33% win rate from 6 trades; (5) Both teams described as 'struggling' with no clear form edge. The injury catalyst likely offsets some of the stat signal but doesn't create a clear profitable edge. Previous decisions on identical market correctly identified gap too small.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Red Sox Royals'})` → No related markets found for 'Red Sox Royals'
- `search_web({'query': 'Boston Red Sox Kansas City Royals game 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Where to watch Boston Red Sox vs Kansas City Royal
- `search_web({'query': 'Red Sox vs Royals recent results 2025'})` → [Mon, 04 Aug 2025] Google News
[Tue, 05 Aug 2025] Kansas City Royals at Boston Red Sox Game Story, S
- `search_web({'query': 'Boston Red Sox recent performance results May 2026'})` → [Mon, 18 May 2026] Google News
[Wed, 13 May 2026] Where to watch Boston Red Sox vs Kansas City Royal
- `search_web({'query': 'Kansas City Royals recent performance results May 2026'})` → [Mon, 18 May 2026] Google News
[Thu, 07 May 2026] Where to watch Boston Red Sox vs Kansas City Royal
- `search_web({'query': 'Kansas City Royals All-Star pitcher injured list May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Royals Rotation Takes Another Hit Following Latest
- `search_web({'query': 'Boston Red Sox record 2026 standings wins losses'})` → [Sun, 17 May 2026] Google News
[Tue, 24 Mar 2026] 2026 Cardinals Standings and Record: Regular Seaso
- `search_web({'query': '"Boston Red Sox" record 2026'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Red Sox Gambled on Aroldis Chapman and Now He’s Ma
- `search_web({'query': '"Kansas City Royals" record 2026'})` → [Mon, 18 May 2026] Google News
[Tue, 05 May 2026] Red Sox vs. Royals series matches two struggling t
- `search_web({'query': 'Red Sox vs Royals May 18 2026 pitchers starting lineup'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Red Sox-Royals start time moved up to 6:10 p.m. CT
- `search_web({'query': 'Kansas City Royals Kris Bubic injury IL May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Bubic lands on IL with 'very mild' left elbow sore
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $77,203.00 | 24h: +0.27%

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*