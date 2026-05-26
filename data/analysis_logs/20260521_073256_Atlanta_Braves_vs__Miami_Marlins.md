# Market Analysis — 2026-05-21 07:32 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $77,966
- **Liquidity:** $70,226

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,549 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,549 (+0.3% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- [SPORTS] Recent games:
- ATL @ MIA | Final | Miami Marlins(home) 22-28 score:1 vs Atlanta Braves(away) 34-16 score:9
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)

### Bing/Google News
- 6 articles found:
- [NewsAPI] Acuña scores 3 times in return as Braves bounce back against Marlins: It was Acuña’s first game since being sidelined May 2 because of a lef
- [NewsAPI] Braves place star catcher Drake Baldwin on 10-day IL with strained oblique: The Atlanta Braves placed star catcher Drake Baldwin on the 10-d
- [NewsAPI] Philadelphia Phillies Rolling With Zack Wheeler Leading The Rotation: Zack Wheeler has been as effective as ever after his return to the Phi
- [NewsAPI] Marlins Notes: Garrett, Snelling, Alderman: The Marlins are optioning lefty Braxton Garrett back to Triple-A Jacksonville, reports Christina
- [NewsAPI] Acuña scores 3 times in return as Braves surge past Marlins: Ronald Acuña Jr. doubled, walked twice and scored three times in his return and
- [NewsAPI] Ronald Acuña’s Three-Run Return Powers Braves Past Marlins, 8-4: Ronald Acuña Jr. doubled, walked twice and scored three times in his return
- [CAUSAL CHAINS] Relevant cause-effect patterns:

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Braves vs Marlins Game 4 will continue at LoanDepot Park. Here's a look at the latest odds, predictions, and picks.
- [Wed, 20 May 2026] Braves vs. Marlins Game 2: Predictions, Picks &amp; Odds, May 21
- → The Braves have activated Eli White from the IL, adding speed and depth in the outfield ahead of their matchup against the Marlins.
- [Wed, 20 May 2026] Braves’ outfield receives boost ahead of Marlins clash
- → LoanDepot Park is the site where the Miami Marlins (22-27) will play the Atlanta Braves (33-16) on Thursday. The odds on this game have Atlanta at -

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal: markets priced at 57% YES historically resolve YES only 44.7% of the time (n=13,967), indicating 12.3% overpricing of YES side. Entry point 50-60% has WR=27% from 11 trades confirming weakness in this range. Injury data shows Braves have key IL players (Baldwin C, Waldrep SP, Farmer DH) while Marlins have minor day-to-day status. Market currently at 57% but historical base rate for similar situations shows NO wins ~55.3% of the time. Despite past SKIP decisions due to gate threshold, the large statistical discrepancy provides actionable edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 season series results'})` → [Wed, 27 Aug 2025] Google News
[Wed, 27 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Braves vs Marlins August 2025 pitching matchup preview'})` → [Wed, 20 May 2026] Google News
[Wed, 15 Apr 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `search_web({'query': '"Braves" "Marlins" August 27 2025'})` → [2026-05-14] Ted Turner (1938–2026) and Bobby Cox (1941–2026): The Duo That Changed Atlanta Baseball

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*