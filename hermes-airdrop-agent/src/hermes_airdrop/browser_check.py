"""Browser readiness audit.

Airdrop work is almost entirely GUI: connect wallet, click claim, approve,
sign, read a quest board. There is no CLI for any of it. So "does this worker
have a working, visible, persistent browser?" is not a nice-to-have — it is the
precondition for the whole system, and it must be *checked*, not assumed.

Three separate things have to be true, and they fail independently:

1. **The worker has browser tools.** A profile without ``browser`` in
   ``toolsets`` cannot touch a page at all. Hermes drops an unregistered or
   missing toolset silently, so this is easy to lose in an edit.
2. **The browser is visible.** Camofox always runs on an Xvfb virtual display,
   but at *1x1 resolution* unless the VNC plugin is enabled. Without
   ``ENABLE_VNC=1`` the browser is not merely headless — it is unwatchable, so
   nobody can solve the CAPTCHA or MFA prompt the agent halts on. Note that
   Hermes' own ``browser.headed`` only affects its *local Chromium* fallback;
   it does not make Camofox visible.
3. **The session persists.** Camofox keys its cookie/localStorage store by
   ``userId``. Without a stable ``browser.camofox.user_id`` plus
   ``managed_persistence``, every run starts logged out.

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

#: The noVNC path the Camofox VNC plugin serves the GUI on.
NOVNC_PATH = "/vnc.html"


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
    cloud_provider: str = ""
    backend: str = ""
    managed_persistence: bool = False
    user_id: str = ""
    adopt_existing_tab: bool = False
    headed: bool = False
    inactivity_timeout: int | None = None
    record_sessions: bool = False
    camofox_url: str = ""

    @property
    def persistent(self) -> bool:
        """True only when a session can actually survive a restart."""
        return self.managed_persistence and bool(self.user_id)


def inspect_profile(path: Path, *, name: str | None = None) -> ProfileBrowser:
    """Read a profile's config.yaml and extract its browser settings."""
    p = Path(path)
    data = load_yaml(p)
    b = data.get("browser") or {}
    cf = b.get("camofox") or {}
    ts = data.get("toolsets") or []
    if isinstance(ts, str):
        ts = [t.strip() for t in ts.split(",") if t.strip()]
    return ProfileBrowser(
        name=name or p.parent.name,
        path=p,
        has_browser_toolset="browser" in ts,
        toolsets=list(ts),
        cloud_provider=str(b.get("cloud_provider") or ""),
        backend=str(b.get("backend") or ""),
        managed_persistence=bool(cf.get("managed_persistence")),
        user_id=str(cf.get("user_id") or ""),
        adopt_existing_tab=bool(cf.get("adopt_existing_tab")),
        headed=bool(b.get("headed")),
        inactivity_timeout=b.get("inactivity_timeout"),
        record_sessions=bool(b.get("record_sessions")),
    )


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
    if not pb.cloud_provider:
        out.append(
            Finding(
                "error",
                pb.name,
                "browser.cloud_provider is unset — no browser backend selected",
                "Set browser.cloud_provider: camofox.",
            )
        )
    if pb.cloud_provider == "camofox" and pb.backend not in ("off", ""):
        out.append(
            Finding(
                "warn",
                pb.name,
                f"browser.backend is '{pb.backend}'; Camofox exposes no CDP endpoint, "
                "so the Browser Use harness cannot attach to it",
                'Set browser.backend: "off" to keep the built-in browser tools.',
            )
        )
    if not pb.managed_persistence:
        out.append(
            Finding(
                "error",
                pb.name,
                "camofox.managed_persistence is off — every run starts logged out",
                "Set browser.camofox.managed_persistence: true.",
            )
        )
    if pb.managed_persistence and not pb.user_id:
        out.append(
            Finding(
                "error",
                pb.name,
                "persistence is on but camofox.user_id is empty — the profile is "
                "random per session, so logins still do not survive",
                "Set a stable browser.camofox.user_id, e.g. 'haa-worker-daily'.",
            )
        )
    if not pb.headed:
        out.append(
            Finding(
                "warn",
                pb.name,
                "browser.headed is off — the local Chromium fallback would run invisibly",
                "Set browser.headed: true. (This does not affect Camofox; "
                "ENABLE_VNC=1 in the container is what makes Camofox visible.)",
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


def audit_user_id_collisions(profiles: list[ProfileBrowser]) -> list[Finding]:
    """Two workers sharing a user_id share a cookie jar and fight over tabs."""
    seen: dict[str, list[str]] = {}
    for pb in profiles:
        if pb.user_id:
            seen.setdefault(pb.user_id, []).append(pb.name)
    out: list[Finding] = []
    for uid, names in seen.items():
        if len(names) > 1:
            out.append(
                Finding(
                    "error",
                    ", ".join(sorted(names)),
                    f"share camofox.user_id '{uid}' — they will share one cookie jar "
                    "and contend for the same tabs",
                    "Give each worker its own user_id.",
                )
            )
    return out


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

    Any HTTP status counts as "up" — a 404 from the server still proves the
    server is listening, which is what this check is for.
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
    api: ProbeResult | None = None
    gui: ProbeResult | None = None

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.level == "error"]

    @property
    def ok(self) -> bool:
        return not self.errors and (self.api is None or self.api.ok)

    def render(self) -> str:
        lines = ["browser readiness"]
        for pb in self.profiles:
            flags = []
            flags.append("browser" if pb.has_browser_toolset else "NO-BROWSER")
            flags.append(pb.cloud_provider or "no-provider")
            flags.append("persistent" if pb.persistent else "EPHEMERAL")
            flags.append(f"user_id={pb.user_id or '-'}")
            flags.append("visible-fallback" if pb.headed else "headless-fallback")
            lines.append(f"  {pb.name:20} " + " · ".join(flags))
        for f in self.findings:
            lines.append("  " + str(f).replace("\n", "\n  "))
        if self.api:
            lines.append(f"  control API  {self.api}")
        if self.gui:
            lines.append(f"  GUI (noVNC)  {self.gui}")
        return "\n".join(lines)


def audit_all(
    root: Path,
    *,
    camofox_url: str = "",
    novnc_url: str = "",
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

    report.findings.extend(audit_user_id_collisions(report.profiles))

    if not report.profiles:
        report.findings.append(
            Finding("error", str(root), "no Hermes config found to audit")
        )
        return report

    if live and camofox_url:
        report.api = probe(camofox_url)
        if not report.api.ok:
            report.findings.append(
                Finding(
                    "error",
                    camofox_url,
                    f"the Camofox control API did not answer ({report.api.detail})",
                    "Run ./scripts/start-browser.sh, or: docker compose up -d",
                )
            )
        # The GUI is what makes take-over possible. Probe it whenever we know
        # where it should be.
        gui_target = novnc_url or _guess_novnc(camofox_url)
        if gui_target:
            report.gui = probe(gui_target, path=NOVNC_PATH)
            if not report.gui.ok:
                report.findings.append(
                    Finding(
                        "warn",
                        gui_target,
                        f"the noVNC GUI did not answer ({report.gui.detail}) — the "
                        "browser is running unwatchable, so nobody can take over "
                        "for a CAPTCHA or MFA prompt",
                        "Start Camofox with ENABLE_VNC=1 (docker compose up -d does "
                        "this by default).",
                    )
                )
    return report


def _label(path: Path, root: Path) -> str:
    """'main' for the top-level config, otherwise the profile directory name.

    A profile config sits at ``profiles/<name>/config.yaml``, so the label is
    the *parent* directory — ``path.parent.name``, not ``rel.parts[0]`` (which
    would be the literal string "profiles" for every single worker).
    """
    rel = path.relative_to(root)
    if str(rel) == "config.yaml":
        return "main"
    return path.parent.name


def _guess_novnc(camofox_url: str) -> str:
    """Derive the noVNC origin from the control-API origin.

    Compose maps 6080 alongside 9377 on the same host, so if we know one we can
    probe the other without being told.
    """
    import re

    m = re.match(r"^(https?://[^:/]+)(?::\d+)?(/.*)?$", camofox_url.rstrip("/"))
    if not m:
        return ""
    return f"{m.group(1)}:6080"
