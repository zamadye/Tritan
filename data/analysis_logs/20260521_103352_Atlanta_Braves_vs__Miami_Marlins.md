# Market Analysis — 2026-05-21 10:33 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $94,240
- **Liquidity:** $150,924

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,206 (-0.4% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,556 (+0.1% 24h) → neutral

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
- → The Atlanta Braves have scored a combined 17 runs since being blown out earlier this week ...
- [Thu, 21 May 2026] Braves Throttle Marlins Again, Close in on Another Series Win
- → The Atlanta Braves and Miami Marlins meet Thursday to complete a 4-game series at Loan Depot Park in Miami, Florida. First pitch is at 6:40 p.m. ET.
- [Thu, 21 May 2026] Atlanta Braves at Miami Marlins odds, picks, and predictions
- → Atlanta Braves (34-16, first in the NL East) vs. Miami Marlins (22-28, fourth in the NL East) Miami; Thursday, 6:40 p.m. EDT PITCHING PROBABLES: Bra

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 56% YES historically resolve YES only 44.7% of the time — a ~11% overpricing of YES. Market at 56% is mispriced; true probability closer to 45%. Atlanta has more significant injuries (SP Waldrep 15-Day-IL, C Baldwin 10-Day-IL) vs Miami's minor day-to-day players. No direct game news found, but historical pattern is robust. Note: Entry 50-60% bracket shows only 25% WR historically (12 trades), which tempers confidence. Gap vs base rate is only 3% (<5% gate), but the stat signal itself provides the edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 game preview'})` → [Tue, 19 May 2026] Google News
[Tue, 26 Aug 2025] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Braves Marlins injury update May 2025'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Marlins vs. Braves: Injury Report, Updates &amp; P
- `search_web({'query': 'Atlanta Braves vs Miami Marlins May 27 2025'})` → [Tue, 19 May 2026] Google News
[Wed, 27 Aug 2025] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `get_market_context({'keyword': 'Atlanta Braves Marlins'})` → No related markets found for 'Atlanta Braves Marlins'
- `get_market_context({'keyword': 'Braves'})` → No related markets found for 'Braves'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*