# Market Analysis — 2026-05-21 07:41 UTC

## Market
- **Question:** Israel closes its airspace by May 24?
- **Category:** geopolitik
- **YES Price:** 8.0%
- **Days Left:** 2
- **Volume 24h:** $70,799
- **Liquidity:** $37,958

## Statistical Prior
- **p_base:** 1.5%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 6.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,549 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,583 (+0.4% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving

### Bing/Google News
- 6 articles found:
- [NewsAPI] Trump cancels scheduled military strike on Iran, easing tensions: The decision to halt military action may foster diplomatic dialogue, reduc
- [NewsAPI] Trump discusses resuming combat operations against Iran with security team: Increased military tensions could destabilize regional security,
- [NewsAPI] Lufthansa to resume Israel flights in June, easing airspace closure concerns: Lufthansa's flight resumption signals improved regional stabil
- [NewsAPI] Israeli strikes on Iranian universities escalate conflict, impact peace deal pro: The escalation reduces peace prospects, heightens regional
- [NewsAPI] Iran closes Strait of Hormuz amid US-Israel conflict escalation: The closure of the Strait of Hormuz exacerbates global economic disruptions
- [NewsAPI] Israel operates secret military base in Iraq, escalating regional tensions: The secret base heightens regional instability, complicates peac
- [CAUSAL CHAINS] Relevant cause-effect patterns:

### Multi-Source
- [MULTI-SOURCE NEWS] 4 sources for: israel closes airspace
- [Al Jazeera]
- [Thu, 21 May 2026] Hebron’s Ibrahimi Mosque illuminated in Israeli flag colours
- [Wed, 20 May 2026] US condemns Israel’s Ben-Gvir while sanctioning Gaza flotilla organisers
- [The Guardian]
- [Wed, 20 May 2026] British Council staff in Italy to strike over proposed 80% workforce cut
- → p Far-right figure Itamar Ben-Gvir shares footage of himself taunting bound international detainees /p  p Israel’s far-right national security minis
- [Wed, 20 May 2026] Israeli security minister stirs diplomatic outrage with flotilla activist abuse video

## LLM Decision
- **Action:** SKIP
- **Confidence:** 42%
- **p_true:** 1.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL_TENSION
- **Catalyst Strength:** 0.20

### Reasoning
Market priced at 8% (4x base rate of 2%) with no imminent catalyst. News shows Israel closed airspace in June 2025 AFTER the May 24 deadline, confirming the historical pattern of rare closures. Current Iran tensions exist but no specific trigger for closure in remaining 2 days. GEOPOLITIK category has terrible 9% WR from 11 trades. Previous decisions on this exact market were correctly SKIPPED. Confidence far below 55% threshold - would need concrete evidence of imminent military strike to justify a bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 42%<52%

## Tool Calls
- `search_web({'query': 'Israel airspace closure May 2025'})` → [2026-05-18] Iran War: Trumps Makes New Threat as Buildup Continues; Middle East Data Centers, Key t
- `search_web({'query': 'Israel air defense airspace restrictions May 2025'})` → [2026-05-09] The Praxian Genocidal Kill Chain – Part 1 — In this two-part article series, Iain Davis
- `search_web({'query': '"Israel closes its airspace" 2025'})` → [Sun, 22 Jun 2025] Google News
[Fri, 13 Jun 2025] Israel closes its airspace in apparent precaution 
- `search_web({'query': 'Israel airspace May 2025 closure warning'})` → [2026-05-11] Board Of Trade, Ahoy! — In my never-ending quest to connect U.S.-China relations to the
- `search_web({'query': 'Israel airspace closure imminent May 2025 Iran attack'})` → [2026-05-18] Iran War: Trumps Makes New Threat as Buildup Continues; Middle East Data Centers, Key t
- `get_market_context({'keyword': 'Israel'})` → No related markets found for 'Israel'
- `search_web({'query': 'Israel airspace closure probability Polymarket'})` → [Thu, 07 May 2026] Google News
[Tue, 24 Mar 2026] When Will Iran Close Its Airspace? Polymarket Pred

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*