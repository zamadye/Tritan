# Market Analysis — 2026-05-19 14:21 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $60,614
- **Liquidity:** $270,096

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,487 (-0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,487 (-0.0% 24h) → neutral

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
- → Sonny Gray had arguably the best start of his Boston Red Sox tenure on Monday in the team’s 3-1 win over the Kansas City Royals. Gray was dominant a
- [Tue, 19 May 2026] Royals Slugger Praises Sonny Gray After Dominant Outing
- → On Monday, the Royals fell short in a 3-1 loss to the Boston Red Sox at Kauffman Stadium. It was their sixth loss in seven games. The Royals had the

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Strong stat signal (n=13,967) shows 55% markets resolve YES only 44.7% - clear overpricing. However, gate constraint not met (gap=2% < 5%), entry zone 50-60% shows weak WR=33%, and no new catalytic information. Previous similar decisions skipped with same reasoning.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Boston Red Sox'})` → INJURY [boston red sox] Ceddanne Rafaela (CF): Day-To-Day
INJURY [boston red sox] Carlos Narvaez (C)
- `get_sports_data({'sport': 'mlb', 'team': 'Kansas City Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] James McArthur (
- `search_web({'query': 'Boston Red Sox recent results last 10 games 2025'})` → [Wed, 10 Sep 2025] Google News
[Fri, 15 Aug 2025] Boston Red Sox at Athletics Game Story, Scores/Hig
- `search_web({'query': 'Kansas City Royals recent performance June 2025'})` → [Mon, 02 Mar 2026] Google News
[Fri, 20 Jun 2025] Royals Prospect Eyeing Potential Role With Strong 
- `get_market_context({'keyword': 'Boston Red Sox vs Kansas City Royals'})` → No related markets found for 'Boston Red Sox vs Kansas City Royals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals game odds June 2025'})` → [Fri, 27 Mar 2026] Google News
[Mon, 04 Aug 2025] Here’s what oddsmakers say about the Royals’ 2026 
- `search_web({'query': 'Boston Red Sox win loss record 2025 season'})` → [Tue, 05 May 2026] Google News
[Tue, 17 Mar 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Kansas City Royals win loss record 2025 season standings'})` → [Tue, 05 May 2026] Google News
[Tue, 24 Mar 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': '"Red Sox vs Royals" August 2025 prediction picks'})` → [Wed, 06 Aug 2025] Google News
[Mon, 04 Aug 2025] Red Sox vs. Royals Prediction, Odds, Picks - Augus

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*