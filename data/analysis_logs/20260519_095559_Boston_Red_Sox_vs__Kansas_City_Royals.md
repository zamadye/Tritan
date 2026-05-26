# Market Analysis — 2026-05-19 09:55 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $56,457
- **Liquidity:** $57,454

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,744 (-0.2% 24h) → neutral
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
- → Boston Red Sox (20-27, fifth in the AL East) vs. Kansas City Royals (20-28, fifth in the AL Central) Kansas City, Missouri; Tuesday, 7:40 p.m. EDT .
- [Mon, 18 May 2026] Red Sox face the Royals with 1-0 series lead
- → The Royals are scheduled to kick off their 9-game homestand with a series opener against Boston at The K on Monday night.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 49.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical edge: markets priced at 55% historically resolve YES only 44.7% (n=13,967) — a ~10% overpricing. While base rate gap (2%) is below 5% threshold, the historical resolution data provides direct quantitative evidence the crowd is overpricing YES. Royals have more impactful injuries (Cole Ragans SP on IL) vs Red Sox day-to-day players. No breaking news or new catalyst needed — the persistent market overpricing IS the edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_sports_data({'sport': 'mlb', 'team': 'Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] James McArthur (
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Boston Red Sox Kansas City Royals'})` → No related markets found for 'Boston Red Sox Kansas City Royals'
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals game 2025 preview odds'})` → [Wed, 06 Aug 2025] Google News
[Fri, 13 Feb 2026] Red Sox vs. Royals Prediction, Odds, Picks - Augus
- `search_web({'query': 'Red Sox Royals August 2025 series pitching matchup'})` → [Thu, 09 Apr 2026] Google News
[Tue, 05 Aug 2025] Predicting the winner of every MLB game on Thursda
- `search_web({'query': '"Red Sox" "Royals" today game 2025 injury update'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Red Sox Injury Update: Carlos Narváez diagnosis, R

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*