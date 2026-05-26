# Market Analysis — 2026-05-21 15:09 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $131,869
- **Liquidity:** $586,263

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,959 (-0.4% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,894 (-0.7% 24h) → neutral
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
- → The St. Louis Cardinals look to win the series at home against the Pittsburgh Pirates on Thursday afternoon. The Cardinals won Game 1, 9-6, while th
- [Thu, 21 May 2026] Pirates vs. Cardinals prediction, odds, time: 2026 MLB picks for Thursday, May 21 from proven model
- → The Pittsburgh Pirates (24-24) are on their way to Busch Stadium on Thursday where they will attempt to beat the St. Louis Cardinals (28-19). The li
- [Wed, 20 May 2026] Pittsburgh Pirates vs St. Louis Cardinals Prediction, 5/21/2026 MLB Picks, Best Bets &amp; Odds
- → Spencer Horwitz homered, Konnor Griffin had four singles, and the Pittsburgh Pirates beat the St. Louis Cardinals 7-0 to snap a four-game losing str

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 51.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Statistical signal shows YES overpriced (51% market vs 44.7% historical), but gap from base rate only 1% (below 5% threshold), no game-specific catalyst identified, and 50-60% entry range historically weak (38% WR). Both teams have balanced injuries with no clear edge. Insufficient concrete evidence for bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals 2025 series preview'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pirates vs Cardinals Prediction, Picks &amp; Odds 
- `search_web({'query': 'Pittsburgh Pirates recent form injuries 2025'})` → [Tue, 12 Aug 2025] Google News
[Wed, 28 Jan 2026] Oneil Cruz leaves game with apparent injury - MLB.
- `get_market_context({'keyword': 'Pirates Cardinals'})` → No related markets found for 'Pirates Cardinals'
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `search_web({'query': 'St. Louis Cardinals recent results May 2025'})` → [Sat, 31 May 2025] Google News
[Fri, 30 May 2025] St. Louis Cardinals at Texas Rangers Game Story, S
- `search_web({'query': 'Pittsburgh Pirates 2025 season record standings'})` → [Tue, 05 May 2026] Google News
[Fri, 11 Jul 2025] 2026 Spring Training - MLB.com
[Thu, 26 Mar 2026] 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*