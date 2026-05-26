# Market Analysis — 2026-05-21 09:00 UTC

## Market
- **Question:** Cleveland Guardians vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 49.0%
- **Days Left:** 7
- **Volume 24h:** $57,177
- **Liquidity:** $136,300

## Statistical Prior
- **p_base:** 48.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,832 (+0.5% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,859 (+0.6% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- [SPORTS] Recent games:
- CLE @ DET | Final | Detroit Tigers(home) 20-30 score:2 vs Cleveland Guardians(away) 29-22 score:3
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: cleveland guardians detroit tigers
- [Bing News]
- [Wed, 20 May 2026] cleveland guardians detroit tigers
- → Angel Mart&#237;nez hit a tiebreaking triple in the 10th inning, Jos&#233; Ram&#237;rez followed with an RBI double and the Cleveland Guardians beat
- [Thu, 21 May 2026] Guardians score twice in the 10th for a 3-2 victory over the slumping Tigers
- → Cleveland Guardians (29-22, first in the AL Central) vs. Detroit Tigers (20-30, fourth in the AL Central) Detroit; Thursday, 1:10 p.m. EDT PITCHING 
- [Wed, 20 May 2026] Guardians bring win streak into matchup with the Tigers
- → Making his first start in a Detroit Tigers uniform, pitcher Drew Anderson set a career-high in strikeouts in Detroit's loss against Cleveland.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 48.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market at fair value (YES 49% vs base 48%, gap -1%). No verifiable edge despite Tigers having more injuries. Guardians pitcher bribery scandal may partially offset injury advantage. Historical pattern shows systematic YES overpricing in similar matchups. Entry point 40-50% has only 50% win rate. No direct catalyst or information gap identified.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Cleveland Guardians'})` → INJURY [cleveland guardians] Gabriel Arias (SS): 10-Day-IL
INJURY [cleveland guardians] Peyton Palle
- `get_sports_data({'sport': 'mlb', 'team': 'Detroit Tigers'})` → INJURY [detroit tigers] Justin Verlander (SP): 60-Day-IL
INJURY [detroit tigers] Gleyber Torres (2B)
- `search_web({'query': 'Cleveland Guardians recent news April 2024'})` → [Thu, 02 Apr 2026] Google News
[Mon, 03 Nov 2025] Guardians share extreme, vulgar threats from betto
- `search_web({'query': 'Detroit Tigers recent news April 2024'})` → [Sat, 04 Apr 2026] Google News
[Thu, 26 Mar 2026] Detroit Tigers vs St. Louis Cardinals, Game 8: One
- `get_market_context({'keyword': 'Cleveland Guardians Detroit Tigers'})` → No related markets found for 'Cleveland Guardians Detroit Tigers'
- `get_market_context({'keyword': 'Guardians Tigers'})` → No related markets found for 'Guardians Tigers'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Cleveland Guardians'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*