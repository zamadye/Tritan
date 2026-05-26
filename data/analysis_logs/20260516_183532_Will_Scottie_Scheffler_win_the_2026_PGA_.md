# Market Analysis — 2026-05-16 18:35 UTC

## Market
- **Question:** Will Scottie Scheffler win the 2026 PGA Championship?
- **Category:** sports
- **YES Price:** 16.0%
- **Days Left:** 1
- **Volume 24h:** $197,646
- **Liquidity:** $19,237

## Statistical Prior
- **p_base:** 7.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,163 (-1.2% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,120 (-1.5% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [MULTI-SOURCE NEWS] 1 sources for: scottie scheffler 2026 championship
- [Bing News]

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 7.7%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.15

### Reasoning
The 2026 PGA Championship is LIVE NOW (Round 3 today at Aronimink). Scheffler was in a 7-way tie after Round 1 but fell back after Round 2 - McNealy and Smalley now lead. At 16%, the market accurately reflects a world-class player who is still in contention but NOT leading with ~36 holes left. No information asymmetry exists: the leaderboard is public, the tournament is in-progress, and the price already accounts for his current position. The tight leaderboard means high variance - many players have legitimate chances. 16% is reasonable for a trailing-but-contending elite player. No specific catalyst today to create edge. Historical base rate (8%) is less relevant for a live in-progress major where he was recently tied for the lead.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Scottie Scheffler 2025 2026 PGA Championship odds'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] 2026 PGA Championship odds, picks: Surprising week
- `search_web({'query': 'Scottie Scheffler recent results 2025 form'})` → [Mon, 06 Apr 2026] Google News
[Tue, 07 Apr 2026] Who will win the Masters? Scottie Scheffler, Rory 
- `get_market_context({'keyword': 'PGA Championship golf major winner'})` → No related markets found for 'PGA Championship golf major winner'
- `search_web({'query': '2026 PGA Championship leaderboard today Scottie Scheffler'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] PGA Championship leaderboard, Round 2 updates: Mav
- `search_web({'query': '2026 PGA Championship Aronimink standings round 3'})` → [Sat, 16 May 2026] Google News
[Fri, 15 May 2026] 2026 PGA Championship watch guide: Tee times, TV i
- `search_web({'query': '"PGA Championship" leaderboard Scheffler score back 2026'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Round 2 notebook: Tight leaderboard sets up dramat
- `search_web({'query': 'Scottie Scheffler PGA Championship round 2 score position'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Round 2 notebook: Tight leaderboard sets up dramat

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*