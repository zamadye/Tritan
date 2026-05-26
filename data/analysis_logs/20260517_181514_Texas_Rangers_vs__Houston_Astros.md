# Market Analysis — 2026-05-17 18:15 UTC

## Market
- **Question:** Texas Rangers vs. Houston Astros
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 6
- **Volume 24h:** $108,701
- **Liquidity:** $389,098

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,106 (-0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,047 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Recent games:
- TEX @ HOU | Scheduled | Houston Astros(home) 19-28 score:0 vs Texas Rangers(away) 21-24 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: texas rangers houston astros
- [Bing News]
- [Sun, 17 May 2026] texas rangers houston astros
- → The Houston Astros (19-28) will play the final game of their seven-game homestand today as they go for a sweep in the first round of the Silver Boot
- [Sun, 17 May 2026] Astros vs. Rangers Game Thread: Game 48, 5/17/2026
- → Rangers All-Star shortstop Corey Seager was out of the lineup for a second straight game Sunday against the Astros because of back spasms.
- [Sun, 17 May 2026] Rangers' Corey Seager (back) remains sidelined, having MRI
- → Jose Altuve will undergo an MRI after leaving the Astros' 4-1 win over the Rangers amid Houston's 14-player IL crisis.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 56.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] Corey Seager (SS): Day-To-Day
INJURY [texas rangers] Josh Smith (2B): 10-Day-
- `get_sports_data({'sport': 'mlb', 'team': 'Houston Astros'})` → INJURY [houston astros] Jose Altuve (2B): Day-To-Day
INJURY [houston astros] Jeremy Pena (SS): 10-Da
- `get_odds({'sport': 'baseball_mlb'})` → [ODDS] baseball_mlb — 23 events
  Tampa Bay Rays vs Miami Marlins (2026-05-17)
    [FanDuel] Miami M
- `search_web({'query': 'Texas Rangers vs Houston Astros upcoming game 2025'})` → [Sat, 06 Sep 2025] Google News
[Wed, 18 Mar 2026] Houston Astros at Texas Rangers Game Story, Scores
- `search_web({'query': 'Houston Astros vs Texas Rangers recent results injuries'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Astros shut down Rangers again, but face new injur
- `get_market_context({'keyword': 'Texas Rangers Houston Astros'})` → No related markets found for 'Texas Rangers Houston Astros'
- `search_web({'query': 'Polymarket Texas Rangers Houston Astros prediction market'})` → [Tue, 12 May 2026] Google News
[Wed, 13 May 2026] Texas Prediction Markets and Sites: Sports Betting
- `search_web({'query': 'Texas Rangers Houston Astros odds 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Rangers vs. Astros (May 17, 2026) Live Score - ESP
- `search_web({'query': '"Texas Rangers at Houston Astros" odds picks predictions May 17 2026'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Texas Rangers at Houston Astros odds, picks, and p
- `search_web({'query': '"Rangers vs Astros" "May 17, 2026" betting odds'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] How to watch Rangers vs. Astros: TV channel and st
- `search_web({'query': 'Houston Astros Texas Rangers May 2026 series pitching matchup'})` → [Thu, 14 May 2026] Google News
[Fri, 15 May 2026] Rangers vs. Astros Series Injured List - May 15-17
- `search_web({'query': 'Astros shut out Rangers first 2026 matchup Silver Boot Series'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Silver Boot Series: Astros shut out Rangers in fir
- `search_web({'query': 'Rangers vs Astros series injured list May 15-17 SportsTalk 790'})` → [Thu, 14 May 2026] Google News
[] Rangers vs. Astros Series Injured List - May 15-17 - SportsTalk 79
- `search_web({'query': 'baseball betting markets overpriced YES 54% historical resolution rate'})` → No search results for: baseball betting markets overpriced YES 54% historical resolution rate

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*