# Market Analysis — 2026-05-21 22:04 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $247,011
- **Liquidity:** $168,597

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,577 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,700 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)
- ?: A.J. Puk — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → The Atlanta Braves are looking to take the final three games of their series against the Miami Marlins after getting shut out 12-0 in the opener. Th
- [Thu, 21 May 2026] Braves vs. Marlins Prediction, Odds, Probable Pitchers, Prop Bets for Thursday, May 21
- → The Braves are the best team in baseball and there is no denying that. On Wednesday, they just did something for the first time in over two decades.
- [Thu, 21 May 2026] Atlanta Braves just did something the organization hasn't done since 2003 with win over Marlins
- → MIAMI (AP) — Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and th

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Market shows 57% YES vs base rate 60% (gap only +3%, below 5% threshold). While statistical signal indicates overpricing (44.7% historical YES rate at 57%), this conflicts with base rate. Injury data shows similar impact on both teams (3 IL each - Braves: Waldrep, Baldwin, Farmer; Marlins: Snelling, Jimenez, White). Entry range 50-60% has weak WR=42%. Two prior decisions on identical market were SKIP due to insufficient edge. No bookmaker odds available to confirm. No verifiable catalyst found.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Hurston Waldrep (SP): 60-Day-IL
INJURY [atlanta braves] Drake Baldwin (C): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 60-Day-IL
INJURY [miami marlins] Leo Jimenez (3B): 7-day
- `search_web({'query': 'Atlanta Braves recent results June 2025'})` → [Sat, 28 Jun 2025] Google News
[Wed, 18 Jun 2025] Philadelphia Phillies at Atlanta Braves Game Story
- `search_web({'query': 'Miami Marlins recent results June 2025'})` → [Thu, 19 Jun 2025] Google News
[Tue, 17 Jun 2025] Philadelphia Phillies at Miami Marlins Game Story,
- `search_web({'query': 'Braves vs Marlins series July 2025 MLB schedule'})` → [Sun, 10 Aug 2025] Google News
[Sat, 09 Aug 2025] Braves building momentum as they take 4 of 5 from 
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*