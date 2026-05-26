# Market Analysis — 2026-05-17 17:52 UTC

## Market
- **Question:** Texas Rangers vs. Houston Astros
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $104,968
- **Liquidity:** $388,561

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,005 (-0.3% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,943 (-0.4% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- [SPORTS] Recent games:
- TEX @ HOU | Scheduled | Houston Astros(home) 19-28 score:0 vs Texas Rangers(away) 21-24 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: texas rangers houston astros
- [Bing News]
- [Sun, 17 May 2026] texas rangers houston astros
- → The Houston Astros (19-28) will play the final game of their seven-game homestand today as they go for a sweep in the first round of the Silver Boot
- [Sun, 17 May 2026] Astros vs. Rangers Game Thread: Game 48, 5/17/2026
- → Jose Altuve will undergo an MRI after leaving the Astros' 4-1 win over the Rangers amid Houston's 14-player IL crisis.
- [Sun, 17 May 2026] Astros’ Jose Altuve injury deals injury blow to Houston amid rough start to season
- → Here's how to watch Sunday's Houston Astros vs Texas Rangers game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** NO
- **Confidence:** 62%
- **p_true:** 46.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal: Markets at 54% YES price resolve YES only 44.7% of time (n=13,967), suggesting 9.3% systematic overpricing. While bookmaker odds contradict (55.2% for Rangers), the large-sample historical pattern is compelling. Sports bet pattern shows 85% WR overall and 86% WR in 50-60% entry range. True NO probability estimated at 55.3% vs market 46%, offering significant edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] Corey Seager (SS): Day-To-Day
INJURY [texas rangers] Josh Smith (2B): 10-Day-
- `get_sports_data({'sport': 'mlb', 'team': 'Houston Astros'})` → INJURY [houston astros] Jose Altuve (2B): Day-To-Day
INJURY [houston astros] Jeremy Pena (SS): 10-Da
- `search_web({'query': 'Texas Rangers vs Houston Astros 2025 MLB matchup preview'})` → [Sat, 16 May 2026] Google News
[Sun, 10 May 2026] Rangers vs Astros Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'MLB American League West standings 2025 Rangers Astros record'})` → [Thu, 18 Sep 2025] Google News
[Mon, 15 Sep 2025] MLB Power Rankings Week 25: Playoff contenders on 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Texas Rangers'})` → [ODDS] baseball_mlb — 1 events
  Houston Astros vs Texas Rangers (2026-05-17)
    [FanDuel] Houston 
- `get_market_context({'keyword': 'Rangers Astros'})` → No related markets found for 'Rangers Astros'
- `search_web({'query': '"Texas Rangers" "Houston Astros" May 2026 starting pitchers'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Texas Rangers lineup for May 17, 2026 - Yahoo Spor
- `search_web({'query': 'Texas Rangers recent results May 2026'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Texas Rangers lineup for May 17, 2026 - Yahoo Spor
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $78,024.00 | 24h: -0.23%

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*