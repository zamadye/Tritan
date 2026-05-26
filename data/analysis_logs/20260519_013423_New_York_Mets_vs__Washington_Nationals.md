# Market Analysis — 2026-05-19 01:34 UTC

## Market
- **Question:** New York Mets vs. Washington Nationals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 6
- **Volume 24h:** $343,958
- **Liquidity:** $34,882

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,668 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,065 (-0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- NYM @ WSH | In Progress | Washington Nationals(home) 23-24 score:4 vs New York Mets(away) 20-26 score:5
- TOR @ NYY | In Progress | New York Yankees(home) 28-19 score:3 vs Toronto Blue Jays(away) 21-25 score:5
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: york mets washington nationals
- [Bing News]
- [Mon, 18 May 2026] york mets washington nationals
- → Follow our live updates as the New York Mets look to win their third straight game on Monday against the Nationals.
- [Mon, 18 May 2026] NY Mets vs Nationals live updates, score and analysis of today's game
- → Follow along as the Nats kick off a crucial four game home set against the Mets ...
- [Mon, 18 May 2026] Washington Nationals vs New York Mets game thread
- → The New York Mets announced multiple roster moves on Monday ahead of their game against the Washington Nationals.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 51.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.60

### Reasoning
Statistical signal (n=13,967) indicates markets at 51% YES historically resolve YES only 44.7% of the time, suggesting overpricing. However, gap vs base rate is only +1% (51% vs 52%), and past decisions skipped similar setups due to low confidence or insufficient edge (gap <5%). Injury reports show minor impacts for both teams. No direct catalyst or breaking news to confirm edge. Entry zone 50-60% has weak historical win rate (40%). While crowd bias exists, confidence remains moderate due to lack of independent verification and indirect catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Mets'})` → INJURY [new york mets] A.J. Minter (RP): 60-Day-IL
INJURY [new york mets] Mike Tauchman (RF): Day-To
- `get_sports_data({'sport': 'mlb', 'team': 'Nationals'})` → INJURY [washington nationals] Jacob Young (CF): Day-To-Day
INJURY [washington nationals] Clayton Bee
- `search_web({'query': 'Mets vs Nationals game 2025'})` → [Sat, 16 May 2026] Google News
[Sun, 21 Sep 2025] 2026 New York Mets TV schedule: How to watch, stre
- `search_web({'query': 'Mets Nationals pitching matchup May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Mets vs Nationals prediction May 18 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Mets at Nationals: 5 things to watch and series pr
- `search_web({'query': 'Mets at Nationals 5 things to watch series predictions May 18 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Mets at Nationals: 5 things to watch and series pr
- `get_odds({'sport': 'baseball_mlb', 'team': 'Mets'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*