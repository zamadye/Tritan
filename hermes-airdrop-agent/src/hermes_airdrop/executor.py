"""Work planning — turns campaigns + schedules into "what to do today".

This is the piece a human reads each morning. It is deliberately dumb: no LLM,
no browser, no side effects. It reads the store and emits an ordered plan.

The daily loop it feeds (see ``skills/daily-executor/SKILL.md``):

    plan  →  act  →  verify  →  log
              ↑         │
              └─ halt ──┘   (CAPTCHA / MFA / signature prompt → stop, alert)

"Verify" is not optional. An action that did not produce evidence is recorded
as ``failed``, never as ``ok`` — the source material is blunt that most
multi-wallet setups fail because nobody checked.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from .campaign import Campaign, Store
from .guardrails import HaltReason, requires_approval
from .scheduler import ScheduleError, describe, next_run, parse

SEVERITY_ORDER = {"blocked": 0, "needs_approval": 1, "scheduled": 2, "done": 3}


@dataclass
class PlannedAction:
    campaign: str
    action: str
    kind: str
    schedule: str
    next_fire: str
    needs_approval: bool
    blocked_by: str = ""

    @property
    def severity(self) -> str:
        if self.blocked_by:
            return "blocked"
        if self.needs_approval:
            return "needs_approval"
        return "scheduled"

    def to_dict(self) -> dict[str, Any]:
        d = self.__dict__.copy()
        d["severity"] = self.severity
        return d


@dataclass
class Plan:
    on: str
    actions: list[PlannedAction] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    streaks: dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "on": self.on,
            "actions": [a.to_dict() for a in self.actions],
            "warnings": self.warnings,
            "streaks": self.streaks,
            "counts": {
                "total": len(self.actions),
                "scheduled": len([a for a in self.actions if a.severity == "scheduled"]),
                "needs_approval": len([a for a in self.actions if a.severity == "needs_approval"]),
                "blocked": len([a for a in self.actions if a.severity == "blocked"]),
            },
        }

    def render(self) -> str:
        c = self.to_dict()["counts"]
        lines = [
            f"Airdrop plan for {self.on}",
            f"  {c['total']} action(s): {c['scheduled']} scheduled, "
            f"{c['needs_approval']} awaiting approval, {c['blocked']} blocked",
        ]
        if not self.actions:
            lines.append("  (nothing due — active campaigns may be finished or paused)")
        for a in sorted(self.actions, key=lambda x: (SEVERITY_ORDER[x.severity], x.campaign)):
            mark = {"blocked": "⛔", "needs_approval": "🔒", "scheduled": "▫"}[a.severity]
            extra = f"  [{a.blocked_by}]" if a.blocked_by else ""
            lines.append(
                f"  {mark} {a.campaign} :: {a.action} "
                f"({a.kind}, next {a.next_fire}){extra}"
            )
        if self.streaks:
            lines.append("  streaks: " + ", ".join(f"{k}={v}d" for k, v in sorted(self.streaks.items())))
        if self.warnings:
            lines.append("  warnings:")
            lines += [f"    ! {w}" for w in self.warnings]
        return "\n".join(lines)


def build_plan(
    store: Store,
    *,
    on: datetime | None = None,
    approved_actions: frozenset[str] = frozenset(),
) -> Plan:
    """Compute today's plan from the store.

    ``approved_actions`` is the operator's standing allow-list of action names
    that may run unattended. Spend-shaped actions are gated regardless — see
    :func:`~.guardrails.requires_approval`.
    """
    now = on or datetime.now(timezone.utc)
    plan = Plan(on=now.date().isoformat())
    active = store.by_status("active")

    if not active:
        plan.warnings.append(
            "No campaigns have status 'active'. Nothing will run until you set one: "
            "haa campaign set-status <slug> active"
        )

    for camp in active:
        plan.streaks[camp.slug] = store.streak(camp.slug, today=now.date())

        # Surface unparseable schedules here. actions_due() skips them so one
        # typo cannot abort the whole plan, but a silently-skipped action would
        # otherwise look identical to "nothing was due today".
        for spec in camp.actions:
            try:
                parse(spec.schedule)
            except ScheduleError as exc:
                plan.warnings.append(
                    f"{camp.slug}/{spec.name}: bad schedule {spec.schedule!r} ({exc})"
                )

        due = store.actions_due(camp.slug, on=now)
        if not due:
            plan.warnings.append(f"{camp.slug}: active but nothing scheduled for {plan.on}")
            continue

        for spec in due:
            try:
                nxt = next_run(parse(spec.schedule), after=now)
                fire = nxt.isoformat(timespec="minutes")
            except ScheduleError as exc:
                plan.warnings.append(f"{camp.slug}/{spec.name}: bad schedule {spec.schedule!r} ({exc})")
                fire = "?"

            blocked = ""
            if spec.kind == "wallet":
                blocked = (
                    "wallet action — review and sign manually; this system "
                    "does not hold keys"
                )

            plan.actions.append(
                PlannedAction(
                    campaign=camp.slug,
                    action=spec.name,
                    kind=spec.kind,
                    schedule=spec.schedule,
                    next_fire=fire,
                    needs_approval=(not blocked)
                    and requires_approval(spec.name, approved_actions=approved_actions),
                    blocked_by=blocked,
                )
            )

    return plan


def summarize(store: Store, *, since_days: int = 7, now: datetime | None = None) -> dict[str, Any]:
    """Weekly-rollup shape used by the monitor worker."""
    today = (now or datetime.now(timezone.utc)).date()
    rows: list[dict[str, Any]] = []
    for camp in store.all():
        prog = store.load_progress(camp.slug)
        recent = [
            e
            for e in prog.log
            if (today - datetime.fromisoformat(e.ts).date()).days <= since_days
        ]
        ok = [e for e in recent if e.status == "ok"]
        rows.append(
            {
                "campaign": camp.slug,
                "status": camp.status,
                "days_active": prog.days_active,
                "total_points": prog.total_points,
                "actions_7d": len(recent),
                "ok_7d": len(ok),
                "failure_rate_7d": round(1 - len(ok) / len(recent), 2) if recent else 0.0,
                "streak_days": store.streak(camp.slug, today=today),
                "open_issues": len(prog.issues),
                "verdict": (camp.verdict or {}).get("decision", "unrated"),
                "overall": (camp.verdict or {}).get("overall"),
            }
        )
    rows.sort(key=lambda r: (-(r["ok_7d"] or 0), r["campaign"]))
    return {
        "as_of": today.isoformat(),
        "window_days": since_days,
        "campaigns": rows,
        "totals": {
            "campaigns": len(rows),
            "active": len([r for r in rows if r["status"] == "active"]),
            "points": sum(r["total_points"] for r in rows),
            "actions_7d": sum(r["actions_7d"] for r in rows),
        },
    }
