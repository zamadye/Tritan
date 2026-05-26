# Market Analysis — 2026-05-21 13:32 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $108,065
- **Liquidity:** $222,515

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,200 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,224 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Final | Miami Marlins(home) 22-28 score:1 vs Atlanta Braves(away) 34-16 score:9
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and the Atlanta Bra
- [Thu, 21 May 2026] Atlanta Braves beat Miami Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → The Miami Marlins will try to halt their slide on Thursday when they send ace Sandy Alcantara to the mound in the finale of their four-game home ser
- [Thu, 21 May 2026] Marlins turn to Sandy Alcantara in quest for series split vs. Braves
- → The Miami Marlins are learning one of baseball’s cruelest lessons in real time. “This game will humble you,” said Marlins starting pitcher Janson Ju

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 57% YES historically resolve YES only 44.7% of the time — a 12.3% edge for NO. Atlanta's key injuries (C, SP, DH on IL) add marginal support. Entry zone pattern confirms 50-60% YES markets consistently overprice YES (38% WR). The stat signal significantly outweighs the 3% base rate gap.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves Marlins'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins MLB'})` → No related markets found for 'Atlanta Braves Miami Marlins MLB'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins upcoming game MLB 2025'})` → [Mon, 25 Aug 2025] Google News
[Sat, 09 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Atlanta Braves recent results August 2025 MLB'})` → [Sun, 31 Aug 2025] Google News
[Sat, 16 Aug 2025] Atlanta Braves at Philadelphia Phillies Game Story
- `search_web({'query': 'Miami Marlins recent results August 2025 MLB'})` → [Sun, 24 Aug 2025] Google News
[Sun, 31 Aug 2025] Toronto Blue Jays at Miami Marlins Game Story, Sco

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*