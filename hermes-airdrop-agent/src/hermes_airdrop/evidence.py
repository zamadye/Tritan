"""Evidence ledger — a hash-stamped, append-only record of what happened.

Every action the agent takes writes one line to ``data/logs/evidence.jsonl``.
The line contains a SHA-256 of the action's proof artifact (a screenshot, a
response body) so that a later claim of "I did the check-in on the 12th" can
be checked against the bytes on disk.

Append-only JSONL, not a database: you can ``tail -f`` it, ``grep`` it, and it
survives a crash mid-write (worst case you lose the last line, not the file).
"""

from __future__ import annotations

import hashlib
import json
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

from .guardrails import classify_secret_material


class EvidenceError(Exception):
    pass


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path | str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


@dataclass
class Record:
    ts: str
    campaign: str
    action: str
    outcome: str  # ok | failed | skipped | halted
    detail: str = ""
    artifact: str = ""  # relative path to the proof file
    sha256: str = ""
    halted_reason: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Record":
        known = set(cls.__dataclass_fields__)  # type: ignore[attr-defined]
        return cls(**{k: v for k, v in d.items() if k in known})


@dataclass
class Ledger:
    path: Path
    _buffer: list[Record] = field(default_factory=list, repr=False)

    @classmethod
    def open(cls, path: Path | str) -> "Ledger":
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        return cls(path=p)

    # ------------------------------------------------------------------ write
    def append(
        self,
        *,
        campaign: str,
        action: str,
        outcome: str,
        detail: str = "",
        artifact: Path | str | None = None,
        halted_reason: str = "",
        when: datetime | None = None,
    ) -> Record:
        if outcome not in ("ok", "failed", "skipped", "halted"):
            raise EvidenceError(f"invalid outcome {outcome!r}")

        # Never let key material into the audit trail, even by accident.
        for label, text in (("detail", detail), ("artifact", str(artifact or ""))):
            if kind := classify_secret_material(text):
                raise EvidenceError(
                    f"refusing to log {label}: it contains {kind} material"
                )

        art = str(artifact) if artifact else ""
        digest = sha256_file(art) if artifact and Path(art).exists() else ""

        rec = Record(
            ts=(when or _utcnow()).isoformat(timespec="seconds"),
            campaign=campaign,
            action=action,
            outcome=outcome,
            detail=detail,
            artifact=art,
            sha256=digest,
            halted_reason=halted_reason,
        )
        with open(self.path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec.to_dict(), sort_keys=True) + "\n")
            fh.flush()
            os.fsync(fh.fileno())
        self._buffer.append(rec)
        return rec

    # ------------------------------------------------------------------- read
    def read(self) -> list[Record]:
        out: list[Record] = []
        if not self.path.exists():
            return out
        with open(self.path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(Record.from_dict(json.loads(line)))
                except (json.JSONDecodeError, TypeError):
                    continue  # tolerate a torn final line
        return out

    def tail(self, n: int = 20) -> list[Record]:
        return self.read()[-n:]

    def for_campaign(self, campaign: str) -> list[Record]:
        return [r for r in self.read() if r.campaign == campaign]

    def __iter__(self) -> Iterator[Record]:
        return iter(self.read())

    def __len__(self) -> int:
        return len(self.read())

    # ------------------------------------------------------------- integrity
    def verify(self) -> list[str]:
        """Re-hash every referenced artifact. Returns mismatch messages."""
        problems: list[str] = []
        for rec in self.read():
            if not rec.artifact or not rec.sha256:
                continue
            p = Path(rec.artifact)
            if not p.exists():
                problems.append(f"{rec.ts} {rec.campaign}/{rec.action}: artifact missing ({rec.artifact})")
                continue
            actual = sha256_file(p)
            if actual != rec.sha256:
                problems.append(
                    f"{rec.ts} {rec.campaign}/{rec.action}: hash mismatch "
                    f"(expected {rec.sha256[:12]}…, got {actual[:12]}…)"
                )
        return problems
