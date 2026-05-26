# Market Analysis — 2026-05-21 19:20 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $195,053
- **Liquidity:** $236,675

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,483 (+0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,374 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [] atlanta braves miami marlins
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 60.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Stat signal indicates market overprices YES (44.7% vs 57%), but entry zone 50-60% has poor 42% win rate historically, gap below threshold at 3%, and no direct catalyst. Previous similar analyses also resulted in SKIP.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `search_web({'query': 'Atlanta Braves vs Miami Marlins game 2025'})` → [Tue, 26 Aug 2025] Google News
[Sat, 09 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Braves Marlins series August 2025 preview'})` → [Tue, 26 Aug 2025] Google News
[Sat, 09 Aug 2025] Atlanta Braves at Miami Marlins Preview - 08/27/20
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves recent results August 2025'})` → [Sun, 31 Aug 2025] Google News
[Sat, 16 Aug 2025] Atlanta Braves at Philadelphia Phillies Game Story
- `search_web({'query': 'Miami Marlins recent results August 2025'})` → [Sun, 03 Aug 2025] Google News
[Sun, 24 Aug 2025] New York Yankees at Miami Marlins Game Story, Scor

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*