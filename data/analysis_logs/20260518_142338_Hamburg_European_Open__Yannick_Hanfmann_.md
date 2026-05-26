# Market Analysis — 2026-05-18 14:23 UTC

## Market
- **Question:** Hamburg European Open: Yannick Hanfmann vs Max Schoenhaus
- **Category:** sports
- **YES Price:** 68.0%
- **Days Left:** 6
- **Volume 24h:** $100,064
- **Liquidity:** $101,468

## Statistical Prior
- **p_base:** 75.6%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,677 (-1.8% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,624 (-1.7% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → ECB rate cut → EUR weakens vs USD → EUR/USD falls
- → EU GDP beats expectations → EUR strengthens
- → EU political crisis (elections) → EUR uncertainty → falls
- → EUR/USD above 1.10 → European exports competitive → EU stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: hamburg european open: yannick hanfmann
- [Bing News]
- [Wed, 22 Apr 2026] hamburg european open: yannick hanfmann
- → Yannick Hanfmann, the World No. 60 in men's singles tennis and a former No. 45, enters the 2026 Madrid Open on the back of a first-round exit from t
- [] Yannick Hanfmann vs Marcos Giron preview, head-to-head, odds, prediction &amp; betting tips | Madrid Open 2026
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** YES
- **Confidence:** 62%
- **p_true:** 77.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MISPRICING
- **Catalyst Strength:** 0.45

### Reasoning
8% gap between base rate (76%) and market price (68%) with no contradicting evidence found. Hanfmann is the established ATP player (AO 2026, Rome) vs young Schoenhaus. No injuries or form issues discovered to explain the market discount. Pattern shows 91% WR for sports and 80% WR at this entry range. Moderate confidence due to lack of direct catalyst beyond statistical edge.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Hanfmann'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Yannick Hanfmann vs Max Schoenhaus Hamburg European Open 2025 odds'})` → [Sun, 17 May 2026] Google News
[] 2026 Hamburg European Open Betting Odds for Men’s Singles - Bleach
- `search_web({'query': 'Max Schoenhaus injury update 2025'})` → [Thu, 04 Sep 2025] Google News
[Fri, 11 Jul 2025] Juniors: Ivanov, Klugman reach semis at the 2025 U
- `get_market_context({'keyword': 'Hamburg European Open'})` → No related markets found for 'Hamburg European Open'
- `search_web({'query': 'Hamburg European Open 2026 tennis draw Yannick Hanfmann Max Schoenhaus'})` → [Fri, 19 Jul 2019] Google News
[Sun, 05 Apr 2026] Hamburg | Draws | ATP Tour | Tennis - ATP Tour
[] 
- `search_web({'query': 'Yannick Hanfmann recent matches 2026'})` → [Tue, 05 May 2026] Google News
[Tue, 20 Jan 2026] ATP Rome Best Bets Including Hubert Hurkacz vs Yan
- `search_web({'query': 'Max Schoenhaus tennis ranking 2026'})` → [Thu, 14 Aug 2025] Google News
[Fri, 29 Aug 2025] Max Schoenhaus Player Profile | Official Site of t
- `search_web({'query': 'Yannick Hanfmann injury May 2026'})` → [Wed, 21 Jan 2026] Google News
[Wed, 21 Jan 2026] Alcaraz survives 78-minute opening set in Australi
- `search_web({'query': 'Max Schoenhaus form Hamburg 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Yannick Hanfmann vs. Max Schoenhaus prediction, od
- `search_web({'query': 'Yannick Hanfmann vs Max Schoenhaus prediction dimers.com May 18 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Yannick Hanfmann vs. Max Schoenhaus prediction, od
- `search_web({'query': 'Hanfmann Schoenhaus ATP Hamburg 2026 odds preview'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Yannick Hanfmann vs. Max Schoenhaus prediction, od
- `search_web({'query': 'Hanfmann Hamburg 2026 form results'})` → [Sun, 17 May 2026] Google News
[Tue, 25 Jul 2023] Hamburg Open 2026: Results, Draw, Schedule, Entry 
- `search_web({'query': 'Schoenhaus Hamburg 2026 ranking ATP'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Hamburg Open 2026: All matches, live scores and ho

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*