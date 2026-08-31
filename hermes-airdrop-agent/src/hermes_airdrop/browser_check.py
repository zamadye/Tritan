"""Browser readiness audit for the CDP-Chrome setup.

Airdrop work is almost entirely GUI: connect wallet, click claim, approve,
sign, read a quest board. There is no CLI for any of it. So "does this worker
have a working, visible browser?" is the precondition for the whole system, and
it must be *checked*, not assumed.

Three things have to be true, and they fail independently:

1. **The worker has browser tools.** A profile without ``browser`` in
   ``toolsets`` cannot touch a page at all. Hermes drops a missing toolset
   silently, so this is easy to lose in an edit.

2. **Chrome is reachable over CDP.** ``browser.cdp_url`` must be set, and
   something must actually be listening. The nastiest failure mode here is
   Chrome 136+ silently refusing to open the debug port when
   ``--remote-debugging-port`` is combined with the *default* user-data-dir —
   the browser launches normally, nothing listens, and there is no error
   message. Only an HTTP probe catches it.

3. **The window is visible.** ``browser.headed: true`` makes local Chrome
   launch with a real window. This matters now in a way it did not under the
   old Camofox setup: for local Chrome the flag is honoured, and the visible
   window is how the operator takes over for a CAPTCHA or MFA prompt.

Persistence is a *host-side* property (Chrome's ``--user-data-dir``), not a
config key — so it is enforced by ``scripts/start-browser.sh``, which refuses
to launch without a dedicated profile directory. This module checks the parts
that live in config and probes the parts that live at runtime.

Nothing here talks to an LLM. :func:`probe` is the only part that touches the
network, and it is a plain HTTP GET.
"""

from __future__ import annotations

import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .config import load_yaml

#: CDP's self-describing endpoint. A 200 here means the debug port is open.
CDP_VERSION_PATH = "/json/version"


@dataclass(frozen=True)
class Finding:
    level: str  # error | warn | ok
    where: str
    message: str
    fix: str = ""

    def __str__(self) -> str:
        mark = {"error": "✗", "warn": "!", "ok": "✓"}[self.level]
        line = f"{mark} {self.where}: {self.message}"
        return f"{line}\n         ↳ {self.fix}" if self.fix else line


@dataclass
class ProfileBrowser:
    """What one profile's config says about its browser."""

    name: str
    path: Path
    has_browser_toolset: bool = False
    toolsets: list[str] = field(default_factory=list)
    cdp_url: str = ""
    engine: str = ""
    backend: str = ""
    headed: bool = False
    inactivity_timeout: int | None = None
    command_timeout: int | None = None
    record_sessions: bool = False

    @property
    def ready(self) -> bool:
        """Config-level readiness: tools present and a CDP endpoint named."""
        return self.has_browser_toolset and bool(self.cdp_url)


def inspect_profile(path: Path, *, name: str | None = None) -> ProfileBrowser:
    """Read a profile's config.yaml and extract its browser settings."""
    p = Path(path)
    data = load_yaml(p)
    b = data.get("browser") or {}
    ts = data.get("toolsets") or []
    if isinstance(ts, str):
        ts = [t.strip() for t in ts.split(",") if t.strip()]
    return ProfileBrowser(
        name=name or _default_name(p),
        path=p,
        has_browser_toolset="browser" in ts,
        toolsets=list(ts),
        cdp_url=str(b.get("cdp_url") or ""),
        engine=str(b.get("engine") or ""),
        backend=str(b.get("backend") or ""),
        headed=bool(b.get("headed")),
        inactivity_timeout=b.get("inactivity_timeout"),
        command_timeout=b.get("command_timeout"),
        record_sessions=bool(b.get("record_sessions")),
    )


def _default_name(path: Path) -> str:
    return "main" if path.name == "config.yaml" and path.parent.name == "hermes" else path.parent.name


def audit_profile(pb: ProfileBrowser) -> list[Finding]:
    """Check one profile for GUI browser readiness."""
    out: list[Finding] = []

    if not pb.has_browser_toolset:
        out.append(
            Finding(
                "error",
                pb.name,
                "no 'browser' in toolsets — this worker cannot open a page at all",
                "Add 'browser' to the toolsets list in its config.yaml.",
            )
        )

    if not pb.cdp_url:
        out.append(
            Finding(
                "error",
                pb.name,
                "browser.cdp_url is unset — the browser tools will not be offered at all",
                "Set browser.cdp_url: http://127.0.0.1:9222 and run "
                "./scripts/start-browser.sh.",
            )
        )
    elif not pb.cdp_url.startswith(("http://", "https://", "ws://", "wss://")):
        out.append(
            Finding(
                "error",
                pb.name,
                f"browser.cdp_url {pb.cdp_url!r} is not a URL",
                "Expected something like http://127.0.0.1:9222. An unresolved "
                "${VAR} placeholder lands here when the env var is unset.",
            )
        )

    if not pb.headed:
        out.append(
            Finding(
                "error",
                pb.name,
                "browser.headed is off — Chrome would run without a visible window, "
                "so nobody can take over for a CAPTCHA or MFA prompt",
                "Set browser.headed: true.",
            )
        )

    if pb.engine and pb.engine not in ("auto", "chrome", "chromium"):
        out.append(
            Finding(
                "warn",
                pb.name,
                f"browser.engine is '{pb.engine}'",
                "Expected 'chrome' (or 'auto'). Anything else is a different "
                "engine such as lightpanda, which cannot screenshot.",
            )
        )

    if pb.inactivity_timeout is not None and pb.inactivity_timeout < 300:
        out.append(
            Finding(
                "warn",
                pb.name,
                f"inactivity_timeout is {pb.inactivity_timeout}s — a slow claim flow "
                "can be reaped mid-action",
                "Raise it to at least 900s for dApp work.",
            )
        )

    return out


