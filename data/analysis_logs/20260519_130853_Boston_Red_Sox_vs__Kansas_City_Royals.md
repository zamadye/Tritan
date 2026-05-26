# Market Analysis — 2026-05-19 13:08 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $59,633
- **Liquidity:** $262,042

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,890 (-0.7% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,791 (-0.9% 24h) → neutral

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
- → On Monday, the Royals fell short in a 3-1 loss to the Boston Red Sox at Kauffman Stadium. It was their sixth loss in seven games. The Royals had the
- [Tue, 19 May 2026] Royals’ losing ways return in series-opening defeat against Red Sox: what happened
- → Ranger Suarez has been dominant on the mound of late, but he needs some run support from his Boston Red Sox teammates.
- [Tue, 19 May 2026] Behind Ranger Suarez, Red Sox eager to continue Royals' woes
- → Here's how to watch Tuesday's Kansas City Royals vs Boston Red Sox game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 49.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows markets at 55% resolve YES only 44.7% of the time — a 10.3% edge on NO. While the 2% gap vs base rate doesn't meet the typical 5% gate, the large-sample historical pattern at this exact price point is highly reliable and independent. Red Sox have 3 injury concerns (Rafaela, Narvaez, Anthony on IL), and recent game they won 3-1 may create recency bias inflating YES price. Sports pattern is strong (81% WR), and extreme macro fear (25/100) suggests market may be overconfident on favorites. Past skip decisions lacked catalyst — but the systematic mispricing pattern IS the catalyst. Confidence tempered to 0.65 due to missing starting pitcher data and the entry price pattern (50-60% = 33% WR).

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `search_web({'query': 'Boston Red Sox Kansas City Royals recent game results'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Where to watch Boston Red Sox vs Kansas City Royal
- `search_web({'query': 'Red Sox vs Royals score May 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Boston Red Sox at Kansas City Royals Game Story, S
- `get_market_context({'keyword': 'Red Sox Royals'})` → No related markets found for 'Red Sox Royals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'
- `search_web({'query': 'Boston Red Sox Kansas City Royals series May 2026 predictions starting pitchers'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Red Sox vs Royals Picks and Best Bet for May 19, 2

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*