# Market Analysis — 2026-05-19 09:29 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $56,432
- **Liquidity:** $39,496

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,848 (-0.1% 24h) → neutral
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
- → Boston Red Sox (20-27, fifth in the AL East) vs. Kansas City Royals (20-28, fifth in the AL Central) Kansas City, Missouri; Tuesday, 7:40 p.m. EDT. 
- [Mon, 18 May 2026] Red Sox face the Royals with 1-0 series lead
- → Willson Contreras hit his team-leading 10th homer and Sonny Gray outdueled Seth Lugo as the Boston Red Sox beat the Kansas City Royals 3-1.

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.3%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.78

### Reasoning
Market at 55% significantly overprices YES - historical data (n=13,967) shows markets at this price resolve YES only 44.7% of the time, creating a 10.3% edge for NO. Royals have key SP injuries (Cole Ragans AND Kris Bubic both on IL), Red Sox just beat them 3-1. The 2% gap vs base rate is misleading; the stat signal reveals the real mispricing. Sports WR=80% pattern supports conviction, though entry in 50-60% range historically underperforms (33% WR from 6 trades) adds some uncertainty.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `search_web({'query': 'Boston Red Sox injuries update 2025'})` → [Mon, 18 May 2026] Google News
[Tue, 12 May 2026] Red Sox Injury Update: Carlos Narváez diagnosis, R
- `search_web({'query': 'Kansas City Royals injuries update 2025'})` → [Thu, 07 May 2026] Google News
[Tue, 31 Mar 2026] Carlos Estévez Injury Update: Royals Closer Leaves
- `get_sports_data({'sport': 'mlb', 'team': 'Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] James McArthur (
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Red Sox Royals'})` → No related markets found for 'Red Sox Royals'
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals starting pitchers tonight 2026'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Red Sox vs. Royals series matches two struggling t
- `search_web({'query': 'Red Sox vs Royals May 19 2026 probable pitchers lineup'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Red Sox recent results May 2026'})` → [Tue, 19 May 2026] Google News
[Thu, 14 May 2026] Boston Red Sox at Kansas City Royals Game Story, S
- `search_web({'query': 'Royals recent results May 2026'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Kansas City Royals at St. Louis Cardinals Game Sto

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*