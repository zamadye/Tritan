"""Evidence ledger: hashing, tamper detection, key-material refusal."""
from __future__ import annotations

import pytest

from fakes import EVM_PRIVATE_KEY

from hermes_airdrop.evidence import EvidenceError, Ledger, sha256_bytes, sha256_file


@pytest.fixture
def ledger(tmp_path):
    return Ledger.open(tmp_path / "logs" / "evidence.jsonl")


class TestHashing:
    def test_bytes_and_file_agree(self, tmp_path):
        data = b"proof"
        p = tmp_path / "f.bin"
        p.write_bytes(data)
        assert sha256_bytes(data) == sha256_file(p)

    def test_hash_is_stable(self):
        assert sha256_bytes(b"x") == sha256_bytes(b"x")


class TestAppend:
    def test_creates_parent_dirs(self, tmp_path):
        led = Ledger.open(tmp_path / "a" / "b" / "c.jsonl")
        led.append(campaign="x", action="y", outcome="ok")
        assert led.path.exists()

    def test_append_and_read_back(self, ledger):
        ledger.append(campaign="demo", action="check_in", outcome="ok", detail="done")
        recs = ledger.read()
        assert len(recs) == 1
        assert recs[0].campaign == "demo"
        assert recs[0].outcome == "ok"

    def test_jsonl_one_record_per_line(self, ledger):
        for i in range(3):
            ledger.append(campaign="demo", action=f"a{i}", outcome="ok")
        assert len(ledger.path.read_text().strip().splitlines()) == 3

    def test_invalid_outcome_rejected(self, ledger):
        with pytest.raises(EvidenceError):
            ledger.append(campaign="d", action="a", outcome="probably-fine")

    def test_hashes_the_artifact(self, ledger, tmp_path):
        art = tmp_path / "shot.png"
        art.write_bytes(b"\x89PNG fake")
        rec = ledger.append(campaign="d", action="a", outcome="ok", artifact=art)
        assert rec.sha256 == sha256_file(art)

    def test_missing_artifact_hashes_empty(self, ledger, tmp_path):
        rec = ledger.append(campaign="d", action="a", outcome="ok",
                            artifact=tmp_path / "gone.png")
        assert rec.sha256 == ""

    def test_tolerates_torn_final_line(self, ledger):
        ledger.append(campaign="d", action="a", outcome="ok")
        with open(ledger.path, "a") as fh:
            fh.write('{"campaign": "d", "acti')
        assert len(ledger.read()) == 1


class TestKeyRefusal:
    def test_private_key_in_detail_refused(self, ledger):
        key = EVM_PRIVATE_KEY
        with pytest.raises(EvidenceError) as ei:
            ledger.append(campaign="d", action="a", outcome="ok", detail=f"signed with {key}")
        assert "evm-private-key" in str(ei.value)

    def test_mnemonic_in_detail_refused(self, ledger):
        m = ("abandon ability able about above absent absorb abstract absurd "
             "abuse access accident")
        with pytest.raises(EvidenceError):
            ledger.append(campaign="d", action="a", outcome="ok", detail=m)

    def test_refused_write_leaves_no_record(self, ledger):
        with pytest.raises(EvidenceError):
            ledger.append(campaign="d", action="a", outcome="ok", detail="private_key=abc")
        assert ledger.read() == []


class TestQueries:
    def test_tail(self, ledger):
        for i in range(10):
            ledger.append(campaign="d", action=f"a{i}", outcome="ok")
        assert [r.action for r in ledger.tail(3)] == ["a7", "a8", "a9"]

    def test_for_campaign(self, ledger):
        ledger.append(campaign="a", action="x", outcome="ok")
        ledger.append(campaign="b", action="y", outcome="ok")
        assert [r.campaign for r in ledger.for_campaign("a")] == ["a"]

    def test_len_and_iter(self, ledger):
        ledger.append(campaign="d", action="a", outcome="ok")
        assert len(ledger) == 1
        assert len(list(ledger)) == 1

    def test_empty_ledger(self, ledger):
        assert ledger.read() == []
        assert ledger.tail() == []


class TestIntegrity:
    def test_clean_ledger_verifies(self, ledger, tmp_path):
        art = tmp_path / "s.png"
        art.write_bytes(b"data")
        ledger.append(campaign="d", action="a", outcome="ok", artifact=art)
        assert ledger.verify() == []

    def test_tampered_artifact_detected(self, ledger, tmp_path):
        art = tmp_path / "s.png"
        art.write_bytes(b"original")
        ledger.append(campaign="d", action="a", outcome="ok", artifact=art)
        art.write_bytes(b"tampered")
        problems = ledger.verify()
        assert len(problems) == 1
        assert "hash mismatch" in problems[0]

    def test_deleted_artifact_detected(self, ledger, tmp_path):
        art = tmp_path / "s.png"
        art.write_bytes(b"data")
        ledger.append(campaign="d", action="a", outcome="ok", artifact=art)
        art.unlink()
        assert any("missing" in p for p in ledger.verify())
