# Market Analysis — 2026-05-21 06:14 UTC

## Market
- **Question:** Israel closes its airspace by May 24?
- **Category:** geopolitik
- **YES Price:** 15.0%
- **Days Left:** 2
- **Volume 24h:** $58,146
- **Liquidity:** $35,324

## Statistical Prior
- **p_base:** 4.3%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 10.7%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,730 (+0.8% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,680 (+0.7% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Major AI model release → benchmark competition → sector excitement
- → AI regulation proposed → uncertainty → AI stocks fall short-term
- → AI chip shortage → NVIDIA revenue beats → AI infrastructure stocks rally
- → AI energy demand → data center power stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 5 sources for: israel closes airspace
- [Bing News]
- [Sat, 28 Feb 2026] israel closes airspace
- → TEMPO.CO, Jakarta Majid Akhavan, the spokesperson of the Iran Civil Aviation Organization, announced in an interview with the Mehr news agency on Sa
- [Sun, 17 May 2026] Iran Closes Airspace as Israel Launches Attack
- → Key Takeaways – The movement of the Turkish flotilla towards Israel appears to increase the potential for Israeli airspace closure. – Market pricing
- [Fri, 08 May 2026] Turkish flotilla nears Israel, Netanyahu to discuss defense response
- → When a corridor closes, replacement routings add anywhere from forty minutes to three hours per sector, which translates into extra fuel burn, paylo

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 4.3%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL_TENSION
- **Catalyst Strength:** 0.30

### Reasoning
Market price (15%) is 3.75x historical base rate (4%), but no clear imminent catalyst for airspace closure by May 24. Conflicting news: Lufthansa resuming flights in June suggests openness, while some airlines suspending flights indicates ongoing tensions. With only 2 days left, unlikely concrete catalyst will emerge. Low conviction.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Israel airspace closure May 24 2025'})` → [Mon, 27 Apr 2026] Google News
[Thu, 23 Apr 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Israel close airspace security threat April 2026'})` → [Mon, 11 May 2026] Google News
[Mon, 27 Apr 2026] US military aircraft at Ben Gurion Airport amid Is
- `search_web({'query': '"US military aircraft at Ben Gurion Airport" Israel airspace closure'})` → [Mon, 11 May 2026] Google News
[Wed, 13 May 2026] US military aircraft at Ben Gurion Airport amid Is
- `search_web({'query': 'Lufthansa resume Israel flights June airspace closure concerns'})` → [Wed, 13 May 2026] Google News
[Wed, 13 May 2026] Lufthansa to resume Israel flights in June, easing
- `search_web({'query': 'international airlines suspend flights Tel Aviv May 2026'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] American Airlines to Extend Tel Aviv Suspension Un
- `get_market_context({'keyword': 'Israel airspace'})` → No related markets found for 'Israel airspace'
- `get_market_context({'keyword': 'Israel flight'})` → No related markets found for 'Israel flight'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*