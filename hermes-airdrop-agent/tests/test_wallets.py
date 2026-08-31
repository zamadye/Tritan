"""Wallet tier registry and the main-wallet firewall."""
from __future__ import annotations

import json
import os

import pytest

from fakes import EVM_PRIVATE_KEY

from hermes_airdrop.wallets import (
    FARMABLE_TIERS,
    TIER_FARMING,
    TIER_HIGH_RISK,
    TIER_MAIN,
    Registry,
    Wallet,
    WalletError,
    detect_chain,
    validate_address,
)

EVM = "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb0"
EVM2 = "0x1111111111111111111111111111111111111111"
SOL = "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM"
COSMOS = "cosmos1qypqxpq9qcrsszg2pvxq6rs0zqg3yyc5lzv7xu"


class TestChainDetection:
    @pytest.mark.parametrize("addr,chain", [(EVM, "evm"), (SOL, "solana"), (COSMOS, "cosmos")])
    def test_detects(self, addr, chain):
        assert detect_chain(addr) == chain

    def test_unknown(self):
        assert detect_chain("not-an-address") == "unknown"


class TestAddressValidation:
    def test_accepts_evm(self):
        assert validate_address(EVM) == EVM

    def test_strips_whitespace(self):
        assert validate_address(f"  {EVM}  ") == EVM

    def test_rejects_empty(self):
        with pytest.raises(WalletError):
            validate_address("")

    def test_rejects_garbage(self):
        with pytest.raises(WalletError):
            validate_address("hello")

    def test_rejects_private_key_disguised_as_address(self):
        key = EVM_PRIVATE_KEY
        with pytest.raises(WalletError) as ei:
            validate_address(key)
        assert "never stored" in str(ei.value)

    def test_rejects_labelled_key(self):
        with pytest.raises(WalletError):
            validate_address("private_key: whatever")


class TestWallet:
    def test_chain_autodetected(self):
        assert Wallet(address=SOL, tier=TIER_FARMING).chain == "solana"

    def test_invalid_tier_rejected(self):
        with pytest.raises(WalletError):
            Wallet(address=EVM, tier="yolo")

    def test_main_tier_is_not_farmable(self):
        assert Wallet(address=EVM, tier=TIER_MAIN).farmable is False

    @pytest.mark.parametrize("tier", sorted(FARMABLE_TIERS))
    def test_farmable_tiers(self, tier):
        assert Wallet(address=EVM, tier=tier).farmable is True

    def test_round_trip(self):
        w = Wallet(address=EVM, tier=TIER_FARMING, label="farm-1")
        assert Wallet.from_dict(w.to_dict()).to_dict() == w.to_dict()


class TestRegistry:
    def reg(self):
        r = Registry()
        r.add(Wallet(address=EVM, tier=TIER_MAIN, label="main"))
        r.add(Wallet(address=EVM2, tier=TIER_FARMING, label="farm-1"))
        return r

    def test_add_and_get(self):
        r = self.reg()
        assert r.get(EVM).tier == TIER_MAIN

    def test_duplicate_rejected(self):
        r = self.reg()
        with pytest.raises(WalletError):
            r.add(Wallet(address=EVM, tier=TIER_FARMING))

    def test_duplicate_allowed_with_replace(self):
        r = self.reg()
        r.add(Wallet(address=EVM, tier=TIER_HIGH_RISK), replace=True)
        assert len(r.wallets) == 2
        assert r.get(EVM).tier == TIER_HIGH_RISK

    def test_by_tier(self):
        assert [w.label for w in self.reg().by_tier(TIER_MAIN)] == ["main"]

    def test_remove(self):
        r = self.reg()
        assert r.remove(EVM) is True
        assert r.remove(EVM) is False

    def test_main_wallet_cannot_be_farmed(self):
        r = self.reg()
        with pytest.raises(WalletError) as ei:
            r.assert_farmable(EVM)
        assert "must never be used for farming" in str(ei.value)

    def test_farming_wallet_passes(self):
        assert self.reg().assert_farmable(EVM2).label == "farm-1"

    def test_unregistered_address_rejected(self):
        with pytest.raises(WalletError):
            self.reg().assert_farmable(SOL)


class TestAudit:
    def test_empty_registry_flags_missing_main(self):
        assert any("main" in p for p in Registry().audit())

    def test_healthy_registry_is_clean(self):
        assert self_healthy().audit() == []

    def test_two_main_wallets_flagged(self):
        r = self_healthy()
        r.add(Wallet(address=SOL, tier=TIER_MAIN))
        assert any("more than one" in p.lower() or "Consolidate" in p for p in r.audit())

    def test_no_farming_wallet_flagged(self):
        r = Registry()
        r.add(Wallet(address=EVM, tier=TIER_MAIN))
        assert any("farming" in p for p in r.audit())


def self_healthy():
    r = Registry()
    r.add(Wallet(address=EVM, tier=TIER_MAIN))
    r.add(Wallet(address=EVM2, tier=TIER_FARMING))
    return r


class TestPersistence:
    def test_save_and_load(self, tmp_path):
        p = tmp_path / "wallets.json"
        r = self_healthy()
        r.save(p)
        loaded = Registry.load(p)
        assert len(loaded.wallets) == 2
        assert loaded.get(EVM).tier == TIER_MAIN

    def test_saved_file_is_0600(self, tmp_path):
        p = tmp_path / "wallets.json"
        self_healthy().save(p)
        assert oct(os.stat(p).st_mode & 0o777) == "0o600"

    def test_missing_file_gives_empty_registry(self, tmp_path):
        assert Registry.load(tmp_path / "nope.json").wallets == []

    def test_save_creates_parent_dirs(self, tmp_path):
        p = tmp_path / "a" / "b" / "wallets.json"
        self_healthy().save(p)
        assert json.loads(p.read_text())["wallets"]
