# Market Analysis — 2026-05-21 11:21 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $97,549
- **Liquidity:** $147,223

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,253 (-0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,253 (-0.2% 24h) → neutral

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
- [MULTI-SOURCE NEWS] 1 sources for: atlanta braves miami marlins
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending
- [] Will Donald Trump publicly threaten to raise tariffs on China between
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 50.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_SIGNAL
- **Catalyst Strength:** 0.70

### Reasoning
Historical data shows markets at 56% YES resolve YES only 44.7% of time (n=13,967), indicating YES is overpriced. Braves key injuries (SP Waldrep, C Baldwin, DH Farmer) support NO. However, gap to base rate is only -3% (fails 5% gate), and past decisions were SKIP. Moderate confidence based on strong statistical signal despite small gap.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'team': 'Atlanta Braves', 'sport': 'mlb'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'team': 'Miami Marlins', 'sport': 'mlb'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `search_web({'query': 'Atlanta Braves vs Miami Marlins preview today 2025'})` → [Tue, 19 May 2026] Google News
[Tue, 26 Aug 2025] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Braves Marlins injury report today'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Marlins vs. Braves: Injury Report, Updates &amp; P
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins May 2025 odds prediction'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Braves vs. Marlins Odds, Props, Picks &amp; Predic
- `search_web({'query': 'Braves vs Marlins today MLB game 2025'})` → [Tue, 26 Aug 2025] Google News
[Sat, 09 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `get_odds({'sport': 'baseball_mlb', 'team': 'Miami Marlins'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*