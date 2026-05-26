# Market Analysis — 2026-05-21 08:57 UTC

## Market
- **Question:** Israel closes its airspace by May 24?
- **Category:** geopolitik
- **YES Price:** 10.0%
- **Days Left:** 2
- **Volume 24h:** $71,487
- **Liquidity:** $50,597

## Statistical Prior
- **p_base:** 2.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,832 (+0.5% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,830 (+0.6% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Major AI model release → benchmark competition → sector excitement
- → AI regulation proposed → uncertainty → AI stocks fall short-term
- → AI chip shortage → NVIDIA revenue beats → AI infrastructure stocks rally
- → AI energy demand → data center power stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 4 sources for: israel closes airspace
- [Bing News]
- [Sat, 28 Feb 2026] israel closes airspace
- → TEMPO.CO, Jakarta Majid Akhavan, the spokesperson of the Iran Civil Aviation Organization, announced in an interview with the Mehr news agency on Sa
- [] Iran Closes Airspace as Israel Launches Attack
- [Al Jazeera]
- [Thu, 21 May 2026] Israel pushes for war amid US ceasefire, but its options may be limited
- [Thu, 21 May 2026] Hebron’s Ibrahimi Mosque illuminated in Israeli flag colours

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 2.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market at 10% is 5x the historical base rate (2%) with no clear imminent catalyst. Search results show Iran tensions but easing (Trump cancelled military strike). No breaking news of imminent Israeli airspace closure before May 24. Only 2 days remain. GEOPOLITIK category has abysmal 9% WR from 11 trades. While market appears overpriced vs base rate, lack of direct evidence and weak category performance make SKIP the prudent choice.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Israel airspace closure May 2025 latest news'})` → [Mon, 11 May 2026] Google News
[Mon, 27 Apr 2026] Middle East - The Latest News on Mobility and Trav
- `search_web({'query': 'Israel closes airspace May 24 2025 airspace closure threat'})` → [Mon, 27 Apr 2026] Google News
[Tue, 03 Mar 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Israel airspace closed May 2025 threat'})` → [Mon, 27 Apr 2026] Google News
[Sun, 30 Nov 2025] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Israel Iran tensions airspace closure May 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 03 May 2026] Trump cancels scheduled military strike on Iran, e
- `get_market_context({'keyword': 'Israel airspace'})` → No related markets found for 'Israel airspace'
- `get_market_context({'keyword': 'Israel Iran'})` → No related markets found for 'Israel Iran'
- `get_market_context({'keyword': 'Middle East conflict'})` → No related markets found for 'Middle East conflict'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*