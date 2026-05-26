# Market Analysis — 2026-05-19 11:32 UTC

## Market
- **Question:** Geneva Open: Alexei Popyrin vs Clement Tabur
- **Category:** sports
- **YES Price:** 59.0%
- **Days Left:** 6
- **Volume 24h:** $405,831
- **Liquidity:** $49,159

## Statistical Prior
- **p_base:** 63.3%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,814 (+0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,814 (+0.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: alexei popyrin clement
- [Bing News]
- [Sat, 16 May 2026] geneva open: alexei popyrin clement
- → May in Switzerland and sees Novak Djokovic as the defending champion but unlike previous years, he won't return to play in the tournament in ...
- [] Geneva Open 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 57.3%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.65

### Reasoning
Strong statistical pattern (n=13,967) shows markets at 59% YES resolve YES only 44.7% of the time, indicating significant overpricing. Popyrin's recent form is poor (hasn't won a match in over 5 months). Base rate of 63% suggests YES is favored, but market correction pattern is robust. No direct injury/news catalyst found, but crowd bias appears to be inflating YES price. Moderate confidence due to lack of specific match catalyst but strong statistical edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Popyrin'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp_italian_open'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Alexei Popyrin vs Clement Tabur Geneva Open 2025 head to head'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': 'Alexei Popyrin recent form results 2025'})` → [Mon, 19 Jan 2026] Google News
[Wed, 11 Feb 2026] “It can’t keep going on like this”: Shattered Popy
- `get_market_context({'keyword': 'Geneva Open tennis'})` → No related markets found for 'Geneva Open tennis'
- `search_web({'query': 'Popyrin vs Tabur prediction pick odds Geneva Open May 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Popyrin vs. Tabur Prediction at the Gonet Geneva O
- `search_web({'query': 'Clement Tabur tennis form ranking 2026'})` → [Mon, 18 May 2026] Google News
[Thu, 02 Apr 2026] ATP Geneva Day 3 Predictions Including Casper Ruud
- `search_web({'query': '"Popyrin" "Tabur" odds prediction Geneva 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] ATP Geneva Best Bets Including Casper Ruud vs Jens
- `search_web({'query': 'Alexei Popyrin ATP ranking 2026 clay season results'})` → [Fri, 03 Apr 2026] Google News
[Thu, 23 Apr 2026] ATP Houston Quarterfinal Predictions Including Fra
- `search_web({'query': 'Alexei Popyrin clay court record 2025 2026'})` → [Fri, 08 May 2026] Google News
[Wed, 22 Apr 2026] French Open 2026 Odds: Clay Performance Score Rank
- `search_web({'query': 'Clement Tabur ATP ranking clay specialist French player'})` → [Sun, 17 May 2026] Google News
[Mon, 13 Apr 2026] ATP Geneva 2026 Preview, Draw Analysis, Top Seeds 
- `search_web({'query': 'Popyrin Tabur Bleacher Nation prediction odds picks'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Popyrin vs. Tabur Prediction at the Gonet Geneva O
- `search_web({'query': 'Clement Tabur record 2026 ATP tour results'})` → [Tue, 27 May 2025] Google News
[Mon, 03 Nov 2025] Djokovic maintains perfect R1 record at Roland Gar

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*