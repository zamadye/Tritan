# Market Analysis — 2026-05-19 09:01 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $68,506
- **Liquidity:** $91,826

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,032 (+0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,000 (+0.1% 24h) → neutral

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
- [Tue, 19 May 2026] atlanta braves miami marlins
- → Atlanta Braves (32-16, first in the NL East) vs. Miami Marlins (22-26, fourth in the NL East) Miami; Tuesday, 4:10 p.m. EDT PITCHING PROBABLES: Brav
- [Mon, 18 May 2026] Marlins try to keep home win streak going, host the Braves
- → According to Francys Romero of Beisbol FR, the Atlanta Braves are calling up a player to the MLB. They are in a series with the Marlins.
- [Tue, 19 May 2026] Atlanta Braves Make Roster Move After Marlins Game
- → Ronald Acuna Jr. will return to the Atlanta starting lineup on Tuesday when the visiting Braves play the Miami Marlins in the second game of a four-

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MISPRICING_SIGNAL_CONFLICT
- **Catalyst Strength:** 0.40

### Reasoning
Conflicting signals prevent confident trade: (1) STAT SIGNAL strongly suggests YES overpriced (57% markets resolve YES only 44.7% historically, n=13,967), (2) BUT BASE RATE suggests YES slightly underpriced (60% vs 57% market), (3) Gap only 3% fails 5% threshold gate from prior decisions, (4) Pattern data shows weak 33% WR for 50-60% entry range, (5) Injury data balanced (Braves: DH+CF on IL, Marlins: SP on IL), (6) No breaking news catalyst identified—Action Network notes pitching edge but not game-changing. Two prior analyses of this exact market correctly resulted in SKIP for same reasons. Statistical edge exists but insufficient confirmation from independent sources for actionable bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 series preview starting pitchers'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] MLB Picks Today: Greg Peterson Best Bets Tuesday, 
- `search_web({'query': 'Atlanta Braves recent results April 2025'})` → [Wed, 18 Jun 2025] Google News
[Mon, 23 Jun 2025] New York Mets at Atlanta Braves Game Story, Scores
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins MLB'})` → No related markets found for 'Atlanta Braves Miami Marlins MLB'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Braves vs Marlins May 2026 odds moneyline runline'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Atlanta Braves vs Miami Marlins Odds - Tuesday May
- `search_web({'query': 'OddsShark Braves Marlins May 19 2026 moneyline odds'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Atlanta Braves vs Miami Marlins Odds - Tuesday May
- `search_web({'query': '"Braves" "Marlins" "May 19" 2026 odds moneyline favorite underdog'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] How to watch Braves vs. Marlins: TV channel and st
- `search_web({'query': 'Action Network Braves Marlins prediction May 19 2026 moneyline odds'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Braves vs Marlins Prediction, Pick, Odds: Big Edge

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*