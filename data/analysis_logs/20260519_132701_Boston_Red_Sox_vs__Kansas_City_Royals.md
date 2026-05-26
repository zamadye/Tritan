# Market Analysis — 2026-05-19 13:27 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $59,855
- **Liquidity:** $267,354

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,742 (-0.8% 24h) → neutral
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
- [Mon, 18 May 2026] Royals’ losing ways return in series-opening defeat against Red Sox: what happened
- → Willson Contreras hit his team-leading 10th homer and Sonny Gray outdueled Seth Lugo as the Boston Red Sox beat the Kansas City Royals 3-1 on Monday
- [Tue, 19 May 2026] Red Sox beat Royals 3-1 behind Willson Contreras’ homer and Sonny Gray’s strong outing
- → Ranger Suarez has been dominant on the mound of late, but he needs some run support from his Boston Red Sox teammates.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MEAN_REVERSION
- **Catalyst Strength:** 0.30

### Reasoning
Stat signal (n=13,967) clearly indicates YES overpriced at 55% (true ~44.7%), giving a theoretical 10% edge for NO. However, no concrete catalyst or breaking news to drive resolution, the 50-60% entry range historically has only 33% WR (6 trades), the base rate gap is only +2% (below 5% gate), and no related markets confirm the edge. Both teams have significant injuries but this cuts both ways. Prior analyses of this exact market reached the same SKIP conclusion. Statistical edge exists in theory but lacks actionable catalyst for the 7-day window.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_sports_data({'sport': 'mlb', 'team': 'Kansas City Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] James McArthur (
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals 2025 series preview prediction'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Red Sox vs. Royals: Prediction, Lineups, How to Wa
- `get_market_context({'keyword': 'Boston Red Sox Kansas City Royals'})` → No related markets found for 'Boston Red Sox Kansas City Royals'
- `search_web({'query': 'Red Sox Royals game today May 2025 injuries starting pitcher'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Fantasy baseball: Gasser, Rodriguez called up for 
- `search_web({'query': 'Kansas City Royals recent results standings 2025'})` → [Tue, 05 May 2026] Google News
[Thu, 13 Nov 2025] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': '"Boston Red Sox" "Kansas City Royals" prediction'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Red Sox vs Royals Prediction, Picks &amp; Odds for

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*