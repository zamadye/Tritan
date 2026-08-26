"""Hard-stop guardrails: key detection, page classification, approvals."""
from __future__ import annotations

import pytest

from hermes_airdrop.guardrails import (
    Halt,
    HaltReason,
    SPEND_ACTIONS,
    check_spend_limit,
    classify_secret_material,
    inspect_page,
    requires_approval,
    scan_text_for_keys,
)

from fakes import EVM_PRIVATE_KEY as EVM_KEY  # noqa: E402
MNEMONIC = (
    "abandon ability able about above absent absorb abstract absurd abuse access accident"
)


class TestSecretDetection:
    def test_raw_evm_private_key(self):
        assert classify_secret_material(EVM_KEY) == "evm-private-key"

    def test_0x_prefixed_evm_private_key(self):
        assert classify_secret_material("0x" + EVM_KEY) == "evm-private-key"

    def test_labelled_key(self):
        assert classify_secret_material("PRIVATE_KEY=anything-at-all") == "labelled-private-key"

    def test_seed_phrase_label(self):
        assert classify_secret_material("seed phrase: hello world") == "labelled-private-key"

    def test_pem_block(self):
        pem = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEE\n-----END EC PRIVATE KEY-----"
        assert classify_secret_material(pem) == "pem-private-key"

    def test_bip39_mnemonic(self):
        assert classify_secret_material(MNEMONIC) == "mnemonic-phrase"

    def test_24_word_mnemonic(self):
        words = MNEMONIC.split() * 2
        assert classify_secret_material(" ".join(words)) == "mnemonic-phrase"

    def test_normal_english_is_not_a_mnemonic(self):
        text = (
            "the quick brown fox jumps over the lazy dog near the river bank while "
            "seventeen sleepy owls watch quietly from tall pines above the valley floor"
        )
        assert classify_secret_material(text) is None

    def test_solana_secret_key(self):
        blob = "5" + "Kd" * 43  # 87 chars of base58-ish
        assert classify_secret_material(blob) == "solana-secret-key"

    @pytest.mark.parametrize("v", [None, "", "short", "https://example.com", "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb"])
    def test_clean_values(self, v):
        assert classify_secret_material(v) is None

    def test_returns_label_only_never_the_value(self):
        label = classify_secret_material(EVM_KEY)
        assert EVM_KEY not in label


class TestScanText:
    def test_flags_key_material(self):
        h = scan_text_for_keys(EVM_KEY)
        assert isinstance(h, Halt)
        assert h.reason is HaltReason.PRIVATE_KEY

    def test_clean_text_passes(self):
        assert scan_text_for_keys("just a normal log line") is None

    def test_halt_message_does_not_echo_the_key(self):
        h = scan_text_for_keys(EVM_KEY)
        assert EVM_KEY not in str(h)


class TestPageInspection:
    def test_captcha_detected(self):
        h = inspect_page("Please complete the CAPTCHA to continue", url="https://x.test")
        assert h and h.reason is HaltReason.CAPTCHA

    def test_cloudflare_challenge_detected(self):
        h = inspect_page("Just a moment... Checking your browser")
        assert h and h.reason is HaltReason.CAPTCHA

    def test_turnstile_detected(self):
        assert inspect_page("Verify you are human via Turnstile").reason is HaltReason.CAPTCHA

    def test_signature_prompt_detected(self):
        h = inspect_page("Confirm Transaction in your wallet")
        assert h and h.reason is HaltReason.SIGNATURE_REQUEST

    def test_dangerous_approval_detected(self):
        assert inspect_page("setApprovalForAll").reason is HaltReason.SIGNATURE_REQUEST

    def test_signature_beats_login_phrase(self):
        # A page mentioning both must halt on the signature, not the login.
        h = inspect_page("Please sign in, then Confirm Transaction")
        assert h.reason is HaltReason.SIGNATURE_REQUEST

    def test_mfa_detected(self):
        assert inspect_page("Enter the 6-digit code from your authenticator app").reason is HaltReason.MFA

    def test_expired_session_detected(self):
        assert inspect_page("Your session expired, please log in again").reason is HaltReason.LOGIN_EXPIRED

    def test_clean_page_passes(self):
        assert inspect_page("Welcome to the dashboard. Your points: 1,200") is None

    def test_empty_page_passes(self):
        assert inspect_page("") is None
        assert inspect_page(None) is None

    def test_halt_str_is_actionable(self):
        s = str(inspect_page("solve the captcha"))
        assert "HALT[captcha]" in s and "—" in s


class TestApprovalGating:
    @pytest.mark.parametrize("a", sorted(SPEND_ACTIONS))
    def test_spend_actions_always_need_approval(self, a):
        assert requires_approval(a) is True

    def test_spend_cannot_be_preapproved(self):
        # Even a standing allow-list must not auto-approve a transfer.
        assert requires_approval("transfer", approved_actions=frozenset({"transfer"})) is True

    def test_non_spend_can_be_preapproved(self):
        assert requires_approval("check_in", approved_actions=frozenset({"check_in"})) is False

    def test_non_spend_needs_approval_by_default(self):
        assert requires_approval("check_in") is True

    def test_case_and_whitespace_insensitive(self):
        assert requires_approval("  SWAP  ") is True


class TestSpendLimit:
    def test_under_limit_passes(self):
        assert check_spend_limit(1.0, 5.0) is None

    def test_at_limit_passes(self):
        assert check_spend_limit(5.0, 5.0) is None

    def test_over_limit_halts(self):
        h = check_spend_limit(5.01, 5.0)
        assert h and h.reason is HaltReason.SPEND_LIMIT
        assert "$5.01" in h.detail
