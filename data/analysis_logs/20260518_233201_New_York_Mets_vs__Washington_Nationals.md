# Market Analysis — 2026-05-18 23:32 UTC

## Market
- **Question:** New York Mets vs. Washington Nationals
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 6
- **Volume 24h:** $199,947
- **Liquidity:** $14,721

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,999 (-1.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,999 (-1.1% 24h) → risk-OFF

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- [SPORTS] Recent games:
- NYM @ WSH | In Progress | Washington Nationals(home) 23-24 score:2 vs New York Mets(away) 20-26 score:1
- TOR @ NYY | In Progress | New York Yankees(home) 28-19 score:1 vs Toronto Blue Jays(away) 21-25 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: york mets washington nationals
- [Bing News]
- [Mon, 18 May 2026] york mets washington nationals
- → The New York Mets announced multiple roster moves on Monday ahead of their game against the Washington Nationals.
- [Mon, 18 May 2026] Mets announce multiple roster moves before Nationals clash
- → Follow along as the Nats kick off a crucial four game home set against the Mets ...
- [Mon, 18 May 2026] Washington Nationals vs New York Mets game thread
- → Follow our live updates as the New York Mets look to win their third straight game on Monday against the Nationals.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 54.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.70

### Reasoning
Despite strong STAT SIGNAL (n=13,967) showing markets at 53% resolve YES only 44.7% of the time — suggesting YES is overpriced by ~8.3 percentage points — the gap between market (53%) and base rate (54%) is only +1%, failing the 5% gate threshold. Historical pattern confirms 50-60% entry range has only 25% WR from 4 trades. Same market was previously SKIP'd (gap=3%<5%). Minor injuries on both sides (Minter RP 60-Day-IL, Herz SP 60-Day-IL) not game-changing. No breaking news or specific game catalyst identified. Risk-off macro environment is irrelevant for sports markets. Gate rule supersedes stat edge when gap is insufficient.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Mets'})` → INJURY [new york mets] A.J. Minter (RP): 60-Day-IL
INJURY [new york mets] Mike Tauchman (RF): Day-To
- `get_sports_data({'sport': 'mlb', 'team': 'Nationals'})` → INJURY [washington nationals] Clayton Beeter (RP): 15-Day-IL
INJURY [washington nationals] DJ Herz (
- `search_web({'query': 'New York Mets vs Washington Nationals 2025 game preview prediction'})` → [Fri, 19 Sep 2025] Google News
[Wed, 29 Apr 2026] New York Mets vs. Washington Nationals prediction,
- `search_web({'query': 'Mets Nationals series injuries starting pitchers 2025'})` → [Fri, 15 May 2026] Google News
[Tue, 30 Sep 2025] MLB 2026: Scorecard for Mets, Yankees ahead of Sub
- `get_market_context({'keyword': 'Mets Nationals baseball'})` → No related markets found for 'Mets Nationals baseball'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Mets'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'New York Mets Washington Nationals September 19 2025 starting pitchers odds'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] Mets vs Nationals Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Mets Nationals game today September 2025 odds starting pitchers'})` → [Mon, 18 May 2026] Google News
[Wed, 25 Mar 2026] Mets vs Nationals Prediction, Odds, Moneyline, Spr
- `search_web({'query': '2025 Mets epic collapse ESPN September 2025'})` → [Sun, 28 Sep 2025] Google News
[Sun, 28 Sep 2025] A $340 million disaster: 10 moments that define 20
- `get_market_context({'keyword': 'Mets'})` → No related markets found for 'Mets'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*