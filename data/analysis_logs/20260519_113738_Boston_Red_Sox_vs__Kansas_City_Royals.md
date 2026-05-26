# Market Analysis — 2026-05-19 11:37 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $58,931
- **Liquidity:** $83,939

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,814 (+0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,815 (-0.1% 24h) → neutral

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
- → Boston Red Sox (20-27, fifth in the AL East) vs. Kansas City Royals (20-28, fifth in the AL Central) Kansas City, Missouri; Tuesday, 7:40 p.m. EDT. 
- [Tue, 19 May 2026] Red Sox face the Royals with 1-0 series lead
- → Here's how to watch Tuesday's Kansas City Royals vs Boston Red Sox game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 47.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal: markets priced at 55% resolve YES only 44.7% historically (n=13,967), indicating ~10% edge on NO side. Both teams have significant pitching injuries (Red Sox: Roman Anthony IL; Royals: ace Cole Ragans 15-Day-IL, Kris Bubic 15-Day-IL), but the stat signal dominates. Past pattern data confirms 50-60% entry range has only 33% WR (6 trades). Crowd is overpricing YES relative to historical base rates. Macro fear environment (25/100) doesn't directly impact sports but confirms risk-off sentiment.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_sports_data({'sport': 'mlb', 'team': 'Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] James McArthur (
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals 2025 series preview'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Series Preview: Red Sox at Royals - Over the Monst
- `search_web({'query': 'Red Sox Royals July 2025 pitching matchup'})` → [Mon, 30 Mar 2026] Google News
[Tue, 05 Aug 2025] Predicting winners in MLB on Monday, March 30th, 2
- `search_web({'query': 'Red Sox recent results July 2025'})` → [Tue, 29 Jul 2025] Google News
[Fri, 11 Jul 2025] Boston Red Sox at Minnesota Twins Game Story, Scor
- `search_web({'query': 'Royals recent results July 2025'})` → [Sat, 26 Jul 2025] Google News
[Mon, 28 Jul 2025] Cleveland Guardians at Kansas City Royals Game Sto
- `search_web({'query': 'Red Sox vs Royals 2025 head to head record'})` → [Fri, 15 May 2026] Google News
[Mon, 18 May 2026] Diving into all 15 Rivalry Weekend matchups - MLB.
- `get_market_context({'keyword': 'Red Sox Royals'})` → No related markets found for 'Red Sox Royals'
- `search_web({'query': 'MLB standings July 2025 AL East AL Central'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Red Sox starting pitcher July 2025'})` → [Sat, 18 Oct 2025] Google News
[Thu, 02 Oct 2025] Grading The 2025 Boston Red Sox: Starting Pitchers
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*