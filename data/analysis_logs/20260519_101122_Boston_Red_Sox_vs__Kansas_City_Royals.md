# Market Analysis — 2026-05-19 10:11 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $56,467
- **Liquidity:** $58,688

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,733 (-0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,723 (-0.3% 24h) → neutral

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
- → Boston Red Sox (20-27, fifth in the AL East) vs. Kansas City Royals (20-28, fifth in the AL Central) Kansas City, Missouri; Tuesday, 7:40 p.m. EDT P
- [Mon, 18 May 2026] Red Sox face the Royals with 1-0 series lead
- → Willson Contreras hit his team-leading 10th homer and Sonny Gray outdueled Seth Lugo as the Boston Red Sox beat the Kansas City Royals 3-1.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 51.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.65

### Reasoning
Strong statistical edge from stat signal: markets priced at 55% historically resolve YES only 44.7% of the time (n=13,967), indicating ~10% overpricing of YES. The crowd is systematically overpricing favorites at this price point. Royals have significant pitching injuries (Ragans + Bubic on 15-Day-IL) but market appears to have overcompensated. Pattern data confirms: Entry 50-60% range has only 33% WR (n=6), supporting avoidance of YES in this zone. While gap gate (2% < 5%) was not met, the stat signal provides a more robust edge than the base rate comparison. Previous SKIPs were appropriate given weaker evidence; now statistical signal provides sufficient edge for NO bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_sports_data({'sport': 'mlb', 'team': 'Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] James McArthur (
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals 2025 MLB'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Where to watch Boston Red Sox vs Kansas City Royal
- `search_web({'query': 'Red Sox Royals recent results series preview May 2025'})` → [Wed, 06 Aug 2025] Google News
[Tue, 11 Nov 2025] Kansas City Royals at Boston Red Sox Game Story, S
- `search_web({'query': 'Boston Red Sox record 2025 May wins losses'})` → [Tue, 05 May 2026] Google News
[Tue, 24 Mar 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Kansas City Royals record 2025 May wins losses'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] 2026 MLB Standings and Records: Regular Season - M
- `get_market_context({'keyword': 'Boston Red Sox Kansas City Royals'})` → No related markets found for 'Boston Red Sox Kansas City Royals'
- `search_web({'query': '"Red Sox" "Royals" May 2026 pitching matchup probable starters'})` → [Tue, 19 May 2026] Google News
[Fri, 15 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*