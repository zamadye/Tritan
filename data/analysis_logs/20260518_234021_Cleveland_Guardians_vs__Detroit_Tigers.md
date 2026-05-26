# Market Analysis — 2026-05-18 23:40 UTC

## Market
- **Question:** Cleveland Guardians vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 42.0%
- **Days Left:** 6
- **Volume 24h:** $493,253
- **Liquidity:** $16,162

## Statistical Prior
- **p_base:** 38.1%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,999 (-1.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,984 (-1.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- [SPORTS] Recent games:
- CLE @ DET | In Progress | Detroit Tigers(home) 20-27 score:1 vs Cleveland Guardians(away) 26-22 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: cleveland guardians detroit tigers
- [Bing News]
- [Mon, 18 May 2026] cleveland guardians detroit tigers
- → The Detroit Tigers and Cleveland Guardians entered a rain delay before the start of Monday's series opener due to inclement weather at Comerica Park
- [Mon, 18 May 2026] Detroit Tigers weather, rain delay vs Guardians. When will game start?
- → The Cleveland Guardians are 26-22 and sit in first place in the American League Central. Aiming to increase their division lead, the Guardians' bull
- [Mon, 18 May 2026] Cleveland Guardians Reinstate Shawn Armstrong Before Series Against Tigers
- → DETROIT — One Detroit-versus-Cleveland series is over. Another begins tonight. The Tigers (20-27) open a four-game series against the Guardians (26-

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 34.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_ADVANTAGE
- **Catalyst Strength:** 0.60

### Reasoning
Market overprices YES at 42% vs 38% historical base rate; Detroit Tigers missing ace Skubal + Verlander strongly favors Cleveland; historical patterns suggest YES overpriced by 4-7%

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Cleveland Guardians'})` → INJURY [cleveland guardians] Gabriel Arias (SS): 10-Day-IL
INJURY [cleveland guardians] Carlos Herna
- `get_sports_data({'sport': 'mlb', 'team': 'Detroit Tigers'})` → INJURY [detroit tigers] Tarik Skubal (SP): 15-Day-IL
INJURY [detroit tigers] Troy Melton (RP): 60-Da
- `search_web({'query': 'Cleveland Guardians vs Detroit Tigers 2025 series preview'})` → [Mon, 18 May 2026] Google News
[Thu, 26 Mar 2026] Cleveland Guardians at Detroit Tigers odds, picks 
- `search_web({'query': 'Cleveland Guardians Detroit Tigers May 2026 series'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Guardians vs. Tigers (18 May, 2026) Live Score - E
- `get_market_context({'keyword': 'Guardians Tigers'})` → No related markets found for 'Guardians Tigers'
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `get_market_context({'keyword': 'baseball'})` → No related markets found for 'baseball'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*