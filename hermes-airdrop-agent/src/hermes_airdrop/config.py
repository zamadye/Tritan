"""Environment + YAML configuration loading.

Two hard rules this module enforces:

1. **Secrets never leave this module as plaintext.** ``Settings.dump()`` and
   ``__repr__`` redact. The CLI prints redacted output only.
2. **Missing keys are an explicit, actionable error**, not a crash 40 frames
   deep inside a browser action.

Layout follows Hermes' own convention (see
https://hermes-agent.nousresearch.com/docs/user-guide/configuration):
secrets live in ``.env``, everything else in ``config.yaml``.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

try:  # PyYAML is a hard dep at install time, but degrade gracefully.
    import yaml
except ImportError:  # pragma: no cover - exercised only on broken installs
    yaml = None  # type: ignore[assignment]

REPO_ROOT = Path(__file__).resolve().parents[2]

#: Every variable that must hold a secret. Never printed, never logged.
SECRET_KEYS: frozenset[str] = frozenset(
    {
        "ANTHROPIC_API_KEY",
        "OPENAI_API_KEY",
        "OPENROUTER_API_KEY",
        "NOUS_API_KEY",
        "GLM_API_KEY",
        "KIMI_API_KEY",
        "CUSTOM_API_KEY",
        "TELEGRAM_BOT_TOKEN",
        "NOTION_API_KEY",
        "BROWSER_USE_API_KEY",
        "BROWSERBASE_API_KEY",
        "FIRECRAWL_API_KEY",
        "GITHUB_TOKEN",
    }
)

#: Placeholder values shipped in .env.example. Treated as "not set".
# A value is "unset" when it is empty or still the shipped placeholder. Matched
# structurally rather than by provider prefix: zero or more "word-" segments
# followed by 3+ x's. That covers sk-xxx, sk-ant-xxx, sk-or-v1-xxx, xxx, xxxx,
# plus the usual your_key_here / changeme / <...> forms.
#
# Note the prefix is a *repetition* of one segment, not a single optional one —
# a placeholder like sk-ant-xxx has two hyphens.
PLACEHOLDER_RE = re.compile(
    r"^(?:(?:[A-Za-z0-9]+[-_])*)x{3,}$|^your[-_].*$|^changeme$|^<.*>$|^$", re.I
)

#: At least one of these must be present for the agent to reach a model at all.
MODEL_KEY_GROUPS: tuple[tuple[str, ...], ...] = (
    ("ANTHROPIC_API_KEY",),
    ("OPENAI_API_KEY",),
    ("OPENROUTER_API_KEY",),
    ("NOUS_API_KEY",),
    ("GLM_API_KEY",),
    ("KIMI_API_KEY",),
    ("CUSTOM_API_KEY",),
)


class ConfigError(Exception):
    """Raised for configuration problems the operator must fix by hand."""


def is_placeholder(value: str | None) -> bool:
    """True when a value is empty or still the shipped placeholder."""
    if value is None:
        return True
    v = value.strip()
    return v == "" or bool(PLACEHOLDER_RE.match(v))


def redact(key: str, value: str | None) -> str:
    """Return a printable, non-recoverable form of a secret.

    Keeps the first 4 and last 4 chars for long keys so an operator can tell
    two keys apart in a log, but never enough to reconstruct the value.
    """
    if key not in SECRET_KEYS:
        return value or ""
    if is_placeholder(value):
        return "<unset>"
    v = (value or "").strip()
    if len(v) <= 8:
        return "*" * len(v)
    return f"{v[:4]}{'*' * 8}{v[-4:]}"


def parse_env_text(text: str) -> dict[str, str]:
    """Parse .env file content. Handles ``export``, quotes, comments, blanks."""
    out: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip()
        if len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"'):
            val = val[1:-1]
        if key:
            out[key] = val
    return out


@dataclass
class Settings:
    """Resolved runtime settings."""

    env: dict[str, str] = field(default_factory=dict)
    source: Path | None = None

    # ---------------------------------------------------------------- secrets
    def get(self, key: str, default: str | None = None) -> str | None:
        """Fetch a value, treating placeholders as absent."""
        v = self.env.get(key, os.environ.get(key))
        return default if is_placeholder(v) else (v or "").strip()

    def get_secret(self, key: str) -> str | None:
        """Same as :meth:`get` but refuses non-secret keys, to prevent
        accidentally routing a config value through a secret code path."""
        if key not in SECRET_KEYS:
            raise ConfigError(f"{key} is not a registered secret key")
        return self.get(key)

    def has(self, key: str) -> bool:
        return self.get(key) is not None

    # --------------------------------------------------------------- loading
    @classmethod
    def load(cls, path: Path | None = None, env: dict[str, str] | None = None) -> "Settings":
        p = Path(path) if path else REPO_ROOT / ".env"
        data: dict[str, str] = {}
        used: Path | None = None
        if p.exists():
            data = parse_env_text(p.read_text(encoding="utf-8"))
            used = p
        if env:
            data.update({k: v for k, v in env.items() if v is not None})
        return cls(env=data, source=used)

    # ------------------------------------------------------------ validation
    def model_provider_keys(self) -> list[str]:
        """Which model credentials are actually present and usable."""
        found: list[str] = []
        for group in MODEL_KEY_GROUPS:
            if any(self.has(k) for k in group):
                found.extend(k for k in group if self.has(k))
        return sorted(set(found))

    def validate(self, *, require_model_key: bool = True) -> list[str]:
        """Return a list of human-readable problems. Empty list == healthy."""
        problems: list[str] = []
        if require_model_key and not self.model_provider_keys():
            names = " | ".join(g[0] for g in MODEL_KEY_GROUPS)
            problems.append(
                f"No usable model API key. Set one of: {names} in .env "
                f"(placeholders like 'sk-xxx' do not count)."
            )
        if self.get("TELEGRAM_BOT_TOKEN") and not self.get("TELEGRAM_CHAT_ID"):
            problems.append("TELEGRAM_BOT_TOKEN is set but TELEGRAM_CHAT_ID is missing — alerts cannot be delivered.")
        if self.get("CUSTOM_API_KEY") and not self.get("CUSTOM_BASE_URL"):
            problems.append("CUSTOM_API_KEY is set but CUSTOM_BASE_URL is missing — endpoint unknown.")
        leaked = self.find_leaked_secrets()
        if leaked:
            problems.append(
                "Refusing to run: private key material found in .env ("
                + ", ".join(leaked)
                + "). This tool stores addresses only."
            )
        return problems

    def find_leaked_secrets(self) -> list[str]:
        """Scan for wallet private keys / mnemonics pasted into .env.

        Returns the *key names* (never the values) of offending entries.
        """
        from .guardrails import classify_secret_material  # local import: avoids cycle

        bad: list[str] = []
        for k, v in self.env.items():
            if classify_secret_material(v) is not None:
                bad.append(k)
        return bad

    # ---------------------------------------------------------------- output
    def dump(self) -> dict[str, str]:
        """Safe, printable snapshot — secrets redacted."""
        return {k: redact(k, v) for k, v in sorted(self.env.items())}

    def __repr__(self) -> str:  # pragma: no cover - cosmetic
        return f"Settings(source={self.source}, keys={sorted(self.dump())})"


# ---------------------------------------------------------------------------
# YAML helpers
# ---------------------------------------------------------------------------


def load_yaml(path: Path) -> dict[str, Any]:
    if yaml is None:  # pragma: no cover
        raise ConfigError("PyYAML is required: pip install pyyaml")
    p = Path(path)
    if not p.exists():
        raise ConfigError(f"No such file: {p}")
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ConfigError(f"{p}: expected a YAML mapping at the top level")
    return data


_ENV_REF_RE = re.compile(r"\$\{(env:)?([A-Za-z_][A-Za-z0-9_]*)\}")


def expand_env(value: Any, env: dict[str, str] | None = None) -> Any:
    """Resolve ``${VAR}`` / ``${env:VAR}`` references the way Hermes does.

    Hermes leaves unknown placeholders verbatim and warns, rather than
    substituting an empty string — we match that behaviour so a typo is
    visible instead of silently becoming "".
    """
    if env is None:
        env = dict(os.environ)
    if isinstance(value, dict):
        return {k: expand_env(v, env) for k, v in value.items()}
    if isinstance(value, list):
        return [expand_env(v, env) for v in value]
    if isinstance(value, str):
        def sub(m: re.Match[str]) -> str:
            name = m.group(2)
            return env.get(name, m.group(0))  # keep verbatim when unset

        return _ENV_REF_RE.sub(sub, value)
    return value


def unresolved_refs(value: Any) -> list[str]:
    """List ``${VAR}`` names still unresolved after :func:`expand_env`."""
    found: list[str] = []

    def walk(v: Any) -> None:
        if isinstance(v, dict):
            for x in v.values():
                walk(x)
        elif isinstance(v, list):
            for x in v:
                walk(x)
        elif isinstance(v, str):
            for m in _ENV_REF_RE.finditer(v):
                found.append(m.group(2))

    walk(value)
    return sorted(set(found))


def iter_yaml_files(root: Path) -> Iterable[Path]:
    for p in sorted(Path(root).rglob("*.yaml")):
        yield p
    for p in sorted(Path(root).rglob("*.yml")):
        yield p
