# Market Analysis — 2026-05-21 19:47 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $199,282
- **Liquidity:** $266,151

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,551 (-0.0% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,551 (-0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- [SPORTS] Recent games:
- ATL @ MIA | Scheduled | Miami Marlins(home) 22-28 score:0 vs Atlanta Braves(away) 34-16 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Thu, 21 May 2026] atlanta braves miami marlins
- → Here's how to watch Thursday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Thu, 21 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 21
- → Atlanta Braves roster update: veteran pitcher Carlos Carrasco is back in the spotlight as the team faces the Marlins.
- [Thu, 21 May 2026] Atlanta Braves Announce Unsurprising Signing Of 17-Year MLB Player Before Marlins Game
- → Janson Junk #26 of the Miami Marlins delivers during the first inning against the Atlanta Braves at loanDepot park on May 20, 2026 in Miami, Florida

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Stat signal suggests YES is overpriced (57% market vs 44.7% historical resolution rate), but entry conditions are not met: gap is only 3% (below the 5% gate), the 50-60% entry zone has a historically poor 42% win rate from 19 trades, no fresh catalysts or breaking news found, no related markets to cross-verify, and previous decisions on this exact market both failed the gate. The theoretical edge exists but practical entry conditions favor SKIP.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Hurston Waldrep (SP): 60-Day-IL
INJURY [atlanta braves] Drake Baldwin (C): 1
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `get_sports_data({'sport': 'mlb', 'team': 'Marlins'})` → INJURY [miami marlins] Leo Jimenez (3B): 7-day il
INJURY [miami marlins] Robby Snelling (SP): 60-Day
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 MLB series preview pitching matchup'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Atlanta Braves recent results standings June 2025'})` → [Thu, 11 Sep 2025] Google News
[Sat, 29 Nov 2025] MLB Power Rankings Week 24: Every team's standing 
- `search_web({'query': 'Atlanta Braves Miami Marlins today probable pitchers starting lineup'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'MLB 2025 Braves record standings wild card race'})` → [Mon, 01 Sep 2025] Google News
[Mon, 01 Sep 2025] Ranking 2025 MLB playoff races that will rule the 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*