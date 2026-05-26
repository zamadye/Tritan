# Market Analysis — 2026-05-19 00:20 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $133,505
- **Liquidity:** $510,350

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,068 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,946 (-0.6% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)
- ?: Max Muncy — 10-Day-IL (Fracture)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: angeles dodgers diego padres
- [Bing News]
- [Mon, 18 May 2026] angeles dodgers diego padres
- → Siani only spent three months with the Dodgers organization after being claimed in February. The 26-year-old outfielder never appeared in a Major Le
- [Mon, 18 May 2026] Dodgers Lose Player to Orioles Before Padres Game
- → The Los Angeles Dodgers (29-18) meet the San Diego Padres( 28-18) to start a three-game series between the NL West rivals. The Dodgers have won five
- [Mon, 18 May 2026] Where to watch Los Angeles Dodgers vs. San Diego Padres: Live stream, TV channel, odds for Monday, May 18
- → Emmet Sheehan will do something no Dodgers pitcher has done yet in 2026 on Tuesday night against the San Diego Padres at Petco Park. Sheehan will st

## LLM Decision
- **Action:** SKIP
- **Confidence:** 48%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Contradictory signals prevent confident action. Base rate (60%) > Market (57%) suggests YES slightly underpriced (+3% gap), BUT stat signal (n=13,967) shows markets at 57% resolve YES only 44.7% of time — indicating YES is overpriced. Gap of 3% is below 5% gate threshold. Both teams have comparable injury situations (Dodgers: 3 relievers on IL; Padres: SP Márquez, C Campusano on IL). Dodgers entering on win streak but no decisive edge emerges. Two previous decisions on this exact market also SKIPped for same contradictory signal reasons. Entry in 50-60% range historically has only 40% WR — worst performing bracket. No new catalyst or breaking news to break the tie.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Ben Casparius (RP): 60-Day-IL
INJURY [los angeles dodgers] Brusdar Grat
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres game 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Padres Lineup vs Dodgers: Fernando Tatis Leading O
- `search_web({'query': 'Dodgers Padres series 2025'})` → [Mon, 18 May 2026] Google News
[Sun, 24 Aug 2025] Dodgers Preview: Dodgers–Padres Showdown: Yamamoto
- `search_web({'query': 'Dodgers Padres upcoming game 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Dodgers Vs. Padres: The Biggest Three-Game Series 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres May 2026 pitching matchup'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Dodgers vs Padres Prediction: Odds, recent stats, 
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `search_web({'query': 'San Diego Padres injuries roster May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Dodgers vs. Padres Series Injured List - May 18-20
- `search_web({'query': 'Dodgers win streak Padres May 18 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Dodgers take win streak into matchup with the Padr
- `search_web({'query': 'Dodgers recent results May 2026'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Los Angeles Dodgers at Los Angeles Angels Game Sto
- `search_web({'query': 'Dodgers last 10 games results May 2026'})` → [Sun, 17 May 2026] Google News
[Wed, 01 Apr 2026] Dodgers 10-1 Angels (May 17, 2026) Game Recap - ES
- `search_web({'query': 'Padres last 10 games results May 2026'})` → [Sat, 16 May 2026] Google News
[Sun, 10 May 2026] Padres 2-0 Mariners (May 15, 2026) Game Recap - ES

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*