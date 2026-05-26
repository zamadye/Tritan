# Market Analysis — 2026-05-21 00:31 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 60.0%
- **Days Left:** 6
- **Volume 24h:** $152,250
- **Liquidity:** $42,627

## Statistical Prior
- **p_base:** 64.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.7%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,616 (+1.3% 24h) → risk-ON
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,616 (+1.3% 24h) → risk-ON
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: pittsburgh pirates louis cardinals
- [Bing News]
- [Wed, 20 May 2026] pittsburgh pirates louis cardinals
- → The Pittsburgh Pirates have a new look outfield vs. the Cardinals.
- [Wed, 20 May 2026] Pirates Make Big Outfield Adjustment Before Cardinals Game
- → Cardinals star Ivan Herrera revealed the team’s chemistry after his home run lifted St. Louis past the Pirates in a key NL Central battle.
- [Tue, 19 May 2026] Ivan Herrera reveals Cardinals’ secret for success after walk-off home run vs. Pirates
- → The Pittsburgh Pirates and St. Louis Cardinals meet Wednesday at Busch Stadium in St. Louis, Missouri. First pitch is at 7:45 p.m. ET.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 54.8%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** SYSTEMATIC_MARKET_OVERPRICING
- **Catalyst Strength:** 0.75

### Reasoning
STAT SIGNAL from n=13,967 shows markets at 60% resolve YES only 44.7% of time, indicating YES is overpriced by ~15%. Large sample historical edge overrides base rate signal. EV on NO ≈ +8% at current 60% price.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `get_market_context({'keyword': 'Pittsburgh Pirates Cardinals'})` → No related markets found for 'Pittsburgh Pirates Cardinals'
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals May 2025 series preview'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Pittsburgh Pirates vs. St. Louis Cardinals predict
- `search_web({'query': 'Pittsburgh Pirates recent results May 2025'})` → [Sat, 05 Jul 2025] Google News
[Sat, 31 May 2025] Pittsburgh Pirates at Seattle Mariners Game Story,
- `search_web({'query': 'St. Louis Cardinals recent results May 2025'})` → [Tue, 05 May 2026] Google News
[Sat, 31 May 2025] 2026 MLB Standings and Records: Spring Training - 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': '"Pittsburgh Pirates" "St. Louis Cardinals" series results 2025'})` → [Tue, 26 Aug 2025] Google News
[Wed, 13 May 2026] Pittsburgh Pirates at St. Louis Cardinals Game Sto
- `search_web({'query': 'MLB standings 2025 Pittsburgh Pirates St. Louis Cardinals'})` → [Tue, 05 May 2026] Google News
[Thu, 30 Apr 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Pittsburgh Pirates win rate vs Cardinals 2025'})` → No search results for: Pittsburgh Pirates win rate vs Cardinals 2025
- `search_web({'query': 'St. Louis Cardinals pitching rotation May 2025'})` → [Wed, 04 Mar 2026] Google News
[Sun, 01 Feb 2026] Cardinals Considering Unorthodox Rotation to Kick 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*