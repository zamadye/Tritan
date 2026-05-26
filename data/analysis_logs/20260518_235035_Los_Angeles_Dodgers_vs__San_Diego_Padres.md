# Market Analysis — 2026-05-18 23:50 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $129,584
- **Liquidity:** $546,136

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,037 (-0.1% 24h) → neutral
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,980 (-1.1% 24h) → risk-OFF

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)
- ?: Max Muncy — 10-Day-IL (Fracture)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: angeles dodgers diego padres
- [Bing News]
- [Mon, 18 May 2026] angeles dodgers diego padres
- → Siani only spent three months with the Dodgers organization after being claimed in February. The 26-year-old outfielder never appeared in a Major Le
- [Mon, 18 May 2026] Dodgers Lose Player to Orioles Before Padres Game
- → Petco Park is the location where the San Diego Padres (27-18) will take on the Los Angeles Dodgers (28-18) on Tuesday. The moneyline on this game ha
- [Mon, 18 May 2026] Los Angeles Dodgers vs San Diego Padres Prediction, 5/19/2026 MLB Picks, Best Bets &amp; Odds
- → The Los Angeles Dodgers (29-18) meet the San Diego Padres( 28-18) to start a three-game series between the NL West rivals. The Dodgers have won five

## LLM Decision
- **Action:** SKIP
- **Confidence:** 63%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
No verifiable edge. Contradictory signals (base rate 60% suggests underpriced YES, but stat signal shows 57% markets resolve YES only 44.7%). Gap of 3% below 5% gate threshold. Both teams have starting pitchers on IL (Snell for LAD, Marquez for SDP) — injuries appear balanced. No breaking news or catalyst found. Pattern data shows 40% WR in 50-60% price zone. Consistent with two prior SKIP decisions on identical market.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Dodgers'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Jack Drey
- `get_sports_data({'sport': 'mlb', 'team': 'San Diego Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Los Angeles Dodgers recent results 2025'})` → [Tue, 16 Sep 2025] Google News
[Sat, 01 Nov 2025] Philadelphia Phillies at Los Angeles Dodgers Game 
- `search_web({'query': 'San Diego Padres recent results 2025'})` → [Tue, 29 Jul 2025] Google News
[Thu, 18 Sep 2025] New York Mets at San Diego Padres Game Story, Scor
- `search_web({'query': 'Dodgers injury update Blake Snell'})` → [Sat, 16 May 2026] Google News
[Fri, 15 May 2026] How Dodgers could navigate starting rotation witho
- `search_web({'query': 'Padres injury update German Marquez'})` → [Sun, 17 May 2026] Google News
[Sun, 03 May 2026] Dodgers vs. Padres Series Injured List - May 18-20
- `get_market_context({'keyword': 'Dodgers vs Padres'})` → No related markets found for 'Dodgers vs Padres'
- `get_market_context({'keyword': 'Dodgers'})` → No related markets found for 'Dodgers'
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*