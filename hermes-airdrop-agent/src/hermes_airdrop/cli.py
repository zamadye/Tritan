"""``haa`` — the Hermes Airdrop Agent control CLI.

Every subcommand is read-only or writes only inside ``data/``; none of them
drive a browser or sign anything. The browser work belongs to Hermes.

    haa doctor                     full health check
    haa config check               validate config.yaml against Hermes' schema
    haa analyze --project X ...    score a project on the 4 dimensions
    haa campaign add|list|show     manage campaigns
    haa plan [--date 2026-08-26]   what is due today
    haa report [--days 7]          weekly rollup
    haa wallets add|list|audit     wallet tier registry
    haa evidence tail|verify       audit trail
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import __version__
from .analyzer import Evidence, score
from .campaign import (
    STATUS_ACTIVE,
    VALID_STATUSES,
    ActionSpec,
    Campaign,
    CampaignError,
    Store,
    slugify,
)
from .config import REPO_ROOT, ConfigError, Settings, load_yaml
from .evidence import Ledger
from .executor import build_plan, summarize
from .hermes_schema import validate, validate_file
from .wallets import (
    FARMABLE_TIERS,
    TIER_FARMING,
    TIER_MAIN,
    VALID_TIERS,
    Registry,
    Wallet,
    WalletError,
)

DEFAULT_DATA = REPO_ROOT / "data"
DEFAULT_CONFIG = REPO_ROOT / "config" / "hermes" / "config.yaml"
WALLETS_FILE = "wallets.json"


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def _data_root(args: argparse.Namespace) -> Path:
    """Resolve the data/ root. ``--data-dir`` arrives as a str from argparse,
    so it must be wrapped before any path joining."""
    override = getattr(args, "data_dir", None)
    return Path(override) if override else DEFAULT_DATA


def _store(args: argparse.Namespace) -> Store:
    return Store(_data_root(args) / "campaigns")


def _ledger(args: argparse.Namespace) -> Ledger:
    return Ledger.open(_data_root(args) / "logs" / "evidence.jsonl")


def _registry_path(args: argparse.Namespace) -> Path:
    return _data_root(args) / WALLETS_FILE


def _emit(obj: Any, *, as_json: bool) -> None:
    print(json.dumps(obj, indent=2, sort_keys=True) if as_json else obj)


def _fail(msg: str) -> int:
    print(f"error: {msg}", file=sys.stderr)
    return 1


# ---------------------------------------------------------------------------
# doctor
# ---------------------------------------------------------------------------


def cmd_doctor(args: argparse.Namespace) -> int:
    ok = True

    print("Hermes Airdrop Agent — doctor")
    print("=" * 46)

    settings = Settings.load(getattr(args, "env_file", None))
    print(f"\n[1/6] environment   ({settings.source or 'no .env found'})")
    problems = settings.validate()
    if problems:
        ok = False
        for p in problems:
            print(f"  ✗ {p}")
    else:
        print(f"  ✓ model credential present: {', '.join(settings.model_provider_keys())}")
    if settings.get("TELEGRAM_BOT_TOKEN"):
        print("  ✓ TELEGRAM_BOT_TOKEN set")
        if not settings.get("TELEGRAM_ALLOWED_USERS"):
            print("  ! TELEGRAM_ALLOWED_USERS is empty — anyone who finds the bot "
                  "can drive your browser")
    else:
        print("  · TELEGRAM_BOT_TOKEN unset — the Telegram UI will not start")

    print("\n[2/6] hermes config.yaml")
    cfg_path = Path(getattr(args, "config", None) or DEFAULT_CONFIG)
    if not cfg_path.exists():
        print(f"  · not found at {cfg_path} (run install.sh)")
    else:
        report = validate_file(cfg_path)
        for issue in report.issues:
            print(f"  {'✗' if issue.severity == 'error' else '!'} {issue}")
            ok = ok and issue.severity != "error"
        if report.ok and not report.warnings:
            print(f"  ✓ schema valid ({cfg_path})")

    print("\n[3/6] worker profiles")
    prof_root = cfg_path.parent / "profiles"
    if prof_root.exists():
        for pdir in sorted(prof_root.iterdir()):
            if not pdir.is_dir():
                continue
            pfile = pdir / "config.yaml"
            if not pfile.exists():
                print(f"  ✗ {pdir.name}: no config.yaml")
                ok = False
                continue
            rep = validate_file(pfile)
            if rep.ok:
                print(f"  ✓ {pdir.name}")
            else:
                ok = False
                for i in rep.errors:
                    print(f"  ✗ {pdir.name}: {i}")
    else:
        print(f"  · no profiles directory at {prof_root}")

    print("\n[4/6] browser readiness (CDP Chrome)")
    from .browser_check import audit_all

    bcfg = Path(getattr(args, "config", None) or DEFAULT_CONFIG).parent
    browser_report = audit_all(
        bcfg,
        cdp_url=settings.get("BROWSER_CDP_URL") or "",
        live=not getattr(args, "offline", False),
    )
    for line in browser_report.render().splitlines()[1:]:
        print(line)
    if browser_report.errors:
        ok = False

    print("\n[5/6] wallet registry")
    reg = Registry.load(_registry_path(args))
    if not reg.wallets:
        print("  · no wallets registered (haa wallets add ...)")
    else:
        print(f"  ✓ {len(reg.wallets)} wallet(s): "
              + ", ".join(f"{w.tier}×{len(reg.by_tier(w.tier))}" for w in
                          sorted({x.tier: x for x in reg.wallets}.values(), key=lambda w: w.tier)))
        for p in reg.audit():
            print(f"  ! {p}")

    print("\n[6/6] campaigns")
    store = _store(args)
    camps = store.all()
    if not camps:
        print("  · no campaigns (haa campaign add ...)")
    else:
        print(f"  ✓ {len(camps)} campaign(s), {len(store.by_status(STATUS_ACTIVE))} active")
        led = _ledger(args)
        if led.path.exists():
            mismatches = led.verify()
            if mismatches:
                ok = False
                for m in mismatches[:5]:
                    print(f"  ✗ evidence: {m}")
            else:
                print(f"  ✓ evidence ledger intact ({len(led)} record(s))")

    print("\n" + ("doctor: all checks passed" if ok else "doctor: problems found (see ✗ above)"))
    return 0 if ok else 1


# ---------------------------------------------------------------------------
# config
# ---------------------------------------------------------------------------


def cmd_config_check(args: argparse.Namespace) -> int:
    path = Path(args.file)
    if args.text is not None:
        import yaml as _yaml

        report = validate(_yaml.safe_load(args.text) or {}, source=path)
    else:
        report = validate_file(path)
    if not report.issues:
        print(f"✓ {path}: schema valid")
        return 0
    for issue in report.issues:
        print(f"{'✗' if issue.severity == 'error' else '!'} {issue}")
    print(f"\n{len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return 1 if report.errors else 0


def cmd_config_show(args: argparse.Namespace) -> int:
    settings = Settings.load(getattr(args, "env_file", None))
    for k, v in settings.dump().items():
        print(f"{k}={v}")
    return 0


def cmd_browser_check(args: argparse.Namespace) -> int:
    """Standalone GUI-browser readiness check for every worker profile."""
    from .browser_check import audit_all

    settings = Settings.load(getattr(args, "env_file", None))
    cfg_root = Path(args.config).parent if args.config else DEFAULT_CONFIG.parent
    report = audit_all(
        cfg_root,
        cdp_url=args.url or settings.get("BROWSER_CDP_URL") or "",
        live=not args.offline,
    )
    print(report.render())
    if report.ok:
        print("\nbrowser: ready")
        return 0
    print("\nbrowser: NOT ready (see ✗ above)")
    return 1


# ---------------------------------------------------------------------------
# analyze
# ---------------------------------------------------------------------------

_RATING_FIELDS = (
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
)


def cmd_analyze(args: argparse.Namespace) -> int:
    if args.from_json:
        data = json.loads(Path(args.from_json).read_text(encoding="utf-8"))
        ev = Evidence.from_dict(data)
    else:
        ratings = {f: getattr(args, f) for f in _RATING_FIELDS}
        ev = Evidence(
            project=args.project,
            url=args.url or "",
            hesitating=args.hesitating,
            **ratings,
        )
    verdict = score(ev)
    if getattr(args, "json", False):
        print(json.dumps(verdict.to_dict(), indent=2, sort_keys=True))
    else:
        print(verdict.render())
        if verdict.needs_review:
            print(
                "\nnote: confidence is below 0.70 — treat this as provisional "
                "and have a human confirm before committing funds."
            )
    if getattr(args, "save_to", None):
        store = _store(args)
        slug = slugify(ev.project)
        if not store.exists(slug):
            store.save(Campaign(slug=slug, project=ev.project, url=ev.url, wallet_tier=TIER_FARMING))
        c = store.record_verdict(slug, verdict)
        store.save(c)
        print(f"\nsaved verdict to campaign '{slug}'")
    return 0 if verdict.decision != "SKIP" else 2


# ---------------------------------------------------------------------------
# campaigns
# ---------------------------------------------------------------------------


def cmd_campaign_add(args: argparse.Namespace) -> int:
    store = _store(args)
    slug = args.slug or slugify(args.project)
    if store.exists(slug) and not args.force:
        return _fail(f"campaign '{slug}' already exists (use --force to overwrite)")
    if args.tier not in FARMABLE_TIERS:
        return _fail(
            f"tier must be one of {sorted(FARMABLE_TIERS)} — the main wallet is never farmed"
        )
    actions = []
    for spec in args.action or []:
        name, _, sched = spec.partition("@")
        actions.append(ActionSpec(name=name.strip(), schedule=sched.strip() or "0 9 * * *"))
    camp = Campaign(
        slug=slug,
        project=args.project,
        url=args.url or "",
        status=args.status,
        wallet_tier=args.tier,
        actions=actions,
        notes=args.notes or "",
    )
    p = store.save(camp)
    print(f"✓ campaign '{slug}' -> {p}")
    if not actions:
        print("  hint: add actions with --action 'check_in@0 9 * * *'")
    return 0


def cmd_campaign_add_action(args: argparse.Namespace) -> int:
    store = _store(args)
    camp = store.load(args.slug)
    name, _, sched = args.spec.partition("@")
    sched = sched.strip() or "0 9 * * *"
    try:
        from .scheduler import describe, parse

        parse(sched)
    except Exception as exc:
        return _fail(f"bad schedule {sched!r}: {exc}")
    if any(a.name == name.strip() for a in camp.actions):
        return _fail(f"action '{name.strip()}' already exists on {args.slug}")
    camp.actions.append(
        ActionSpec(name=name.strip(), schedule=sched, kind=args.kind, notes=args.notes or "")
    )
    store.save(camp)
    from .scheduler import describe

    print(f"✓ {args.slug}: +{name.strip()} ({describe(sched)})")
    return 0


def cmd_campaign_set_status(args: argparse.Namespace) -> int:
    if args.status not in VALID_STATUSES:
        return _fail(f"status must be one of {sorted(VALID_STATUSES)}")
    store = _store(args)
    camp = store.load(args.slug)
    camp.status = args.status
    if args.status in ("done", "dropped"):
        camp.ended_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    store.save(camp)
    print(f"✓ {args.slug} -> {args.status}")
    return 0


def cmd_campaign_list(args: argparse.Namespace) -> int:
    store = _store(args)
    camps = store.all()
    if not camps:
        print("(no campaigns)")
        return 0
    if getattr(args, "json", False):
        print(json.dumps([c.to_dict() for c in camps], indent=2, sort_keys=True))
        return 0
    print(f"{'SLUG':24} {'STATUS':10} {'TIER':10} {'VERDICT':11} ACTIONS")
    for c in camps:
        v = (c.verdict or {}).get("decision", "-")
        o = (c.verdict or {}).get("overall")
        verdict = f"{v}({o})" if o is not None else v
        print(f"{c.slug:24} {c.status:10} {c.wallet_tier:10} {verdict:11} {len(c.actions)}")
    return 0


def cmd_campaign_show(args: argparse.Namespace) -> int:
    store = _store(args)
    camp = store.load(args.slug)
    prog = store.load_progress(args.slug)
    print(json.dumps({"campaign": camp.to_dict(), "progress": prog.to_dict()}, indent=2, sort_keys=True))
    return 0


def cmd_campaign_log(args: argparse.Namespace) -> int:
    store = _store(args)
    prog = store.log_action(
        args.slug, args.action, args.status, args.detail or "", points=args.points,
        evidence=args.evidence or "",
    )
    store.save_progress(prog)
    _ledger(args).append(
        campaign=args.slug, action=args.action, outcome=args.status, detail=args.detail or ""
    )
    print(f"✓ logged {args.action}={args.status} for {args.slug} (points today: {prog.points_today})")
    return 0


# ---------------------------------------------------------------------------
# plan / report
# ---------------------------------------------------------------------------


def _parse_date(s: str | None) -> datetime:
    if not s:
        return datetime.now(timezone.utc)
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        # Raised at call time, not during argparse, so use ValueError — that is
        # what main() turns into a clean "error:" line.
        raise ValueError(f"expected an ISO date like 2026-08-26, got {s!r}") from None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def cmd_plan(args: argparse.Namespace) -> int:
    plan = build_plan(
        _store(args),
        on=_parse_date(getattr(args, "date", None)),
        approved_actions=frozenset(args.approve or []),
    )
    if getattr(args, "json", False):
        print(json.dumps(plan.to_dict(), indent=2, sort_keys=True))
    else:
        print(plan.render())
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    data = summarize(_store(args), since_days=args.days)
    if getattr(args, "json", False):
        print(json.dumps(data, indent=2, sort_keys=True))
        return 0
    t = data["totals"]
    print(f"Airdrop report — {data['as_of']} (last {data['window_days']} days)")
    print(
        f"  {t['campaigns']} campaigns, {t['active']} active, "
        f"{t['actions_7d']} actions, {t['points']} points"
    )
    if data["campaigns"]:
        print(f"\n{'CAMPAIGN':24} {'STATUS':9} {'OK/7D':6} {'STREAK':7} {'VERDICT':9} POINTS")
        for r in data["campaigns"]:
            print(
                f"{r['campaign']:24} {r['status']:9} {r['ok_7d']:<6} "
                f"{r['streak_days']:<7} {r['verdict']:9} {r['total_points']}"
            )
    return 0


# ---------------------------------------------------------------------------
# wallets / evidence
# ---------------------------------------------------------------------------


def cmd_wallets_add(args: argparse.Namespace) -> int:
    path = _registry_path(args)
    reg = Registry.load(path)
    try:
        w = Wallet(address=args.address, tier=args.tier, label=args.label or "", notes=args.notes or "")
        reg.add(w, replace=args.force)
    except WalletError as exc:
        return _fail(str(exc))
    reg.save(path)
    print(f"✓ {w.address[:10]}… registered as '{w.tier}' ({w.chain})")
    if w.tier == TIER_MAIN:
        print("  main tier: never attach a campaign to this wallet.")
    return 0


def cmd_wallets_list(args: argparse.Namespace) -> int:
    reg = Registry.load(_registry_path(args))
    if not reg.wallets:
        print("(no wallets registered)")
        return 0
    print(f"{'TIER':10} {'CHAIN':8} {'ADDRESS':14} LABEL")
    for w in sorted(reg.wallets, key=lambda x: (x.tier, x.address)):
        masked = w.address[:6] + "…" + w.address[-4:]
        print(f"{w.tier:10} {w.chain:8} {masked:14} {w.label}")
    print("\n(addresses are truncated in output; the registry file holds them in full)")
    return 0


def cmd_wallets_audit(args: argparse.Namespace) -> int:
    reg = Registry.load(_registry_path(args))
    problems = reg.audit()
    if not problems:
        print("✓ wallet policy OK")
        return 0
    for p in problems:
        print(f"! {p}")
    return 1


def cmd_evidence_tail(args: argparse.Namespace) -> int:
    led = _ledger(args)
    for rec in led.tail(args.n):
        h = f" sha={rec.sha256[:12]}…" if rec.sha256 else ""
        print(f"{rec.ts}  {rec.campaign}/{rec.action}  [{rec.outcome}] {rec.detail}{h}")
    return 0


def cmd_evidence_verify(args: argparse.Namespace) -> int:
    led = _ledger(args)
    problems = led.verify()
    if not problems:
        print(f"✓ {len(led)} record(s), all artifacts verified")
        return 0
    for p in problems:
        print(f"✗ {p}")
    return 1


# ---------------------------------------------------------------------------
# init
# ---------------------------------------------------------------------------


def cmd_init(args: argparse.Namespace) -> int:
    """Create the data directories.

    Deliberately does *not* write a .env: install.sh owns that file, and a CLI
    command quietly creating one in the checkout would let a test run — or a
    stray invocation with --data-dir — leave a half-configured .env behind that
    a later real install then refuses to overwrite.
    """
    root = _data_root(args)
    for sub in ("campaigns", "logs", "screenshots"):
        (root / sub).mkdir(parents=True, exist_ok=True)
    print(f"✓ data directories ready at {root}")
    if not (REPO_ROOT / ".env").exists():
        print("  hint: no .env yet — run ./install.sh, or copy .env.example yourself")
    return 0


# ---------------------------------------------------------------------------
# parser
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="haa", description="Hermes Airdrop Agent control CLI")
    p.add_argument("--version", action="version", version=f"haa {__version__}")
    p.add_argument("--data-dir", help="override the data/ root (useful in tests)")
    p.add_argument("--env-file", help="override the .env path")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("doctor", help="full health check")
    sp.add_argument("--config", help="path to hermes config.yaml")
    sp.add_argument("--offline", action="store_true",
                    help="skip the live CDP probe")
    sp.set_defaults(func=cmd_doctor)

    br = sub.add_parser("browser", help="GUI browser readiness").add_subparsers(
        dest="sub2", required=True)
    brc = br.add_parser("check", help="verify every worker has a visible CDP browser")
    brc.add_argument("--config", help="path to hermes config.yaml")
    brc.add_argument("--url", help="CDP endpoint (default: from config.yaml / BROWSER_CDP_URL)")
    brc.add_argument("--offline", action="store_true", help="config audit only, no probe")
    brc.set_defaults(func=cmd_browser_check)

    cfg = sub.add_parser("config", help="configuration helpers").add_subparsers(dest="sub2", required=True)
    cc = cfg.add_parser("check", help="validate a Hermes config.yaml")
    cc.add_argument("file", nargs="?", default=str(DEFAULT_CONFIG))
    cc.add_argument("--text", help="validate YAML passed inline instead of a file")
    cc.set_defaults(func=cmd_config_check)
    cs = cfg.add_parser("show", help="print resolved .env with secrets redacted")
    cs.set_defaults(func=cmd_config_show)

    an = sub.add_parser("analyze", help="score a project on the 4 dimensions")
    an.add_argument("--project", help="project name")
    an.add_argument("--url", default="")
    an.add_argument("--from-json", help="read an Evidence object from a JSON file")
    an.add_argument("--hesitating", action="store_true", help="operator hesitation (auto-SKIP)")
    an.add_argument("--save-to", action="store_true", help="store the verdict on a campaign")
    an.add_argument("--json", action="store_true")
    for f in _RATING_FIELDS:
        an.add_argument(f"--{f.replace('_', '-')}", type=int, default=0, choices=range(4), metavar="0-3")
    an.set_defaults(func=cmd_analyze)

    camp = sub.add_parser("campaign", help="manage campaigns").add_subparsers(dest="sub2", required=True)
    ca = camp.add_parser("add")
    ca.add_argument("--project", required=True)
    ca.add_argument("--slug")
    ca.add_argument("--url", default="")
    ca.add_argument("--status", default="research", choices=sorted(VALID_STATUSES))
    ca.add_argument("--tier", default=TIER_FARMING, choices=sorted(VALID_TIERS))
    ca.add_argument("--action", action="append", metavar="NAME@CRON",
                    help="e.g. 'check_in@0 9 * * *' (repeatable)")
    ca.add_argument("--notes", default="")
    ca.add_argument("--force", action="store_true")
    ca.set_defaults(func=cmd_campaign_add)

    cact = camp.add_parser("add-action")
    cact.add_argument("slug")
    cact.add_argument("spec", metavar="NAME@CRON")
    cact.add_argument("--kind", default="browser", choices=["browser", "manual", "wallet"])
    cact.add_argument("--notes", default="")
    cact.set_defaults(func=cmd_campaign_add_action)

    css = camp.add_parser("set-status")
    css.add_argument("slug")
    css.add_argument("status")
    css.set_defaults(func=cmd_campaign_set_status)

    cl = camp.add_parser("list")
    cl.add_argument("--json", action="store_true")
    cl.set_defaults(func=cmd_campaign_list)

    csh = camp.add_parser("show")
    csh.add_argument("slug")
    csh.set_defaults(func=cmd_campaign_show)

    clog = camp.add_parser("log", help="record the outcome of one action")
    clog.add_argument("slug")
    clog.add_argument("action")
    clog.add_argument("status", choices=["ok", "failed", "skipped", "halted"])
    clog.add_argument("--detail", default="")
    clog.add_argument("--points", type=int, default=0)
    clog.add_argument("--evidence", default="")
    clog.set_defaults(func=cmd_campaign_log)

    pl = sub.add_parser("plan", help="what is due today")
    pl.add_argument("--date", help="ISO date, default today (UTC)")
    pl.add_argument("--approve", action="append", metavar="ACTION",
                    help="action name allowed to run unattended (repeatable)")
    pl.add_argument("--json", action="store_true")
    pl.set_defaults(func=cmd_plan)

    rp = sub.add_parser("report", help="rollup over a window")
    rp.add_argument("--days", type=int, default=7)
    rp.add_argument("--json", action="store_true")
    rp.set_defaults(func=cmd_report)

    wa = sub.add_parser("wallets", help="wallet tier registry").add_subparsers(dest="sub2", required=True)
    wad = wa.add_parser("add")
    wad.add_argument("--address", required=True)
    wad.add_argument("--tier", default=TIER_FARMING, choices=sorted(VALID_TIERS))
    wad.add_argument("--label", default="")
    wad.add_argument("--notes", default="")
    wad.add_argument("--force", action="store_true")
    wad.set_defaults(func=cmd_wallets_add)
    wal = wa.add_parser("list")
    wal.set_defaults(func=cmd_wallets_list)
    wau = wa.add_parser("audit")
    wau.set_defaults(func=cmd_wallets_audit)

    ev = sub.add_parser("evidence", help="audit trail").add_subparsers(dest="sub2", required=True)
    evt = ev.add_parser("tail")
    evt.add_argument("-n", type=int, default=20)
    evt.set_defaults(func=cmd_evidence_tail)
    evv = ev.add_parser("verify")
    evv.set_defaults(func=cmd_evidence_verify)

    ini = sub.add_parser("init", help="create data directories and a starter .env")
    ini.set_defaults(func=cmd_init)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args) or 0)
    except (CampaignError, ConfigError, WalletError, FileNotFoundError, ValueError) as exc:
        # A config or usage problem is an operator error, not a crash: print one
        # line and exit non-zero so cron and CI see the failure.
        return _fail(str(exc))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
