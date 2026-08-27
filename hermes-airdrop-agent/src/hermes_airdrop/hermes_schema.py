"""Validation of ``config.yaml`` against Hermes Agent's **real** config schema.

Why this module exists
----------------------
Hermes ignores unknown keys silently. A typo'd or invented setting does not
error at startup — it is simply dropped, and the agent quietly runs with a
default you never chose. That failure mode is invisible until a browser
session behaves strangely three days later.

The key sets below were extracted programmatically from Hermes' own
authoritative default config, ``hermes_cli/config_defaults.py::DEFAULT_CONFIG``
(commit-pinned in ``docs/research/hermes-schema.md``), unioned with the keys
documented in ``cli-config.yaml.example`` and ``website/docs``.

Usage
-----
    from hermes_airdrop.hermes_schema import validate_file
    report = validate_file(Path("config/hermes/config.yaml"))
    for issue in report.issues:
        print(issue.path, issue.message)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .config import load_yaml

# ---------------------------------------------------------------------------
# Schema data — extracted from NousResearch/hermes-agent DEFAULT_CONFIG
# ---------------------------------------------------------------------------

#: Top-level keys Hermes recognises. ``None`` value => free-form subtree.
TOP_LEVEL: dict[str, dict[str, Any] | None] = {
    "model": None,
    "providers": None,
    "fallback_providers": None,
    "credential_pool_strategies": None,
    "toolsets": None,
    "database": {
        "journal_mode": None,
        "wal_autocheckpoint": None,
        "journal_size_limit": None,
    },
    "runtime": {"nofile_soft_limit": None},
    "max_concurrent_sessions": None,
    "max_live_sessions": None,
    "agent": {
        "max_turns": None,
        "verbose": None,
        "reasoning_effort": None,
        "reasoning_overrides": None,
        "reasoning_echo": None,
        "personalities": None,
        "run_budget_seconds": None,
        "gateway_timeout": None,
        "gateway_timeout_warning": None,
        "gateway_turn_lease_timeout": None,
        "gateway_notify_interval": None,
        "gateway_startup_restore_drain_timeout": None,
        "gateway_auto_continue_freshness": None,
        "clarify_timeout": None,
        "api_max_retries": None,
        "service_tier": None,
        "tool_use_enforcement": None,
        "execution_guidance": None,
        "intent_ack_continuation": None,
        "stall_guards": None,
        "task_completion_guidance": None,
        "parallel_tool_call_guidance": None,
        "environment_probe": None,
        "environment_hint": None,
        "bot_mode_protocol": None,
        "coding_context": None,
        "coding_instructions": None,
        "verify_guidance": None,
        "max_verify_nudges": None,
        "verify_on_stop": None,
        "image_input_mode": None,
        "disabled_toolsets": None,
        "empty_response_guard": None,
        "agent_cache": None,
        "restart_drain_timeout": None,
        "restart_after_turn_timeout": None,
        "build_wait_timeout": None,
        "cron_drain_timeout": None,
        "session_stall_timeout": None,
        "reconnect_attention_after": None,
        "local_stream_stale_timeout": None,
    },
    "approvals": {
        "mode": None,
        "timeout": None,
        "cron_mode": None,
        "single_query_mode": None,
        "smart_policy": None,
        "denial_breaker_threshold": None,
        "deny": None,
        "mcp_reload_confirm": None,
        "destructive_slash_confirm": None,
    },
    "auxiliary": None,
    "bedrock": None,
    "bot_mode": None,
    "browser": {
        "backend": None,
        "inactivity_timeout": None,
        "command_timeout": None,
        "snapshot_threshold": None,
        "record_sessions": None,
        "headed": None,
        "allow_private_urls": None,
        "engine": None,
        "auto_local_for_private_urls": None,
        "cdp_url": None,
        "cloud_provider": None,
        "allow_unsafe_evaluate": None,
        "restrict_evaluate": None,
        "dialog_policy": None,
        "dialog_timeout_s": None,
        "camofox": {
            "managed_persistence": None,
            "user_id": None,
            "session_key": None,
            "adopt_existing_tab": None,
            "rewrite_loopback_urls": None,
            "loopback_host_alias": None,
        },
        "extension_control": {"enabled": None, "developer_mode": None},
    },
    "checkpoints": None,
    "code_execution": None,
    "command_allowlist": None,
    "compression": {
        "enabled": None,
        "progress_notices": None,
        "threshold": None,
        "threshold_tokens": None,
        "target_ratio": None,
        "protect_last_n": None,
        "protect_first_n": None,
        "min_tail_user_messages": None,
        "max_attempts": None,
        "tail_mode": None,
        "in_place": None,
        "micro_compact": None,
        "micro_compact_defrag_threshold_tokens": None,
        "micro_compact_every_n_turns": None,
        "idle_compact_after_seconds": None,
        "proactive_prune_tokens": None,
        "proactive_prune_min_result_chars": None,
        "proactive_prune_min_reclaim_tokens": None,
        "hygiene_failure_cooldown_seconds": None,
        "hygiene_hard_message_limit": None,
        "hygiene_timeout_seconds": None,
        "hygiene_total_ceiling_seconds": None,
        "context_timeout_seconds": None,
        "context_total_ceiling_seconds": None,
        "abort_on_summary_failure": None,
        "model_thresholds": None,
        "codex_app_server_auto": None,
        "codex_gpt55_autoraise": None,
        "codex_gpt55_autoraise_notice": None,
        "codex_responses_native": None,
        "codex_responses_compact_threshold": None,
    },
    "computer_use": None,
    "context": None,
    "context_file_max_chars": None,
    "cron": {
        "allow_agent_scheduling": None,
        "preflight": None,
        "model_drift_guard": None,
        "model": None,
        "model_provider": None,
        "provider": None,
        "chronos": None,
        "wrap_response": None,
        "mirror_delivery": None,
        "max_parallel_jobs": None,
        "output_retention": None,
        "script_timeout_seconds": None,
        "session_db_timeout_seconds": None,
        "media_send_timeout_seconds": None,
    },
    "curator": None,
    "dashboard": None,
    "delegation": None,
    "desktop": None,
    "discord": None,
    "display": None,
    "doctor": None,
    "file_read_max_chars": None,
    "gateway": None,
    "goals": None,
    "honcho": None,
    "hooks": None,
    "hooks_auto_accept": None,
    "human_delay": {"mode": None, "min_ms": None, "max_ms": None},
    "kanban": None,
    "logging": None,
    "loops": None,
    "lsp": None,
    "matrix": None,
    "mattermost": None,
    "mcp": None,
    "mcp_discovery_timeout": None,
    "mcp_single_query_discovery_timeout": None,
    "memory": {
        "memory_enabled": None,
        "user_profile_enabled": None,
        "memory_char_limit": None,
        "user_char_limit": None,
        "nudge_interval": None,
        "provider": None,
        "write_approval": None,
    },
    "moa": None,
    "model_catalog": None,
    "model_overrides": None,
    "models_dev": None,
    "monitoring": None,
    "network": None,
    "onboarding": None,
    "openrouter": None,
    "paste_collapse_char_threshold": None,
    "paste_collapse_threshold": None,
    "paste_collapse_threshold_fallback": None,
    "personalities": None,
    "platform_hints": None,
    "platform_toolsets": None,
    "prefill_messages_file": None,
    "privacy": None,
    "prompt_caching": None,
    "proxy": None,
    "quick_commands": None,
    "secrets": None,
    "security": {
        "allow_private_urls": None,
        "redact_secrets": None,
        "allow_data_training_tiers_noninteractive": None,
        "approval": {"transport": None, "transport_fallback": None},
        "protected_instruction_files": None,
        "protected_instruction_extra_patterns": None,
        "tirith_enabled": None,
        "tirith_path": None,
        "tirith_timeout": None,
        "tirith_fail_open": None,
        "website_blocklist": None,
        "acked_advisories": None,
        "allow_lazy_installs": None,
    },
    "session": None,
    "session_reset": {"mode": None, "idle_minutes": None, "at_hour": None},
    "sessions": None,
    "skills": {
        "external_dirs": None,
        "guard_agent_created": None,
        "inline_shell": None,
        "inline_shell_timeout": None,
        "ledger": None,
        "project_discovery": None,
        "template_vars": None,
        "tier1_advisory": None,
        "trusted_project_dirs": None,
        "write_approval": None,
        "creation_nudge_interval": None,
    },
    "slack": None,
    "streaming": None,
    "stt": None,
    "telegram": None,
    "telemetry": None,
    "terminal": None,
    "timezone": None,
    "tool_loop_guardrails": None,
    "tool_output": None,
    "tools": None,
    "tts": None,
    "updates": None,
    "vertex": None,
    "voice": None,
    "wake_word": None,
    "web": None,
    "whatsapp": None,
    "x_search": None,
    "group_sessions_per_user": None,
    "reasoning": None,
}

#: Toolset names accepted by ``toolsets:`` / ``--toolsets``.
#: Extracted from the registry in ``toolsets.py``.
VALID_TOOLSETS: frozenset[str] = frozenset(
    {
        "all",
        "bfl",
        "browser",
        "browser-use",
        "clarify",
        "coding",
        "cronjob",
        "debugging",
        "default",
        "delegation",
        "discord",
        "file",
        "hermes-acp",
        "hermes-api-server",
        "hermes-bluebubbles",
        "hermes-cli",
        "hermes-cron",
        "hermes-dingtalk",
        "hermes-discord",
        "hermes-email",
        "hermes-feishu",
        "hermes-gateway",
        "hermes-homeassistant",
        "hermes-matrix",
        "hermes-mattermost",
        "hermes-qqbot",
        "hermes-signal",
        "hermes-slack",
        "hermes-sms",
        "hermes-telegram",
        "hermes-webhook",
        "hermes-wecom",
        "hermes-wecom-callback",
        "hermes-weixin",
        "hermes-whatsapp",
        "hermes-yuanbao",
        "homeassistant",
        "honcho",
        "kanban",
        "memory",
        "process",
        "research",
        "safe",
        "search",
        "skills",
        "spotify",
        "terminal",
        "todo",
        "tools",
        "tour",
        "tts",
        "vision",
        "web",
    }
)

#: Accepted ``agent.reasoning_effort`` levels.
REASONING_LEVELS: frozenset[str] = frozenset(
    {"none", "minimal", "low", "medium", "high", "xhigh", "max", "ultra"}
)

#: Accepted ``browser.cloud_provider`` selections.
BROWSER_PROVIDERS: frozenset[str] = frozenset(
    {"browserbase", "browser-use", "camofox", "nous", "firecrawl"}
)

#: Keys that Hermes reads from ``.env``, not ``config.yaml``. Putting them in
#: YAML silently does nothing, so we flag them explicitly.
ENV_ONLY_KEYS: dict[str, str] = {
    "browser.camofox.url": "CAMOFOX_URL",
    "browser.camofox.port": "CAMOFOX_PORT",
}


# ---------------------------------------------------------------------------
# Report types
# ---------------------------------------------------------------------------

SEVERITY_ERROR = "error"
SEVERITY_WARNING = "warning"


@dataclass(frozen=True)
class Issue:
    severity: str
    path: str
    message: str
    hint: str | None = None

    def __str__(self) -> str:
        base = f"[{self.severity.upper()}] {self.path}: {self.message}"
        return f"{base}\n         ↳ {self.hint}" if self.hint else base


@dataclass
class Report:
    source: Path
    issues: list[Issue] = field(default_factory=list)

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == SEVERITY_ERROR]

    @property
    def warnings(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == SEVERITY_WARNING]

    @property
    def ok(self) -> bool:
        return not self.errors


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def _known_subkeys(section: str) -> dict[str, Any] | None:
    return TOP_LEVEL.get(section)


def validate(data: dict[str, Any], *, source: Path | None = None) -> Report:
    """Validate a parsed config mapping. Returns a :class:`Report`."""
    report = Report(source=source or Path("<memory>"))

    for key, value in data.items():
        if key not in TOP_LEVEL:
            report.issues.append(
                Issue(
                    SEVERITY_ERROR,
                    key,
                    f"unknown top-level key '{key}' — Hermes will ignore it",
                    "Remove it, or check the spelling against "
                    "hermes_cli/config_defaults.py::DEFAULT_CONFIG.",
                )
            )
            continue

        known = _known_subkeys(key)
        if known is None:
            continue  # free-form subtree, Hermes validates it
        if isinstance(value, dict):
            for sub in value:
                if sub in known:
                    continue
                # Keys that Hermes reads from the environment get one specific
                # message from _check_env_only_keys; don't double-report them
                # as a generic "unknown key".
                if f"{key}.{sub}" in ENV_ONLY_KEYS:
                    continue
                report.issues.append(
                    Issue(
                        SEVERITY_ERROR,
                        f"{key}.{sub}",
                        f"unknown key '{key}.{sub}'",
                        f"Valid keys under '{key}': {', '.join(sorted(known))}",
                    )
                )

        # ---- nested one level deeper for the sections we model explicitly
        if isinstance(value, dict):
            for sub, subval in value.items():
                subknown = known.get(sub)
                if isinstance(subknown, dict) and isinstance(subval, dict):
                    for leaf in subval:
                        if leaf in subknown:
                            continue
                        if f"{key}.{sub}.{leaf}" in ENV_ONLY_KEYS:
                            continue
                        report.issues.append(
                            Issue(
                                SEVERITY_ERROR,
                                f"{key}.{sub}.{leaf}",
                                f"unknown key '{key}.{sub}.{leaf}'",
                                f"Valid keys: {', '.join(sorted(subknown))}",
                            )
                        )

    _check_enum_values(data, report)
    _check_toolsets(data, report)
    _check_env_only_keys(data, report)
    return report


def _check_enum_values(data: dict[str, Any], report: Report) -> None:
    agent = data.get("agent")
    if isinstance(agent, dict):
        re_ = agent.get("reasoning_effort")
        if re_ is not None and str(re_) not in REASONING_LEVELS:
            report.issues.append(
                Issue(
                    SEVERITY_ERROR,
                    "agent.reasoning_effort",
                    f"'{re_}' is not a valid level",
                    f"Valid: {', '.join(sorted(REASONING_LEVELS))}",
                )
            )
        mt = agent.get("max_turns")
        if mt is not None and (not isinstance(mt, int) or isinstance(mt, bool) or mt < 1):
            report.issues.append(
                Issue(
                    SEVERITY_ERROR,
                    "agent.max_turns",
                    f"must be a positive integer, got {mt!r}",
                )
            )

    browser = data.get("browser")
    if isinstance(browser, dict):
        cp = browser.get("cloud_provider")
        if cp is not None and str(cp) not in BROWSER_PROVIDERS:
            report.issues.append(
                Issue(
                    SEVERITY_ERROR,
                    "browser.cloud_provider",
                    f"'{cp}' is not a supported provider",
                    f"Valid: {', '.join(sorted(BROWSER_PROVIDERS))}",
                )
            )

    comp = data.get("compression")
    if isinstance(comp, dict):
        thr = comp.get("threshold")
        if thr is not None and not (isinstance(thr, (int, float)) and 0 < thr <= 1):
            report.issues.append(
                Issue(
                    SEVERITY_ERROR,
                    "compression.threshold",
                    f"must be a fraction in (0, 1], got {thr!r}",
                )
            )


def _check_toolsets(data: dict[str, Any], report: Report) -> None:
    ts = data.get("toolsets")
    if ts is None:
        return
    if isinstance(ts, str):
        ts = [t.strip() for t in ts.split(",") if t.strip()]
    if not isinstance(ts, list):
        report.issues.append(
            Issue(SEVERITY_ERROR, "toolsets", "must be a list of toolset names")
        )
        return
    for name in ts:
        if str(name) not in VALID_TOOLSETS:
            near = _closest(str(name), VALID_TOOLSETS)
            report.issues.append(
                Issue(
                    SEVERITY_ERROR,
                    "toolsets",
                    f"'{name}' is not a registered toolset",
                    f"Did you mean '{near}'?" if near else None,
                )
            )


def _check_env_only_keys(data: dict[str, Any], report: Report) -> None:
    """Flag config keys that Hermes actually reads from the environment."""

    def get(path: str) -> Any:
        cur: Any = data
        for part in path.split("."):
            if not isinstance(cur, dict) or part not in cur:
                return None
            cur = cur[part]
        return cur

    for path, env_name in ENV_ONLY_KEYS.items():
        if get(path) is not None:
            report.issues.append(
                Issue(
                    SEVERITY_ERROR,
                    path,
                    f"'{path}' is read from the environment, not config.yaml",
                    f"Set {env_name} in .env instead.",
                )
            )


def _closest(name: str, options: frozenset[str]) -> str | None:
    """Cheap similarity pick so the error message can suggest a fix."""
    import difflib

    m = difflib.get_close_matches(name, list(options), n=1, cutoff=0.6)
    return m[0] if m else None


def validate_file(path: Path) -> Report:
    """Load and validate a YAML config file."""
    return validate(load_yaml(Path(path)), source=Path(path))
