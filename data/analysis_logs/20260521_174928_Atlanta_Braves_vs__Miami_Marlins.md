# Market Analysis — 2026-05-21 17:49 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $154,151
- **Liquidity:** $215,362

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,772 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,772 (+0.3% 24h) → neutral
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
- [Thu, 21 May 2026] atlanta braves miami marlins
- → MIAMI (AP) — Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and th
- [Thu, 21 May 2026] Braves beat Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → Here's how to watch Thursday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Thu, 21 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 21
- → The Atlanta Braves are looking to take the final three games of their series against the Miami Marlins after getting shut out 12-0 in the opener. Th

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Contradictory signals prevent confident action: base rate (60%) suggests YES is underpriced by +3%, but strong statistical signal (n=13,967) shows markets at 57% resolve YES only 44.7% of time—indicating typical crowd overpricing. Gap (3%) fails the 5% gate threshold. Past decisions for identical market both SKIPped for same reason. Entry 50-60% bucket shows weakest WR=44% from 18 trades. Injury reports balanced (3 Braves IL vs 3 Marlins DTD/IL). Braves are NL East leaders with Spencer Strider returning, but Marlins just beat them 12-0 recently. No verifiable edge large enough to overcome statistical noise and transaction costs.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Leo Jimenez (3B): 10-Day-IL
INJURY [miami marlins] Thomas White (SP): Day-To-
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins MLB'})` → No related markets found for 'Atlanta Braves Miami Marlins MLB'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 series matchup preview'})` → [Tue, 19 May 2026] Google News
[Tue, 14 Apr 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Atlanta Braves recent form record 2025 MLB'})` → [Mon, 18 May 2026] Google News
[Thu, 23 Apr 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Atlanta Braves record 2026 season standings'})` → [Mon, 18 May 2026] Google News
[Thu, 14 May 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Miami Marlins record 2026 season standings'})` → [Tue, 05 May 2026] Google News
[Sun, 17 May 2026] 2026 Spring Training - MLB.com
[Sun, 10 May 2026] 
- `search_web({'query': '"Atlanta Braves" "Miami Marlins" May 2026 pitching matchup starting pitchers'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'MLB standings 2026 NL East Braves Marlins win loss record'})` → [Tue, 24 Mar 2026] Google News
[Thu, 05 Mar 2026] MLB 2026 season preview: Rankings, every team's pl
- `search_web({'query': 'Marlins vs Braves May 21 2026 game 1 series opener preview prediction'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Braves vs. Marlins Odds, Props, Picks &amp; Predic
- `search_web({'query': 'Atlanta Braves NL East lead 2026 season performance'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Braves vs. Marlins Prediction: Spencer Strider Ret
- `search_web({'query': 'Spencer Strider return Braves May 21 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Fantasy baseball: Mets, Yankees ready to reshape r
- `search_web({'query': 'Miami Marlins 2026 season record wins losses'})` → [Tue, 19 May 2026] Google News
[Tue, 05 May 2026] Miami Marlins crush Atlanta Braves 12-0 in record 
- `search_web({'query': 'Braves Marlins May 21 2026 moneyline odds sportsbook consensus'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Atlanta Braves vs Miami Marlins Odds - Thursday Ma

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*