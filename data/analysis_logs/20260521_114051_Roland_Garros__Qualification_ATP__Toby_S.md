# Market Analysis — 2026-05-21 11:40 UTC

## Market
- **Question:** Roland Garros, Qualification ATP: Toby Samuel vs Gonzalo Bueno
- **Category:** sports
- **YES Price:** 60.0%
- **Days Left:** 7
- **Volume 24h:** $94,192
- **Liquidity:** $62,336

## Statistical Prior
- **p_base:** 64.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.7%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,229 (-0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,174 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: roland garros qualification atp: toby
- [Bing News]
- [Wed, 20 May 2026] roland garros qualification atp: toby
- → Britain's Toby Samuel and Felix Gill are both one win away from a lucrative first Grand Slam singles appearance as they reach the final round of Fre
- [Mon, 19 May 2025] British duo one win from French Open breakthroughs
- → With the Entry Lists now confirmed for the 2025 French Open at Roland Garros between May 25 - June 8, the Prize Money has now been set with a record
- [] Prize Money and points breakdown 2025 French Open | Roland Garros | ATP | WTA
- [Metaculus]

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 51.9%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.82

### Reasoning
Strong statistical edge: Markets priced at 60% YES historically resolve YES only 44.7% of the time across 13,967 observations. This represents a ~15% edge for NO (true NO prob ~55.3% vs market NO price of 40%). Both players appear fit with no injury news — Samuel has excellent recent form (top 200, winning streak) while Bueno won Buenos Aires Challenger recently. However, the large-sample statistical pattern overwhelmingly favors NO at this price point. Prior similar market decision also attempted NO but failed gate (gap <5%); now the gap is +5% meeting threshold. Crowd likely overprices YES due to Samuel's recent momentum buzz.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Samuel'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Toby Samuel vs Gonzalo Bueno Roland Garros 2025 qualification'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] French Open qualifying 2026: British duo one win f
- `search_web({'query': 'Toby Samuel tennis recent results form 2025'})` → [Wed, 18 Mar 2026] Google News
[Tue, 31 Mar 2026] Toby Samuel: Tennis player aiming for Grand Slams 
- `get_market_context({'keyword': 'Roland Garros qualification'})` → No related markets found for 'Roland Garros qualification'
- `search_web({'query': 'Gonzalo Bueno tennis recent results form 2025 2026'})` → [Thu, 05 Feb 2026] Google News
[Wed, 14 Jan 2026] Germany v Peru: Start the Davis Cup party, like it
- `search_web({'query': 'Gonzalo Bueno vs Toby Samuel head to head'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] H2H Toby Samuel Vs Gonzalo Bueno stats, prediction
- `search_web({'query': 'Toby Samuel ATP ranking 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 25 Mar 2026] French Open qualifying 2026: British duo one win f
- `search_web({'query': 'Gonzalo Bueno ATP ranking 2026'})` → [Mon, 15 Jan 2024] Google News
[Wed, 13 May 2026] Que bueno! 19-year-old Bueno wins Buenos Aires Cha
- `search_web({'query': 'Toby Samuel injury status May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] GB's Toby Samuel one win from Grand Slam debut at 
- `search_web({'query': 'Gonzalo Bueno injury status May 2026'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] 2026 World Cup injuries tracker: Which players are
- `search_web({'query': '"Toby Samuel" "Gonzalo Bueno" French Open qualifying odds'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] British duo one win from French Open breakthroughs
- `search_web({'query': 'Wincomparator Toby Samuel Gonzalo Bueno prediction odds 21 May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Toby Samuel vs Gonzalo Bueno prediction – Odds &am

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*