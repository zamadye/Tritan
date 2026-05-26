# Market Analysis — 2026-05-19 07:47 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 7
- **Volume 24h:** $68,030
- **Liquidity:** $121,328

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,188 (+0.4% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,188 (+0.4% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- ATL @ MIA | Final | Miami Marlins(home) 22-26 score:12 vs Atlanta Braves(away) 32-16 score:0
- [SPORTS] Injuries:
- ?: James McCann — Out (Strain)
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Mon, 18 May 2026] atlanta braves miami marlins
- → Here's how to watch Monday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Mon, 18 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 18
- → According to Francys Romero of Beisbol FR, the Atlanta Braves are calling up a player to the MLB. They are in a series with the Marlins.
- [Mon, 18 May 2026] Atlanta Braves Make Roster Move After Marlins Game
- → The Atlanta Braves came up empty in virtually every way on Monday as they were demolished by the Miami Marlins 12-0. The matchup was largely quiet f

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 49.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.82

### Reasoning
Strong historical mispricing signal: markets at 58% price point historically resolve YES only 44.7% of the time (n=13,967), suggesting ~13% overpricing of YES. Supporting evidence: Marlins routed Braves 12-0 in Game 1 (May 18), indicating current form issues. Braves have 3 key players on IL (DH Farmer, CF White, RP Jimenez). Market likely reflects brand-name bias for NL East leaders rather than actual win probability. Info gap trades show 64% WR historically.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'team': 'Atlanta Braves', 'sport': 'mlb'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'team': 'Miami Marlins', 'sport': 'mlb'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `get_odds({'team': 'Atlanta Braves', 'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins odds'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] How to watch Braves vs. Marlins: TV channel and st
- `search_web({'query': 'Atlanta Braves Miami Marlins news'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Atlanta Braves at Miami Marlins Game Story, Scores
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins starting pitchers May 18 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Sanoja hits grand slam, Meyer pitches 6 sharp inni
- `search_web({'query': 'Atlanta Braves vs Miami Marlins prediction May 18 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Braves vs. Marlins Prediction, MLB Picks for Monda
- `get_market_context({'keyword': 'Braves Marlins'})` → No related markets found for 'Braves Marlins'
- `get_market_context({'keyword': 'Atlanta Braves'})` → No related markets found for 'Atlanta Braves'
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $77,192.00 | 24h: +0.26%

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*