# Market Analysis — 2026-05-19 00:33 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $135,586
- **Liquidity:** $478,550

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,194 (+0.1% 24h) → neutral
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
- → Petco Park is the location where the San Diego Padres (27-18) will take on the Los Angeles Dodgers (28-18) on Tuesday. The moneyline on this game ha
- [Mon, 18 May 2026] Los Angeles Dodgers vs San Diego Padres Prediction, 5/19/2026 MLB Picks, Best Bets &amp; Odds
- → The Los Angeles Dodgers (29-18) meet the San Diego Padres( 28-18) to start a three-game series between the NL West rivals. The Dodgers have won five

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Tyler Glasnow (SP): 15-Day-IL
INJURY [los angeles dodgers] Ben Caspariu
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres odds 2025'})` → [Mon, 18 May 2026] Google News
[Sun, 24 Aug 2025] LA Dodgers at San Diego Padres odds, picks and pre
- `search_web({'query': 'Dodgers Padres game today odds prediction'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Dodgers vs Padres Prediction: Odds, recent stats, 
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*