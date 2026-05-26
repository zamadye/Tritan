# Market Analysis — 2026-05-20 18:20 UTC

## Market
- **Question:** Houston Astros vs. Minnesota Twins
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 6
- **Volume 24h:** $183,272
- **Liquidity:** $88,964

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,430 (+0.8% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,430 (+0.8% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Recent games:
- HOU @ MIN | In Progress | Minnesota Twins(home) 22-27 score:1 vs Houston Astros(away) 20-30 score:1
- [SPORTS] Injuries:
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: A.J. Puk — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: houston astros minnesota twins
- [Bing News]
- [Wed, 20 May 2026] houston astros minnesota twins
- → The Houston Astros (20-30) and Minnesota Twins (22-27) will play the rubber match of this 3-game series this afternoon at 12:40 p.m. CT. RHP Mike Bu
- [Wed, 20 May 2026] Astros vs. Twins Game Thread: Game 51, 5/20/2026
- → Here's how to watch Wednesday's Minnesota Twins vs Houston Astros game, including start times, TV channels, scores and how to stream.
- [Wed, 20 May 2026] Where to watch Houston Astros vs Minnesota Twins: TV channel, start time, streaming for May 20
- → The Houston Astros have the chance to win their second series in a row against the Minnesota Twins.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 47.2%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical edge: Markets priced at 54% historically resolve YES only 44.7% of the time (n=13,967), creating a 9.3pp edge against YES. Both teams have notable pitching injuries (Astros: Hunter Brown, McCullers; Twins: Taj Bradley). Entry 50-60% pattern shows only 33% win rate historically. No direct news catalyst found, but the empirical mispricing signal is robust with large sample size. Sports pattern shows 83% WR overall but the specific entry price weakness dominates.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Astros'})` → INJURY [houston astros] Hunter Brown (SP): 60-Day-IL
INJURY [houston astros] Taylor Trammell (CF): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Twins'})` → INJURY [minnesota twins] Taj Bradley (SP): 15-Day-IL
INJURY [minnesota twins] Ryan Jeffers (C): 10-D
- `search_web({'query': 'Houston Astros vs Minnesota Twins 2025 series preview'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Minnesota Twins vs Houston Astros Prediction &amp;
- `search_web({'query': 'Astros Twins upcoming matchup odds'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Houston Astros vs. Minnesota Twins - Live Score - 
- `get_market_context({'keyword': 'Astros Twins'})` → No related markets found for 'Astros Twins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Astros'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `search_web({'query': 'Houston Astros vs Minnesota Twins May 18 2026 game preview starting pitchers'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Minnesota Twins Houston Astros series results May 2026'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Paredes’ 2-run homer in the 1st inning powers Astr
- `search_web({'query': 'Astros Twins who is favored tonight 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Resumen Astros @ Twins, Resultados/Jugadas destaca
- `search_web({'query': '"Astros" "Twins" May 20 2026 prediction odds moneyline'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] How to watch Astros vs. Twins: TV channel and stre

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*