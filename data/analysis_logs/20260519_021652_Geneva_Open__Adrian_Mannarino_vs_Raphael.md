# Market Analysis — 2026-05-19 02:16 UTC

## Market
- **Question:** Geneva Open: Adrian Mannarino vs Raphael Collignon
- **Category:** sports
- **YES Price:** 12.0%
- **Days Left:** 6
- **Volume 24h:** $69,934
- **Liquidity:** $28,129

## Statistical Prior
- **p_base:** 4.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,634 (-0.6% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,613 (-0.7% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: adrian mannarino raphael
- [Bing News]
- [Sat, 16 May 2026] geneva open: adrian mannarino raphael
- → May in Switzerland and sees Novak Djokovic as the defending champion but unlike previous years, he won't return to play in the tournament in ...
- [] Geneva Open 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 40%
- **p_true:** 5.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Low-information market with no verifiable edge. Mannarino had disastrous 2026 season (first win only in May at Houston), Collignon is young rising player with upset potential (beat Dimitrov in Brisbane). Market prices YES at 12% vs 5% base rate, suggesting some information priced in but bookmaker odds unavailable to verify. Previous two decisions also skipped due to insufficient confidence (0% and 38%). No direct catalyst or injury news found. Cannot confirm mispricing without complete odds data.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 40%<52%

## Tool Calls
- `search_web({'query': 'Adrian Mannarino Raphael Collignon Geneva Open 2026'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'Mannarino recent form 2026 tennis results'})` → [Sat, 16 May 2026] Google News
[Sun, 08 Feb 2026] Adrian Mannarino v Raphael Collignon 18/05/2026, O
- `get_odds({'sport': 'tennis_atp', 'team': 'Mannarino'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Geneva Open'})` → No related markets found for 'Geneva Open'
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Polymarket Mannarino Collignon Geneva Open prediction market'})` → No search results for: Polymarket Mannarino Collignon Geneva Open prediction market
- `search_web({'query': 'Raphael Collignon ATP ranking 2026'})` → [Tue, 20 Jan 2026] Google News
[Tue, 03 Mar 2026] Tennis, ATP – Australian Open 2026: Musetti downs 
- `get_market_context({'keyword': 'Mannarino'})` → No related markets found for 'Mannarino'
- `search_web({'query': 'Mannarino vs Collignon head to head tennis 2026'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'Geneva Open tennis 2026 results draw third round'})` → [Tue, 19 May 2026] Google News
[Wed, 13 May 2026] "We players are the ones who generate the tourname
- `get_odds({'sport': 'basketball_nba', 'team': 'Lakers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Mannarino tennis results 2026 season wins losses'})` → [Sun, 08 Feb 2026] Google News
[Fri, 29 Aug 2025] Felix Auger-Aliassime sets Canadian record with Mo
- `search_web({'query': 'Raphael Collignon 2026 season results form'})` → [Wed, 13 May 2026] Google News
[Mon, 20 Apr 2026] Raphael Collignon v Geoffrey Blancaneaux LIVE 13/0
- `search_web({'query': 'Mannarino ranking 2026 ATP'})` → [Mon, 02 Feb 2026] Google News
[Mon, 09 Feb 2026] Moise Kouame, 16, becomes sixth-youngest qualifier
- `search_web({'query': 'Collignon ranking 2026 ATP'})` → [Thu, 08 Jan 2026] Google News
[Tue, 20 Jan 2026] Collignon upsets idol Dimitrov in Brisbane: 'It wa
- `search_web({'query': 'Mannarino last 10 matches 2026'})` → [Thu, 02 Apr 2026] Google News
[Thu, 05 Feb 2026] Rain all but wipes out Thursday’s R2 action in Buc
- `search_web({'query': 'Collignon last 10 matches 2026'})` → [Tue, 03 Mar 2026] Google News
[Tue, 21 Apr 2026] Three first round matches to watch in Tennis Parad
- `search_web({'query': '"Mannarino vs Collignon" Geneva Open prediction'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Mannarino vs. Collignon Prediction at the Gonet Ge
- `search_web({'query': 'Mannarino Collignon odds betting preview'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Adrian Mannarino v Raphael Collignon 18/05/2026, O

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*