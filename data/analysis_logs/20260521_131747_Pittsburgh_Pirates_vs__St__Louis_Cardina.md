# Market Analysis — 2026-05-21 13:17 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $79,532
- **Liquidity:** $242,891

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,255 (-0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,189 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: pittsburgh pirates louis cardinals
- [Bing News]
- [Thu, 21 May 2026] pittsburgh pirates louis cardinals
- → The Pittsburgh Pirates (24-24) are on their way to Busch Stadium on Thursday where they will attempt to beat the St. Louis Cardinals (28-19). The li
- [Wed, 20 May 2026] Pittsburgh Pirates vs St. Louis Cardinals Prediction, 5/21/2026 MLB Picks, Best Bets &amp; Odds
- → Spencer Horwitz homered, Konnor Griffin had four singles, and the Pittsburgh Pirates beat the St. Louis Cardinals 7-0 to snap a four-game losing str
- [Thu, 21 May 2026] Spencer Horwitz homers, Konnor Griffin has four hits to help Pirates blank Cardinals 7-0
- → Pittsburgh Pirates (25-24, fifth in the NL Central) vs. St. Louis Cardinals (28-20, second in the NL Central) St. Louis; Thursday, 1:15 p.m. EDT PIT

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals 2025 matchup'})` → [Wed, 20 May 2026] Google News
[Wed, 29 Apr 2026] Pirates vs. Cardinals (21 May, 2026) Live Score - 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'MLB Pirates Cardinals injuries 2025'})` → [Thu, 29 Jan 2026] Google News
[Tue, 26 Aug 2025] Is St. Louis baseball's safest place to pitch? Car
- `search_web({'query': 'Pirates vs Cardinals odds 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pirates vs. Cardinals (May 21, 2026) Odds and Spre
- `search_web({'query': 'Pirates vs Cardinals moneyline odds May 21 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pirates vs. Cardinals (May 21, 2026) Odds and Spre

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*