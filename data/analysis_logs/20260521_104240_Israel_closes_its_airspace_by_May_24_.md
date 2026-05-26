# Market Analysis — 2026-05-21 10:42 UTC

## Market
- **Question:** Israel closes its airspace by May 24?
- **Category:** geopolitik
- **YES Price:** 9.0%
- **Days Left:** 2
- **Volume 24h:** $71,192
- **Liquidity:** $42,487

## Statistical Prior
- **p_base:** 1.8%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.1%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,206 (-0.4% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,209 (-0.3% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
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
- [Mon, 11 May 2026] Iran Closes Airspace as Israel Launches Attack
- → Israel's secret military base in Iraq raises regional tensions. Permanent peace deal with Iran by June 30, 2026 at 16.5% YES; airspace closure by Ma
- [Tue, 12 May 2026] Israel operates secret military base in Iraq, escalating regional tensions
- → Israel deploys Iron Dome to the UAE amid Iran conflict. Permanent peace deal with Iran by June 30, 2026 at 16.5% YES.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 42%
- **p_true:** 1.8%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL_DEESCALATION
- **Catalyst Strength:** 0.30

### Reasoning
Mixed signals: IDF announced potential reopening May 5, suggesting airspace will be open by May 24 deadline. Market at 9% appropriately prices low probability. No verifiable edge - evidence slightly favors NO but confidence below 0.55 threshold. Past decisions on same market were SKIP with 45% confidence. GEOPOLITIK pattern shows weak 23% WR. Only 2 days remain with no imminent closure catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 42%<52%

## Tool Calls
- `search_web({'query': 'Israel airspace closure May 2025 Iran conflict'})` → [Mon, 27 Apr 2026] Google News
[Sun, 01 Mar 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Israel closes airspace May 2026'})` → [Mon, 18 May 2026] Google News
[Thu, 07 May 2026] Ryanair CEO warns European airlines face risks fro
- `get_market_context({'keyword': 'Israel airspace'})` → No related markets found for 'Israel airspace'
- `get_market_context({'keyword': 'Iran conflict'})` → No related markets found for 'Iran conflict'
- `search_web({'query': 'Israel Iran war airspace closure 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] El Al posts loss in first quarter of 2026 amid air
- `search_web({'query': 'Israel Ben Gurion airport closed war'})` → [Thu, 19 Mar 2026] Google News
[Mon, 04 May 2026] Ben Gurion airport shutdowns leave already disrupt
- `search_web({'query': '"airspace closures" Israel May 2026'})` → [Wed, 20 May 2026] Google News
[Mon, 11 May 2026] El Al posts loss in first quarter of 2026 amid air
- `search_web({'query': 'Israel airspace reopening May 2026'})` → [Mon, 27 Apr 2026] Google News
[Mon, 02 Mar 2026] Middle East Airspace – Current Operational Picture

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*