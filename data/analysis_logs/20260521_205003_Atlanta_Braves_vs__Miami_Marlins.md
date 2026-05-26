# Market Analysis — 2026-05-21 20:50 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $216,244
- **Liquidity:** $229,575

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,661 (+0.0% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,637 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Here's how to watch Thursday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Thu, 21 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 21
- → MIAMI (AP) — Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and th
- [Thu, 21 May 2026] Braves beat Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → Atlanta Braves roster update: veteran pitcher Carlos Carrasco is back in the spotlight as the team faces the Marlins.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 48%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
SKIP - Insufficient edge despite stat signal. Stat signal (n=13,967) suggests market at 57% overprices YES (historical resolution 44.7%), but this contradicts the 60% base rate for Atlanta Braves. Gate check FAILS: market-to-base-rate gap is only +3%, below the 5% threshold. No specific catalyst, news, or verifiable information directly affecting this matchup's outcome. Prior 2 identical attempts on same market both SKIPped for same reason. Entry 50-60% range has weak 42% WR (n=19). Conflicting signals + no catalyst = cannot identify actionable edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Hurston Waldrep (SP): 60-Day-IL
INJURY [atlanta braves] Drake Baldwin (C): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Robby Snelling (SP): 60-Day-IL
INJURY [miami marlins] Leo Jimenez (3B): 7-day
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves vs Miami Marlins'})` → No related markets found for 'Atlanta Braves vs Miami Marlins'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins June 2025 prediction'})` → [Mon, 25 Aug 2025] Google News
[Tue, 14 Apr 2026] Braves vs. Marlins Prediction, Odds, Picks - Augus
- `search_web({'query': 'Atlanta Braves upcoming schedule pitchers 2025'})` → [Thu, 19 Feb 2026] Google News
[Tue, 11 Nov 2025] Braves Pitching Injuries Create Perfect Opportunit
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $77,707.00 | 24h: +0.06%

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*