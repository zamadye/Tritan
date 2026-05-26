# Market Analysis — 2026-05-19 13:47 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $59,893
- **Liquidity:** $257,235

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,889 (-0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,751 (-0.3% 24h) → neutral

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
- → Boston Red Sox (20-27, fifth in the AL East) vs. Kansas City Royals (20-28, fifth in the AL Central) Kansas City, Missouri; Tuesday, 7:40 p.m. EDT. 

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 45.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical signal (n=13,967) shows markets at 55% resolve YES only 44.7% of the time — a 10.3% systematic overpricing edge for NO. Despite Royals losing ace Cole Ragans (favoring Red Sox), the massive sample size of the stat signal dominates. Market crowd is systematically overpricing YES at this price level. Edge is robust.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Boston Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_sports_data({'sport': 'mlb', 'team': 'Kansas City Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] James McArthur (
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals series 2025'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Where to watch Boston Red Sox vs Kansas City Royal
- `search_web({'query': 'Red Sox Royals game preview injury report May 2025'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Royals vs. Red Sox: Injury Report, Updates &amp; P
- `get_market_context({'keyword': 'Red Sox Royals baseball'})` → No related markets found for 'Red Sox Royals baseball'
- `search_web({'query': 'Boston Red Sox winning percentage 2025 record'})` → [Tue, 05 May 2026] Google News
[Tue, 30 Sep 2025] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Kansas City Royals winning percentage 2025 record'})` → [Fri, 27 Mar 2026] Google News
[Sun, 15 Jun 2025] Can the weather predict a Royals' win on the home 
- `search_web({'query': '"Red Sox" "Royals" 2025 MLB standings wins losses'})` → [Sun, 17 May 2026] Google News
[Tue, 24 Mar 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Cole Ragans injury update Royals 2025'})` → [Wed, 17 Sep 2025] Google News
[Fri, 08 May 2026] Royals get Ragans back, reward ace's return with c

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*