def _looks_like_unresolved(value: str) -> bool:
    """An unexpanded ``${VAR}`` means the env var was missing at load time."""
    return "${" in value


# ---------------------------------------------------------------------------
# Live probes
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ProbeResult:
    url: str
    ok: bool
    detail: str

    def __str__(self) -> str:
        return f"{'✓' if self.ok else '✗'} {self.url} — {self.detail}"


def probe(url: str, *, timeout: float = 4.0, path: str = "") -> ProbeResult:
    """GET a URL and report whether it answered.

    For the CDP probe specifically, a 200 on ``/json/version`` is the *only*
    reliable evidence the debug port is open — Chrome 136+ will otherwise look
    perfectly healthy while listening on nothing.
    """
    target = url.rstrip("/") + path
    req = urllib.request.Request(target, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return ProbeResult(url, True, f"HTTP {resp.status}")
    except urllib.error.HTTPError as exc:
        # The server answered; it just disliked the request.
        return ProbeResult(url, True, f"HTTP {exc.code} (server is up)")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        reason = getattr(exc, "reason", exc)
        return ProbeResult(url, False, str(reason))


@dataclass
class BrowserReport:
    profiles: list[ProfileBrowser] = field(default_factory=list)
    findings: list[Finding] = field(default_factory=list)
    cdp: ProbeResult | None = None

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.level == "error"]

    @property
    def ok(self) -> bool:
        return not self.errors and (self.cdp is None or self.cdp.ok)

    def render(self) -> str:
        lines = ["browser readiness"]
        for pb in self.profiles:
            flags = [
                "browser" if pb.has_browser_toolset else "NO-BROWSER",
                pb.cdp_url or "no-cdp-url",
                "visible" if pb.headed else "HEADLESS",
                f"engine={pb.engine or '-'}",
            ]
            lines.append(f"  {pb.name:20} " + " · ".join(flags))
        for f in self.findings:
            lines.append("  " + str(f).replace("\n", "\n  "))
        if self.cdp:
            lines.append(f"  CDP endpoint   {self.cdp}")
        return "\n".join(lines)


def audit_all(
    root: Path,
    *,
    cdp_url: str = "",
    live: bool = True,
) -> BrowserReport:
    """Audit the main config plus every worker profile under ``root``."""
    root = Path(root)
    report = BrowserReport()

    targets: list[Path] = []
    main = root / "config.yaml"
    if main.exists():
        targets.append(main)
    prof_root = root / "profiles"
    if prof_root.exists():
        targets.extend(sorted(prof_root.glob("*/config.yaml")))

    for path in targets:
        pb = inspect_profile(path, name=_label(path, root))
        report.profiles.append(pb)
        report.findings.extend(audit_profile(pb))

    if not report.profiles:
        report.findings.append(
            Finding("error", str(root), "no Hermes config found to audit")
        )
        return report

    # Prefer an explicit URL, then whatever the profiles declare.
    endpoint = cdp_url
    if not endpoint:
        declared = {pb.cdp_url for pb in report.profiles if pb.cdp_url}
        if len(declared) > 1:
            report.findings.append(
                Finding(
                    "warn",
                    "cdp_url",
                    f"profiles disagree on browser.cdp_url: {sorted(declared)}",
                    "Point them all at the same Chrome instance, or run one "
                    "Chrome per worker on distinct ports.",
                )
            )
        endpoint = sorted(declared)[0] if declared else ""

    if endpoint and _looks_like_unresolved(endpoint):
        report.findings.append(
            Finding(
                "error",
                "cdp_url",
                f"{endpoint!r} is an unresolved ${'{VAR}'} placeholder",
                "Set the env var, or hardcode the URL in config.yaml.",
            )
        )
        return report

    if live and endpoint:
        report.cdp = probe(endpoint, path=CDP_VERSION_PATH)
        if not report.cdp.ok:
            report.findings.append(
                Finding(
                    "error",
                    endpoint,
                    f"nothing is listening on the CDP port ({report.cdp.detail})",
                    "Run ./scripts/start-browser.sh. If Chrome appears to be "
                    "running anyway, this is the Chrome 136+ trap: close every "
                    "Chrome window and re-run, so it starts with the dedicated "
                    "--user-data-dir instead of joining your default profile.",
                )
            )
    return report


def _label(path: Path, root: Path) -> str:
    """'main' for the top-level config, otherwise the profile directory name."""
    rel = path.relative_to(root)
    if str(rel) == "config.yaml":
        return "main"
    return path.parent.name
