# Roster agent & fase debug per-agent

Strategi: **jangan nyalakan orkestrasi dulu.** Panggil dan amati tiap agent satu
per satu sampai stabil; baru rangkai orkestrasi. Orkestrasi di awal berisiko
error di tengah jalan tanpa tahu agent mana yang salah.

Jalankan satu agent dengan:

```bash
./scripts/debug-agent.sh --list          # lihat roster
./scripts/debug-agent.sh onboard "Kerjakan airdrop baru: <url>"
./scripts/debug-agent.sh daily  "Lanjutkan daily task untuk <slug>"
./scripts/debug-agent.sh research "Riset fakta & angka untuk <slug>"
./scripts/debug-agent.sh social "Buat & bagikan content X untuk <slug>"
./scripts/debug-agent.sh discord "Masuk Discord <slug>, simpan knowledge"
```

## Rantai kerja & handoff

```
Agent 1 onboard   masuk pertama: connect wallet, approve, quest utama s/d done
      │  menulis notes ke info.json (sisa daily, referral, status Discord)
      ▼
Agent 2 daily     HANYA daily task yang berulang (check-in/claim/like).
      │           jika daily-nya "create content" → serahkan ke Agent 4
      ▼
Agent 3 research  kumpulkan fakta/data/angka → data/campaigns/<slug>/research.md
      │           (bahan Agent 4; angka dicross-check 2 sumber, ber-tanggal)
      ▼
Agent 4 social    baca research.md + ambil referral → buat & posting content X
      ▼
Agent 5 discord   join Discord (atau #general bila sudah), ngobrol, simpan
                  knowledge ke research.md bagian discord:
```

## Konvensi handoff (file, bukan pesan)

| Diproduksi oleh | File | Dikonsumsi oleh |
|---|---|---|
| Agent 1 | `info.json` notes (referral, status) | 2, 4, 5 |
| Agent 3 | `research.md` | 4, 5 |
| Agent 5 | `research.md` (bagian `discord:`) | 3, 4 |
| semua | `evidence.jsonl` + screenshots | monitor |

Handoff lewat file agar tiap agent bisa di-debug terpisah tanpa saling
menunggu, dan hasilnya tetap ada walau salah satu agent error.

## Kapan orkestrasi boleh dinyalakan

Setiap agent harus lolos, diobservasi manual:
- mengerjakan task utuh tanpa berhenti minta instruksi (kecuali gate: signature/CAPTCHA),
- menulis output handoff yang benar,
- tidak mencoba membuka browser di luar profil yang dikelola.

Baru setelah itu `worker-orchestrator` + dispatcher kanban diaktifkan.
