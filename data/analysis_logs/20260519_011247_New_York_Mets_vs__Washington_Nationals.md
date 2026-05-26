# Market Analysis — 2026-05-19 01:12 UTC

## Market
- **Question:** New York Mets vs. Washington Nationals
- **Category:** sports
- **YES Price:** 69.0%
- **Days Left:** 6
- **Volume 24h:** $289,379
- **Liquidity:** $41,563

## Statistical Prior
- **p_base:** 76.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,029 (-0.1% 24h) → neutral
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
- **Confidence:** 0%
- **p_true:** 76.9%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 0%<52%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'New York Mets'})` → INJURY [new york mets] A.J. Minter (RP): 60-Day-IL
INJURY [new york mets] Mike Tauchman (RF): Day-To
- `get_sports_data({'sport': 'mlb', 'team': 'Washington Nationals'})` → INJURY [washington nationals] Jacob Young (CF): Day-To-Day
INJURY [washington nationals] Clayton Bee
- `search_web({'query': 'New York Mets vs Washington Nationals series preview 2025'})` → [Sat, 16 May 2026] Google News
[Fri, 19 Sep 2025] Game Notes: Baltimore Orioles vs Washington Nation
- `search_web({'query': 'Mets Nationals game odds today 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] How to watch Mets vs. Nationals: TV channel and st
- `get_odds({'sport': 'baseball_mlb', 'team': 'New York Mets'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'New York Mets Washington Nationals'})` → No related markets found for 'New York Mets Washington Nationals'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*