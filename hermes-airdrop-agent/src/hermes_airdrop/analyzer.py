"""The 4-dimension project filter.

This is a deterministic encoding of the "Sniper" checklist described in
HTX Insights, *The Last Time I'll Talk About Backpack, and Also Discussing My
Airdrop Farming Principles* (author: Princess Christine / @0xsexybanana,
2026-03-23). The four dimensions and their sub-signals map 1:1 to the source:

1. **Team**      — smart enough, good enough execution, good enough heart
2. **Product**   — PMF, competent delivery, responsible attitude to quality
3. **Narrative** — promising unfalsified Web3 narrative + Web2 capital trend
4. **Timing**    — not peak FOMO, low participation cost, not overcrowded

It is deliberately *not* an LLM call. The LLM's job (see
``skills/airdrop-analyzer/SKILL.md``) is to gather evidence and fill in these
ratings with citations. Scoring itself must be reproducible: two runs on the
same ratings must give the same verdict, forever, so a past decision can be
audited.

Every rating is an integer 0-3 with a fixed meaning:

    0 = absent / actively bad     2 = clearly present
    1 = weak / unverified         3 = strong, independently verified
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any

MIN_RATING = 0
MAX_RATING = 3

# Decision labels
PRIORITIZE = "PRIORITIZE"
CONSIDER = "CONSIDER"
SKIP = "SKIP"

# Overall-score cut-offs (0-10 scale).
PRIORITIZE_AT = 7.0
CONSIDER_AT = 5.0

# Dimension weights. Product is weighted highest: the source is bluntest about
# it ("I never hand over a product full of low-level mistakes to users"), and
# a shoddy product predicts both a bad airdrop and a bad exit.
WEIGHTS: dict[str, float] = {
    "team": 0.25,
    "product": 0.30,
    "narrative": 0.20,
    "timing": 0.25,
}


def _check(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an int 0-3, got {value!r}")
    if not MIN_RATING <= value <= MAX_RATING:
        raise ValueError(f"{name} must be 0-3, got {value}")
    return value


@dataclass
class Evidence:
    """Ratings for one project, gathered by the analyzer agent.

    Each field should carry a citation in ``notes`` so the score is
    falsifiable later.
    """

    project: str
    url: str = ""

    # -- 1. Team -----------------------------------------------------------
    team_insight: int = 0  # founder content shows real industry understanding, not slogans
    team_execution: int = 0  # shipped, on time, iterated
    team_integrity: int = 0  # humility, honesty about failures, no shilling

    # -- 2. Product --------------------------------------------------------
    product_pmf: int = 0  # solves a real problem people pay to use
    product_delivery: int = 0  # competent; no low-level bugs in normal use
    product_responsibility: int = 0  # team owns quality, fixes fast

    # -- 3. Narrative ------------------------------------------------------
    narrative_web3: int = 0  # promising, not-yet-falsified Web3 narrative
    narrative_web2: int = 0  # aligns with a Web2 capital trend (AI, robotics…)
    narrative_premium: int = 0  # commands a valuation premium today

    # -- 4. Timing & cost --------------------------------------------------
    timing_fomo: int = 0  # INVERSE: 0 = calm market, 3 = peak feed-wide FOMO
    timing_cost: int = 0  # INVERSE: 0 = ~free to farm, 3 = expensive per action
    timing_crowding: int = 0  # INVERSE: 0 = few farmers, 3 = everyone is farming it

    # -- Operator signal ---------------------------------------------------
    hesitating: bool = False  # "If you feel hesitant, it's best not to participate."
    notes: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for f in (
            "team_insight",
            "team_execution",
            "team_integrity",
            "product_pmf",
            "product_delivery",
            "product_responsibility",
            "narrative_web3",
            "narrative_web2",
            "narrative_premium",
            "timing_fomo",
            "timing_cost",
            "timing_crowding",
        ):
            _check(f, getattr(self, f))

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Evidence":
        known = {f for f in cls.__dataclass_fields__}  # type: ignore[attr-defined]
        return cls(**{k: v for k, v in data.items() if k in known})


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------


def _to_ten(ratings: list[int]) -> float:
    """Map a set of 0-3 ratings onto 0-10."""
    if not ratings:
        return 0.0
    return round(sum(ratings) / (len(ratings) * MAX_RATING) * 10.0, 2)


@dataclass(frozen=True)
class DimensionScore:
    name: str
    score: float  # 0-10
    weight: float
    rationale: str

    @property
    def weighted(self) -> float:
        return round(self.score * self.weight, 3)


@dataclass(frozen=True)
class Verdict:
    project: str
    url: str
    decision: str  # PRIORITIZE | CONSIDER | SKIP
    overall: float  # 0-10
    dimensions: tuple[DimensionScore, ...]
    vetoes: tuple[str, ...]
    recommended_actions: tuple[str, ...]
    confidence: float  # 0-1, driven by how much evidence is still unverified
    created_at: str

    @property
    def needs_review(self) -> bool:
        """Below this, ask a human rather than acting autonomously."""
        return self.confidence < 0.7

    def to_dict(self) -> dict[str, Any]:
        return {
            "project": self.project,
            "url": self.url,
            "decision": self.decision,
            "overall": self.overall,
            "confidence": self.confidence,
            "dimensions": [
                {"name": d.name, "score": d.score, "weight": d.weight, "rationale": d.rationale}
                for d in self.dimensions
            ],
            "vetoes": list(self.vetoes),
            "recommended_actions": list(self.recommended_actions),
            "needs_review": self.needs_review,
            "created_at": self.created_at,
        }

    def render(self) -> str:
        """Human-readable block, matching the format the skill asks the LLM for."""
        lines = [
            f"Project: {self.project}",
            f"Overall Score: {self.overall:.1f}/10",
            f"Decision: {self.decision}",
            f"Confidence: {self.confidence:.2f}"
            + ("  (below 0.7 — human review required)" if self.needs_review else ""),
            "",
            "Reasoning:",
        ]
        for d in self.dimensions:
            lines.append(f"  · {d.name.capitalize()} ({d.score:.1f}/10, w={d.weight}): {d.rationale}")
        if self.vetoes:
            lines += ["", "Hard vetoes:"]
            lines += [f"  ! {v}" for v in self.vetoes]
        lines += ["", "Recommended Actions:"]
        lines += [f"  · {a}" for a in self.recommended_actions] or ["  · none"]
        return "\n".join(lines)


def _rate_team(e: Evidence) -> tuple[float, str]:
    parts = {
        "insight": e.team_insight,
        "execution": e.team_execution,
        "integrity": e.team_integrity,
    }
    # All three are required ("None can be missing") — the weakest gates it.
    weakest = min(parts.values())
    base = _to_ten(list(parts.values()))
    score = min(base, weakest / MAX_RATING * 10.0)
    weak = [k for k, v in parts.items() if v == weakest]
    return round(score, 2), f"weakest signal: {', '.join(weak)} ({weakest}/3)"


def _rate_product(e: Evidence) -> tuple[float, str]:
    parts = {
        "pmf": e.product_pmf,
        "delivery": e.product_delivery,
        "responsibility": e.product_responsibility,
    }
    return _to_ten(list(parts.values())), "PMF/delivery/quality-ownership averaged"


def _rate_narrative(e: Evidence) -> tuple[float, str]:
    parts = {
        "web3": e.narrative_web3,
        "web2": e.narrative_web2,
        "premium": e.narrative_premium,
    }
    return _to_ten(list(parts.values())), "narrative strength + Web2 capital alignment"


def _rate_timing(e: Evidence) -> tuple[float, str]:
    # All three inputs are inverse: 0 is good.
    inv = [MAX_RATING - e.timing_fomo, MAX_RATING - e.timing_cost, MAX_RATING - e.timing_crowding]
    return _to_ten(inv), "inverse of FOMO / cost / crowding"


def _vetoes(e: Evidence) -> list[str]:
    """Hard stops that force SKIP regardless of the arithmetic.

    These encode the source's categorical rules, which a weighted average would
    otherwise let a strong narrative paper over.
    """
    v: list[str] = []
    if e.product_delivery == 0:
        v.append(
            "Product delivery is unusable (0/3). The source treats shoddy "
            "delivery as disqualifying on its own."
        )
    if e.timing_crowding == 3:
        v.append(
            "Everyone is farming it. Overcrowded airdrops yield minimal or "
            "negative returns."
        )
    if e.hesitating:
        v.append("Operator is hesitating — 'if you feel hesitant, don't participate'.")
    if e.timing_cost == 3 and e.timing_fomo >= 2:
        v.append("High participation cost during peak FOMO.")
    return v


def _confidence(e: Evidence) -> float:
    """Confidence = fraction of signals that are *decisive* (0 or 3).

    A rating of 1 or 2 means "we looked but couldn't confirm", so it drags
    confidence down and pushes the verdict toward human review.
    """
    ratings = [
        e.team_insight,
        e.team_execution,
        e.team_integrity,
        e.product_pmf,
        e.product_delivery,
        e.product_responsibility,
        e.narrative_web3,
        e.narrative_web2,
        e.narrative_premium,
        e.timing_fomo,
        e.timing_cost,
        e.timing_crowding,
    ]
    decisive = sum(1 for r in ratings if r in (MIN_RATING, MAX_RATING))
    return round(decisive / len(ratings), 2)


def _recommend(e: Evidence, decision: str) -> list[str]:
    if decision == SKIP:
        return ["Do not participate. Record the reason and move on."]
    out: list[str] = []
    if e.product_delivery <= 1:
        out.append("Re-test the product weekly before committing volume.")
    if e.timing_fomo >= 2:
        out.append("Enter small; expand only if cost per action stays low.")
    if e.narrative_web2 <= 1:
        out.append("Track the Web2 narrative — if it cools, exit early.")
    out.append("Run a 3-5 action sequence weekly for at least 4 weeks before judging.")
    out.append("Keep this to one farming wallet tier; never the main wallet.")
    return out


def score(e: Evidence, *, now: datetime | None = None) -> Verdict:
    """Score one project and return a :class:`Verdict`."""
    if not e.project.strip():
        raise ValueError("Evidence.project must not be empty")

    dims: list[DimensionScore] = []
    for name, fn in (
        ("team", _rate_team),
        ("product", _rate_product),
        ("narrative", _rate_narrative),
        ("timing", _rate_timing),
    ):
        s, rationale = fn(e)
        dims.append(DimensionScore(name=name, score=s, weight=WEIGHTS[name], rationale=rationale))

    vetoes = _vetoes(e)
    overall = round(sum(d.weighted for d in dims), 2)
    # A veto caps the score so the report can never read as "high score, but skipped".
    if vetoes:
        overall = min(overall, 4.0)

    if vetoes or overall < CONSIDER_AT:
        decision = SKIP
    elif overall >= PRIORITIZE_AT:
        decision = PRIORITIZE
    else:
        decision = CONSIDER

    return Verdict(
        project=e.project.strip(),
        url=e.url.strip(),
        decision=decision,
        overall=overall,
        dimensions=tuple(dims),
        vetoes=tuple(vetoes),
        recommended_actions=tuple(_recommend(e, decision)),
        confidence=_confidence(e),
        created_at=(now or datetime.now(timezone.utc)).isoformat(timespec="seconds"),
    )
