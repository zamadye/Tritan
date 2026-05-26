# Market Analysis — 2026-05-19 01:36 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $154,065
- **Liquidity:** $487,268

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,668 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,024 (+0.1% 24h) → neutral

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
- → The Los Angeles Dodgers (29-18) take a five-game winning streak down the coast on Monday night to open a three-game series for the National League W
- [Mon, 18 May 2026] How to live stream Dodgers vs Padres: MLB, TV channel
- → The Los Angeles Dodgers and the San Diego Padres open a 3-game series Monday at Petco Park in San Diego, California. First pitch is set for 9:40 p.m
- [Mon, 18 May 2026] LA Dodgers at San Diego Padres odds, picks and predictions
- → The Los Angeles Dodgers (29-18) meet the San Diego Padres( 28-18) to start a three-game series between the NL West rivals. The Dodgers have won five

## LLM Decision
- **Action:** SKIP
- **Confidence:** 64%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURIES_MIXED_SIGNALS
- **Catalyst Strength:** 0.45

### Reasoning
Despite strong stat signal (57% markets resolve YES only 44.7%), the 3% gap is below the 5% threshold, and previous identical decisions were SKIPs. Dodgers have significant pitching injuries (Snell + Glasnow out) which could justify the market discount, but without knowing which side YES represents and no bookmaker odds to cross-reference, the edge is unclear. The base rate (60%) and market (57%) are within noise range. Entry zone (50-60%) has historically weak 40% WR. Insufficient concrete evidence for confident action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Dodgers'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Blake Sne
- `get_sports_data({'sport': 'mlb', 'team': 'San Diego Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Dodgers Padres MLB'})` → No related markets found for 'Dodgers Padres MLB'
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres next game 2025'})` → [Mon, 18 May 2026] Google News
[Wed, 13 Aug 2025] Dodgers–Padres Showdown: Yamamoto and Ohtani Open 
- `search_web({'query': 'Dodgers Padres series preview May 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Padres vs Dodgers Series Preview: Pitching Probabl
- `search_web({'query': '"Dodgers vs Padres" May 2025 MLB odds predictions'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Dodgers vs. Padres Odds, Props, Picks &amp; Predic

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*