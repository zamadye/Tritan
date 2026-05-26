# Market Analysis — 2026-05-19 09:16 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $56,429
- **Liquidity:** $34,285

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,988 (+0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,982 (+0.0% 24h) → neutral

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
- → Willson Contreras hit his team-leading 10th homer and Sonny Gray outdueled Seth Lugo as the Boston Red Sox beat the Kansas City Royals 3-1 on Monday

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** PITCHING_INJURY
- **Catalyst Strength:** 0.40

### Reasoning
Royals SP Kris Bubic placed on IL (15-day, elbow soreness) - he was scheduled starter. This hurts KC. However: (1) Market overprices YES by 10.3% historically at 55% price (n=13,967 resolves YES only 44.7%), (2) Entry gap only +2% vs 5% minimum threshold, (3) Pattern shows 50-60% entry WR=33% (weak), (4) Prior decisions correctly identified stat edge but gate failed. While Bubic IL is a real catalyst favoring Red Sox, the structural overpricing at this price point dominates. Historical stat edge suggests NO has ~55% true probability vs market's 55% YES price. Not enough concrete edge to justify bet given weak entry range track record.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_sports_data({'sport': 'mlb', 'team': 'Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] James McArthur (
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals 2025 season record standings'})` → [Tue, 05 May 2026] Google News
[Mon, 04 Aug 2025] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Red Sox Royals starting pitchers matchup 2025'})` → [Mon, 20 Apr 2026] Google News
[Wed, 15 Apr 2026] Yankees, Red Sox renew rivalry tonight: Pitching m
- `search_web({'query': 'Red Sox vs Royals May 2025 starting pitcher matchup'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Royals Place All-Star Pitcher On Injured List Befo
- `search_web({'query': 'Boston Red Sox injuries recent news May 2025'})` → [Sun, 17 May 2026] Google News
[Tue, 17 Feb 2026] Fantasy baseball: Gasser, Rodriguez called up for 
- `search_web({'query': 'Kansas City Royals injury update Kris Bubic status May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Royals Rotation Takes Another Hit Following Latest
- `get_market_context({'keyword': 'Red Sox Royals MLB'})` → No related markets found for 'Red Sox Royals MLB'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*