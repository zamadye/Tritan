"""Wallet tier registry — **addresses only, never keys**.

This module implements the one part of "multi-wallet hygiene" that is purely
defensive: keeping distinct pools of capital separated so that a mistake or a
malicious contract on a farming wallet cannot reach the funds you actually
care about.

What is deliberately **not** here
---------------------------------
No fingerprint generation, no proxy assignment, no timing jitter. Those exist
to make one operator's wallets look like several unrelated people to a
protocol's fraud-detection system. That is deception of the counterparty, and
this project does not implement it. See ``README.md`` § "Scope and limits" for
the full position, and ``skills/wallet-isolation/SKILL.md`` for what the agent
is told.

What *is* here is worth doing on its own merits even with a single wallet:

* the main wallet never touches a dApp front-end
* no private key, seed phrase, or keystore is ever written to disk
* every address is labelled with the tier it belongs to, so a script cannot
  accidentally sign with the wrong one
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .guardrails import classify_secret_material

# Wallet tiers, strictest first.
TIER_MAIN = "main"
TIER_FARMING = "farming"
TIER_HIGH_RISK = "high-risk"

VALID_TIERS = frozenset({TIER_MAIN, TIER_FARMING, TIER_HIGH_RISK})

#: Tiers that may be attached to a campaign.
FARMABLE_TIERS = frozenset({TIER_FARMING, TIER_HIGH_RISK})

_EVM_RE = re.compile(r"^0x[0-9a-fA-F]{40}$")
_SOL_RE = re.compile(r"^[1-9A-HJ-NP-Za-km-z]{32,44}$")
_COSMOS_RE = re.compile(r"^[a-z]{1,10}1[02-9ac-hj-np-z]{38,58}$")


class WalletError(Exception):
    pass


def detect_chain(address: str) -> str:
    """Best-effort chain detection from address shape."""
    a = address.strip()
    if _EVM_RE.match(a):
        return "evm"
    if _COSMOS_RE.match(a):
        return "cosmos"
    if _SOL_RE.match(a):
        return "solana"
    return "unknown"


def validate_address(address: str) -> str:
    """Return the normalised address, or raise :class:`WalletError`.

    Also refuses anything that looks like a *key* rather than an address —
    pasting a private key into a wallet list is an easy mistake and a
    catastrophic one.
    """
    a = (address or "").strip()
    if not a:
        raise WalletError("address is empty")
    if kind := classify_secret_material(a):
        raise WalletError(
            f"this looks like {kind} material, not an address. "
            "Private keys are never stored here."
        )
    if detect_chain(a) == "unknown":
        raise WalletError(f"unrecognised address format: {a[:8]}…")
    return a


@dataclass
class Wallet:
    address: str
    tier: str
    label: str = ""
    chain: str = ""
    notes: str = ""

    def __post_init__(self) -> None:
        self.address = validate_address(self.address)
        if self.tier not in VALID_TIERS:
            raise WalletError(
                f"invalid tier {self.tier!r}; expected one of {sorted(VALID_TIERS)}"
            )
        if not self.chain:
            self.chain = detect_chain(self.address)

    @property
    def farmable(self) -> bool:
        return self.tier in FARMABLE_TIERS

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Wallet":
        known = set(cls.__dataclass_fields__)  # type: ignore[attr-defined]
        return cls(**{k: v for k, v in d.items() if k in known})


@dataclass
class Registry:
    wallets: list[Wallet] = field(default_factory=list)
    updated_at: str = ""

    # ------------------------------------------------------------- collection
    def add(self, wallet: Wallet, *, replace: bool = False) -> Wallet:
        if self.get(wallet.address) and not replace:
            raise WalletError(f"wallet already registered: {wallet.address[:10]}…")
        if replace:
            self.wallets = [w for w in self.wallets if w.address != wallet.address]
        self.wallets.append(wallet)
        self.updated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
        return wallet

    def get(self, address: str) -> Wallet | None:
        for w in self.wallets:
            if w.address == address:
                return w
        return None

    def by_tier(self, tier: str) -> list[Wallet]:
        return [w for w in self.wallets if w.tier == tier]

    def remove(self, address: str) -> bool:
        before = len(self.wallets)
        self.wallets = [w for w in self.wallets if w.address != address]
        if len(self.wallets) != before:
            self.updated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
            return True
        return False

    # --------------------------------------------------------------- policy
    def assert_farmable(self, address: str) -> Wallet:
        """Guard used before any interaction. Raises on main-tier wallets."""
        w = self.get(address)
        if w is None:
            raise WalletError(f"address is not in the registry: {address[:10]}…")
        if not w.farmable:
            raise WalletError(
                f"wallet {w.address[:10]}… is tier '{w.tier}' and must never be "
                "used for farming interactions"
            )
        return w

    def audit(self) -> list[str]:
        """Policy problems an operator should fix."""
        problems: list[str] = []
        if not self.by_tier(TIER_MAIN):
            problems.append(
                "No 'main' wallet registered. Define one and keep it out of every "
                "dApp — it is the tier that must never sign anything."
            )
        if not self.by_tier(TIER_FARMING):
            problems.append("No 'farming' wallet registered; campaigns have nowhere safe to run.")
        mains = self.by_tier(TIER_MAIN)
        if len(mains) > 1:
            problems.append(
                f"{len(mains)} wallets are tier 'main'. Consolidate — more than one "
                "main wallet defeats the point of the tier."
            )
        return problems

    # ------------------------------------------------------------ persistence
    def to_dict(self) -> dict[str, Any]:
        return {
            "updated_at": self.updated_at,
            "wallets": [w.to_dict() for w in self.wallets],
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Registry":
        return cls(
            wallets=[Wallet.from_dict(w) for w in d.get("wallets", [])],
            updated_at=d.get("updated_at", ""),
        )

    @classmethod
    def load(cls, path: Path) -> "Registry":
        p = Path(path)
        if not p.exists():
            return cls()
        return cls.from_dict(json.loads(p.read_text(encoding="utf-8")))

    def save(self, path: Path) -> Path:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        # 0600: even though this holds no secrets, the addresses are still
        # information about where funds live.
        tmp = p.with_suffix(p.suffix + ".tmp")
        tmp.write_text(json.dumps(self.to_dict(), indent=2) + "\n", encoding="utf-8")
        os.chmod(tmp, 0o600)
        os.replace(tmp, p)
        return p
