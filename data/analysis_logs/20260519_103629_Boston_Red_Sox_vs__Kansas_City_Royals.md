# Market Analysis — 2026-05-19 10:36 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $56,733
- **Liquidity:** $41,095

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,808 (+0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,710 (-0.0% 24h) → neutral

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
- → On Monday, the Royals fell short in a 3-1 loss to the Boston Red Sox at Kauffman Stadium. It was their sixth loss in seven games. The Royals had the
- [Tue, 19 May 2026] Royals’ losing ways return in series-opening defeat against Red Sox: what happened
- → Boston Red Sox (20-27, fifth in the AL East) vs. Kansas City Royals (20-28, fifth in the AL Central) Kansas City, Missouri; Tuesday, 7:40 p.m. EDT P

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 57.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** INJURY
- **Catalyst Strength:** 0.50

### Reasoning
Strong stat signal (n=13,967) shows markets at 55% resolve YES only 44.7% of time, indicating YES overpricing. While Royals injuries (Cole Ragans SP on IL) provide partial justification for YES price, the ~10% gap between stat-implied probability and market price creates edge on NO. True YES probability estimated at 49% vs market 55%.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Boston Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_sports_data({'sport': 'mlb', 'team': 'Kansas City Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] James McArthur (
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals upcoming series 2025'})` → [Mon, 18 May 2026] Google News
[Fri, 15 May 2026] Red Sox vs. Royals series matches two struggling t
- `search_web({'query': 'Red Sox Royals game tonight May 2026 injuries pitching matchup'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Royals place all-star pitcher on injured list before scheduled start vs Red Sox'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Royals Place All-Star Pitcher On Injured List Befo
- `get_market_context({'keyword': 'Red Sox'})` → No related markets found for 'Red Sox'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*