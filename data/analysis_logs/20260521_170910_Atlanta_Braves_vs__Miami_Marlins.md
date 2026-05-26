# Market Analysis — 2026-05-21 17:09 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $145,160
- **Liquidity:** $221,741

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,163 (-0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,148 (-0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Tommy Henry — Day-To-Day (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Austin Riley and Dominic Smith hit three-run home runs, Chris Sale allowed just one run and struck out eight over seven innings, and the Atlanta Bra
- [Thu, 21 May 2026] Atlanta Braves beat Miami Marlins 9-1 behind Chris Sale and 3-run homers from Austin Riley, Dominic Smith
- → Here's how to watch Thursday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Thu, 21 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 21
- → The Atlanta Braves are looking to take the final three games of their series against the Miami Marlins after getting shut out 12-0 in the opener. Th

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 60.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.65

### Reasoning
Contradictory signals prevent high-confidence bet. The stat signal (n=13,967) shows markets at 57% resolve YES only 44.7% of time, suggesting YES is overpriced by ~12% (strong edge for NO). However, base rate of 60% contradicts this. Gap is only 3% (below 5% gate threshold). Both previous decisions for this exact market were SKIP. Entry range 50-60% has poor 44% WR historically. No concrete catalyst found—Braves have 3 IL players (including SP Waldrep) and Marlins are strong recently, but these are already priced in. Need either gap ≥5% or resolving contradiction between base rate and stat signal to act.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Drake Baldwin (C): 10-Day-IL
INJURY [atlanta braves] Hurston Waldrep (SP): 1
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 season series results'})` → [Wed, 27 Aug 2025] Google News
[Wed, 27 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Braves recent form MLB 2025'})` → [Tue, 19 May 2026] Google News
[Tue, 05 May 2026] 2026 MLB Season: Schedule Information, Latest Rule
- `get_market_context({'keyword': 'Atlanta Braves'})` → No related markets found for 'Atlanta Braves'
- `get_market_context({'keyword': 'Miami Marlins'})` → No related markets found for 'Miami Marlins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Braves vs Marlins odds September 2025 pitching matchup'})` → [Fri, 19 Sep 2025] Google News
[Tue, 02 Sep 2025] How to Watch Tigers vs. Braves: TV Channel &amp; L
- `search_web({'query': 'Atlanta Braves September 2025 record standings wild card'})` → [Mon, 01 Sep 2025] Google News
[Sun, 28 Sep 2025] Ranking 2025 MLB playoff races that will rule the 
- `search_web({'query': 'Miami Marlins 2025 record season'})` → [Thu, 26 Mar 2026] Google News
[Fri, 03 Apr 2026] 2025 Marlins Standings and Record: Wild Card - MLB
- `search_web({'query': '"Atlanta Braves" "Miami Marlins" September 2025 pitching'})` → [Wed, 24 Sep 2025] Google News
[Thu, 16 Apr 2026] Despite injury-laden 1st half, Braves feeling opti
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Thomas White (SP): Day-To-Day
INJURY [miami marlins] Leo Jimenez (3B): Day-To

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*