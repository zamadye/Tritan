# Market Analysis — 2026-05-17 21:08 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 6
- **Volume 24h:** $232,850
- **Liquidity:** $69,255

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,214 (-0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,246 (+0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Bing/Google News
- 6 articles found:
- [NewsAPI] Diamondbacks vs Rockies live updates. Rookie adjusts to a new ballpark: The Arizona Diamondbacks take on the Colorado Rockies for the second
- [NewsAPI] Colorado Rockies game no. 46 thread: Eduardo Rodriguez vs. Tomoyuki Sugano: Rivalry weekend continues, as two NL West foes hope to gain mome
- [NewsAPI] Last Night In Baseball: Pirates Implode Against Phillies: The Phillies stormed back against the Pirates, the Dodgers silenced the Angels, th
- [NewsAPI] Diamondbacks play the Rockies after Vargas' 4-hit game: Arizona Diamondbacks (21-22, third in the NL West) vs. Colorado Rockies (17-28, fift
- [NewsAPI] Carson Kelly drives in 4 as the Cubs beat White Sox 10-5: Carson Kelly hit a tiebreaking single in the seventh inning and drove in four runs
- [NewsAPI] Diamondback 9, Rockies 1: Colorado gets bit early in homestand opener: ﻿Arizona turned an overturned call into a six-run first inning, and M
- [CAUSAL CHAINS] Relevant cause-effect patterns:

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arizona diamondbacks colorado rockies
- [Bing News]
- [Sun, 17 May 2026] arizona diamondbacks colorado rockies
- → Arizona's finale matchup begins in a delay.
- [Sun, 17 May 2026] Diamondbacks game vs Rockies delayed due to weather
- → The Colorado Rockies vs Arizona Diamondbacks game originally scheduled to begin at 1:10 PM MDT has been delayed due to rain in the Denver Metro area
- [Sun, 17 May 2026] Rockies vs Diamondbacks Rain Delay Updates
- → The Colorado Rockies and Arizona Diamondbacks are in a rain delay as inclement weather moves through Denver on Sunday, May 17. Here's what you need 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 56.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Conflicting signals with no clear edge: Bookmaker consensus (~58.6%) suggests Diamondbacks are underpriced at 54%, but historical stat signal (44.7% resolution for 54% markets, n=13,967) strongly suggests YES is overpriced. No concrete catalyst or team-specific information to break the tie. Market appears efficient when weighing both sources.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'team': 'Arizona Diamondbacks', 'sport': 'mlb'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'team': 'Colorado Rockies', 'sport': 'mlb'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `get_odds({'team': 'Arizona Diamondbacks', 'sport': 'baseball_mlb'})` → [ODDS] baseball_mlb — 2 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `search_web({'query': 'Arizona Diamondbacks recent news'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Former D-backs Fan-Favorite Slugger Finds New Home
- `search_web({'query': 'Colorado Rockies recent news'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Colorado Rockies option Zach Agnos and recall Blas
- `get_market_context({'keyword': 'Diamondbacks'})` → No related markets found for 'Diamondbacks'
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies schedule May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Where to watch Arizona Diamondbacks vs Colorado Ro
- `search_web({'query': 'Colorado Rockies vs Arizona Diamondbacks schedule next game'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Where to watch Arizona Diamondbacks vs Colorado Ro

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*