# Market Analysis — 2026-05-21 10:49 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $94,877
- **Liquidity:** $144,758

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,240 (-0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,240 (-0.3% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- [SPORTS] Recent games:
- ATL @ MIA | Final | Miami Marlins(home) 22-28 score:1 vs Atlanta Braves(away) 34-16 score:9
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → The Atlanta Braves and Miami Marlins meet Thursday to complete a 4-game series at Loan Depot Park in Miami, Florida. First pitch is at 6:40 p.m. ET.
- [Thu, 21 May 2026] Atlanta Braves at Miami Marlins odds, picks, and predictions
- → The Atlanta Braves have scored a combined 17 runs since being blown out earlier this week ...
- [Thu, 21 May 2026] Braves Throttle Marlins Again, Close in on Another Series Win
- → Atlanta Braves (34-16, first in the NL East) vs. Miami Marlins (22-28, fourth in the NL East) Miami; Thursday, 6:40 p.m. EDT PITCHING PROBABLES: Bra

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MISPRICING
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 56% YES historically resolve YES only 44.7% of the time - significant 11.3% edge on NO side. Braves have more impactful injuries (Baldwin C, Waldrep SP, Farmer DH all on IL) vs Marlins' minor day-to-day players. Historical pattern shows 50-60% entry zone has only 25% win rate (n=12), confirming systematic overpricing in this range. Market overprices YES despite injury disadvantage and base rate of 59%.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 season series results'})` → [Wed, 27 Aug 2025] Google News
[Wed, 27 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Atlanta Braves recent performance 2025 MLB'})` → [Mon, 18 May 2026] Google News
[Tue, 03 Mar 2026] 2026 MLB Standings and Records: Regular Season - M
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins MLB'})` → No related markets found for 'Atlanta Braves Miami Marlins MLB'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Braves vs Marlins August 2025 game preview prediction'})` → [Tue, 26 Aug 2025] Google News
[Tue, 14 Apr 2026] Braves vs. Marlins Prediction, Odds, Picks - Augus
- `search_web({'query': 'Atlanta Braves 2025 record standings wild card'})` → [Mon, 18 May 2026] Google News
[Mon, 01 Sep 2025] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': '"Braves" "Marlins" August 27 2025 game score result'})` → [Wed, 27 Aug 2025] Google News
[Wed, 27 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'MLB playoff race 2025 Atlanta Braves standings'})` → [Sun, 28 Sep 2025] Google News
[Mon, 01 Sep 2025] 2025 MLB playoff picture: Final baseball standings

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*