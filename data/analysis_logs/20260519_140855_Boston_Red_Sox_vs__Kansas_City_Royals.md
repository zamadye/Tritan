# Market Analysis — 2026-05-19 14:08 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $59,972
- **Liquidity:** $261,293

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,811 (+0.0% 24h) → neutral
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
- → The Boston Red Sox (19-26) are hitting the road to Kauffman Stadium on Wednesday where they will attempt to beat the Kansas City Royals (19-27). The
- [Tue, 19 May 2026] Boston Red Sox vs Kansas City Royals Prediction, 5/20/2026 MLB Picks, Best Bets &amp; Odds
- → On Monday, the Royals fell short in a 3-1 loss to the Boston Red Sox at Kauffman Stadium. It was their sixth loss in seven games. The Royals had the
- [Tue, 19 May 2026] Royals’ losing ways return in series-opening defeat against Red Sox: what happened
- → Boston Red Sox (20-27, fifth in the AL East) vs. Kansas City Royals (20-28, fifth in the AL Central) Kansas City, Missouri; Tuesday, 7:40 p.m. EDT. 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 63%
- **p_true:** 49.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows markets at 55% resolve YES only 44.7% of the time — a ~10pp edge for NO. Crowd overpricing YES. However, confidence limited to 0.63 due to: (1) no fresh catalyst or information gap, (2) entry zone 50-60% has historically poor WR (33%), and (3) gap is only 2% vs 5% threshold. Both teams have known injuries unlikely to move market. Edge exists but is purely statistical, not catalytic.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_sports_data({'sport': 'mlb', 'team': 'Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] James McArthur (
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals April 2025'})` → [Mon, 18 May 2026] Google News
[Sun, 26 Apr 2026] Royals game vs. Red Sox moved up due to severe wea
- `search_web({'query': 'Red Sox Royals injury report lineup April 2025'})` → [Tue, 19 May 2026] Google News
[Wed, 29 Apr 2026] MLB 2026 Buzz: Nationals Plan to Recall Former No.
- `get_market_context({'keyword': 'Red Sox Royals'})` → No related markets found for 'Red Sox Royals'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*