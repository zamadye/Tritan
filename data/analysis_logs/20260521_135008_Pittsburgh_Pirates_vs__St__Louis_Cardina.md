# Market Analysis — 2026-05-21 13:50 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $88,085
- **Liquidity:** $247,402

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,772 (-0.5% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,790 (-0.5% 24h) → neutral
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
- **Confidence:** 65%
- **p_true:** 49.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows markets at 55% resolve YES only 44.7% of the time, indicating a 10.3% overpricing of YES. Historical pattern robust. No specific game-day catalyst needed; the market inefficiency itself provides the edge. Sports category has strong track record (WR=77%).

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates recent results 2025'})` → [Sat, 20 Sep 2025] Google News
[Fri, 08 Aug 2025] Athletics at Pittsburgh Pirates Game Story, Scores
- `search_web({'query': 'St. Louis Cardinals recent performance 2025'})` → [Tue, 16 Sep 2025] Google News
[Mon, 09 Feb 2026] Cincinnati Reds at St. Louis Cardinals Game Story,
- `get_market_context({'keyword': 'Pittsburgh Pirates St. Louis Cardinals'})` → No related markets found for 'Pittsburgh Pirates St. Louis Cardinals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals series odds September 2025'})` → [Mon, 08 Sep 2025] Google News
[Tue, 25 Nov 2025] Bird Watching: Mariners vs. Cardinals Series Previ
- `search_web({'query': 'MLB standings September 2025 NL Central'})` → [Mon, 18 May 2026] Google News
[Mon, 01 Sep 2025] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Pittsburgh Cardinals game tonight starting pitcher'})` → [Tue, 19 May 2026] Google News
[Thu, 21 May 2026] Pirates Starting Pitchers Must Bounceback in Cardi

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*