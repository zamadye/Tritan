# Market Analysis — 2026-05-19 00:10 UTC

## Market
- **Question:** Cleveland Guardians vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 40.0%
- **Days Left:** 6
- **Volume 24h:** $531,656
- **Liquidity:** $84,963

## Statistical Prior
- **p_base:** 35.2%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,966 (-0.6% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,999 (-0.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- CLE @ DET | In Progress | Detroit Tigers(home) 20-27 score:1 vs Cleveland Guardians(away) 26-22 score:2
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: cleveland guardians detroit tigers
- [Bing News]
- [Mon, 18 May 2026] cleveland guardians detroit tigers
- → The Cleveland Guardians (25-22) are traveling to Comerica Park on Tuesday where they will attempt to beat the Detroit Tigers (20-26). The moneyline 
- [Mon, 18 May 2026] Cleveland Guardians vs Detroit Tigers Prediction, 5/19/2026 MLB Picks, Best Bets &amp; Odds
- → The Detroit Tigers and Cleveland Guardians entered a rain delay before the start of Monday's series opener due to inclement weather at Comerica Park
- [Mon, 18 May 2026] Detroit Tigers weather, rain delay vs Guardians comes to an end
- → The Detroit Tigers and Cleveland Guardians are finally underway after a 43-minute rain delay at Comerica Park. Originally scheduled for 6:40 p.m., t

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 35.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_IMPACT
- **Catalyst Strength:** 0.55

### Reasoning
Despite Detroit Tigers missing two key pitchers (Skubal 15-Day IL, Verlander 60-Day IL), the 5% gap (40% price vs 35% base rate) only exactly meets the gate threshold, not clearly exceeds it. The 40-50% entry range shows historically weak WR of 33% (n=3). Past identical market was SKIP at 4% gap; the incremental 1% improvement doesn't provide sufficient edge. Crowd may be overreacting to injuries (bias=true), but without verifiable data that true probability significantly exceeds 40%, the edge is insufficient for a confident bet. The injury news appears partially priced in given previous market discussions.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Cleveland Guardians'})` → INJURY [cleveland guardians] Gabriel Arias (SS): 10-Day-IL
INJURY [cleveland guardians] Carlos Herna
- `get_sports_data({'sport': 'mlb', 'team': 'Detroit Tigers'})` → INJURY [detroit tigers] Tarik Skubal (SP): 15-Day-IL
INJURY [detroit tigers] Troy Melton (RP): 60-Da
- `search_web({'query': 'Cleveland Guardians vs Detroit Tigers May 2025 series preview'})` → [Mon, 18 May 2026] Google News
[Tue, 16 Sep 2025] Cleveland Guardians at Detroit Tigers odds, picks 
- `search_web({'query': 'Detroit Tigers pitching injuries Skubal Verlander 2025'})` → [Fri, 15 May 2026] Google News
[Mon, 04 May 2026] Tigers pitcher Casey Mize to start Saturday's game
- `search_web({'query': 'Cleveland Guardians vs Detroit Tigers May 2025 game'})` → [Wed, 29 Apr 2026] Google News
[Wed, 17 Sep 2025] Cleveland Guardians TV schedule 2026: How to watch
- `search_web({'query': 'MLB games today May 2025 Guardians Tigers'})` → [Wed, 29 Apr 2026] Google News
[Wed, 24 Sep 2025] Cleveland Guardians TV schedule 2026: How to watch
- `get_market_context({'keyword': 'Cleveland Guardians Detroit Tigers'})` → No related markets found for 'Cleveland Guardians Detroit Tigers'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*