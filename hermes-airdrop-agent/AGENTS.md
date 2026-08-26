# AGENTS.md — Project Memory (WAJIB DIBACA SEBELUM CODING)

> Baca file ini **sebelum** menulis kode apa pun. Kalau yang mau kamu kerjakan
> tidak ada di "Scope Masuk" atau bertentangan dengan "Keputusan Terkunci",
> berhenti dan tanya dulu. Jangan mengulang pekerjaan yang sudah tercatat di
> "Sudah Dikerjakan".

Terakhir diperbarui: 2026-08-25

---

## 1. Knowledge Purpose (jangan pernah lepas dari ini)

**Membangun sistem agent airdrop yang bisa dipakai orang awam lewat Telegram.**

Ukuran keberhasilannya bukan "kodenya canggih", tapi:

> User kirim teks airdrop ke bot Telegram → sistem paham task-nya →
> mengerjakan → melapor balik. User tidak pernah menyentuh terminal.

Segala keputusan teknis dinilai dari: **apakah ini membuat alur itu lebih
simpel bagi user?** Kalau tidak, jangan ditambah.

Yang BUKAN tujuan:
- Bukan tool anti-deteksi / sybil evasion
- Bukan framework generik — ini spesifik airdrop
- Bukan frontend/web UI — UI-nya Telegram

---

## 2. Scope Masuk vs Keluar

### MASUK (wajib ada di install.sh)

| Kategori | Item |
|---|---|
| **Runtime deps** | Python 3.10+, Node.js, uv/pip, ripgrep, Docker (opsional) |
| **Framework** | Hermes Agent (`curl .../install.sh \| bash`) |
| **Browser** | Chrome/Chromium + **CDP** di port 9222 (`browser.cdp_url`) |
| **Profiles** | Chrome `--user-data-dir` terpisah per identitas agent |
| **Skills** | 6 skill → `~/.hermes/skills/` |
| **System prompt** | `SOUL.md` per worker profile |
| **Memory** | `~/.hermes/memories/MEMORY.md`, `USER.md` + knowledge base proyek |
| **Knowledge** | Format task airdrop, aturan per proyek, pola verifikasi |
| **Gateway** | **Telegram** (`TELEGRAM_BOT_TOKEN`, `hermes gateway`) |
| **Control plane** | paket `hermes_airdrop` + CLI `haa` |
| **Cron** | `hermes cron` (bukan crontab sistem) |
| **Verifikasi** | `haa doctor`, `haa browser check`, test suite |

### KELUAR (jangan pernah ditambahkan)

- Fingerprint spoofing, anti-detect browser, rotasi proxy per-wallet,
  timing jitter anti-clustering
- CAPTCHA solving
- Auto-posting Discord / mass messaging
- Penyimpanan private key / seed phrase (alamat saja)
- Web UI / dashboard Next.js (UI = Telegram)

Alasan: Layer 2–4 dari model "identity isolation" tujuannya menipu sistem
anti-fraud protokol. Layer 1 (wallet tiering) tetap masuk sebagai manajemen
risiko biasa.

---

## 3. Keputusan Terkunci

| # | Keputusan | Alasan | Status |
|---|---|---|---|
| D1 | **Browser = Chrome via CDP**, bukan Camofox | Chrome asli = GUI sungguhan, bukan Xvfb 1×1. Login pakai cookie user sendiri. Konsisten dengan scope no-evasion. | ✅ 2026-08-25 |
| D2 | `browser.cdp_url` di config.yaml, **bukan** `/browser connect` | `/browser connect` itu slash command CLI interaktif, **tidak** di-dispatch gateway. Dari Telegram tidak akan jalan. | ✅ terverifikasi di docs |
| D3 | UI = **Telegram gateway** | `hermes gateway` + `TELEGRAM_BOT_TOKEN`. Native Hermes. | ✅ terverifikasi |
| D4 | Scoring proyek = kode deterministik, bukan LLM | Harus bisa diaudit berbulan-bulan kemudian | ✅ |
| D5 | Cron = `hermes cron`, bukan crontab sistem | Hanya Hermes cron yang menegakkan `approvals.cron_mode: deny` | ✅ |
| D6 | Identity per **role/task**, bukan per wallet | Session management wajar, bukan evasion | ✅ |
| D7 | Config divalidasi terhadap skema Hermes asli | Hermes diam-diam mengabaikan key tak dikenal | ✅ |
| D8 | Chrome jalan **di host**, bukan Docker | User pilih. GUI asli tanpa VNC, tanpa `--no-sandbox` | ✅ 2026-08-25 |
| D9 | Delegasi **3 lapis**: Orchestrator → Task Lead → Worker | User pilih. Tiap airdrop punya lead yang paham aturan proyek itu | ✅ 2026-08-25 |
| D10 | **1 identitas** dulu (satu Chrome profile) | User pilih. Buktikan alurnya jalan dulu | ✅ 2026-08-25 |
| D11 | `browser.backend: "off"` (built-in tools) | Accessibility tree + ref ID cukup untuk LLM, lebih bisa diaudit, tanpa dep tambahan. Ganti ke `browser-use` kalau perlu fleksibilitas lebih | ✅ |

---

## 4a. JEBAKAN KRITIS — Chrome 136+ (WAJIB TAHU)

Dari `website/docs/user-guide/features/browser.md`, verbatim:

> **Chrome 136+ makes the dedicated profile mandatory.** As a security
> hardening change, Chrome 136 and later **silently refuse to open the remote
> debugging port** when `--remote-debugging-port` is combined with the
> *default* user-data-dir — even from a cold start with no other Chrome
> running. The browser launches normally but nothing ever listens on 9222...
> **There is no error message.**

Konsekuensi: `start-browser.sh` **wajib** memakai `--user-data-dir` yang bukan
profil default. Kalau lupa, Chrome terlihat jalan normal tapi port 9222 tidak
pernah terbuka, dan tidak ada error apa pun. Selalu verifikasi dengan
`curl http://127.0.0.1:9222/json/version`.

Perintah yang benar:

```bash
google-chrome --remote-debugging-port=9222 \
  --user-data-dir="$HOME/.hermes/chrome-debug" \
  --no-first-run --no-default-browser-check &
```

---

## 4. Sudah Dikerjakan (JANGAN DIULANG)

- `src/hermes_airdrop/` — 11 modul, tanpa LLM call: analyzer, scheduler,
  campaign, executor, browser_check, hermes_schema, guardrails, wallets,
  evidence, notify, cli
- 6 skill di `skills/` dengan frontmatter Hermes yang benar
- 5 worker profile + SOUL.md di `config/hermes/profiles/`
- `tests/` — **768 test lulus**, termasuk yang menjalankan `install.sh --dry-run`
- `docs/research/` — hermes-schema.md, browser.md, sources.md
- Skema config Hermes sudah diekstrak dari `DEFAULT_CONFIG` (89 top-level key)

### Sudah dirombak (2026-08-25)

- `browser.camofox.*` → `browser.cdp_url` di semua 8 config; `docker-compose.yml` dihapus
- `install.sh` → system installer 10 langkah (apt/dnf/pacman/zypper/brew, Python,
  Node, Chrome, Hermes, haa, config, skills, memory+knowledge, env+gateway+cron)
- Telegram gateway: dicek & di-setup oleh installer
- `config/hermes/memories/{MEMORY,USER}.md` + `knowledge/*.md`
- `browser_check.py` → audit CDP (bukan Camofox/noVNC)
- `worker-orchestrator` + `worker-lead` (struktur 3 lapis)

### Selesai 2026-08-26

- `cron-jobs.sh` → 5 job, 3-layer aware. Orchestrator jalan 08:30 (sebelum
  worker 09:00) dengan sengaja. Semua job browser diawali preflight
  `haa browser check` yang berhenti cepat kalau Chrome tertutup.
- `README.md` ditulis ulang untuk arsitektur baru (Bahasa Indonesia)
- `docs/research/browser.md` diberi banner SUPERSEDED — risetnya tetap valid
  sebagai catatan, tapi bukan lagi panduan

### Selesai 2026-08-26 (sesi 2)

- **BUG KRITIS ditemukan:** `.gitignore` repo induk punya aturan `skills/` tanpa
  anchor, yang cocok dengan SEMUA direktori `skills/` termasuk punya kita.
  `git add` melewati path ter-ignore tanpa peringatan — jadi 6 SKILL.md tidak
  pernah masuk commit mana pun, sementara semua test hijau karena membaca
  working tree. Sudah diperbaiki: `skills/` → `/skills/` (di-anchor ke root).
  `tests/test_packaging.py` sekarang memeriksa pandangan *git*, bukan filesystem.
- `model:` di 8 config jadi env-driven (`HAA_MODEL_PROVIDER` / `CUSTOM_BASE_URL`
  / `HAA_MODEL_DEFAULT` / `HAA_CONTEXT_LENGTH`) — ganti provider cukup edit .env
- **`install.sh` sekarang symlink `.env` ke `$HERMES_HOME/.env` DAN ke tiap
  profile home.** Sebelumnya tidak, jadi semua `${VAR}` resolve jadi literal
  `"${VAR}"` dan Hermes gagal dengan gejala "nama model salah"
- `haa doctor` mendeteksi `${VAR}` yang tidak teresolve
- `.env.example`: duplikat `TELEGRAM_BOT_TOKEN` dihapus + test anti-duplikat

### Selesai 2026-08-26 (sesi 3) — kontrak otonomi

User menegaskan: task dinamis, UI dinamis, proyek banyak. Agent harus
menentukan sendiri tombol mana yang diklik — TIDAK boleh diinstruksikan per
klik dengan selector DOM (rapuh, gampang diblok, sering salah baca).

Diverifikasi dulu, bukan diasumsikan: **tidak ada satu pun selector DOM di
seluruh proyek** (src/, skills/, config/, knowledge/ = 0). Mekanisme Hermes
memang bukan selector — `browser_snapshot` mengembalikan accessibility tree
dengan ref ID yang dibuat ulang tiap snapshot.

Yang diperbaiki (dua gap nyata):
- Skill terbaca seperti checklist kaku → ditambah **"Autonomy contract"** di
  daily-executor & quest-executor: "Nobody tells you which button to click.
  You decide."
- `browser_snapshot` / `browser_vision` / `browser_get_images` **tidak pernah
  disebut** di skill mana pun → agent tidak diberi tahu alat persepsinya, jadi
  akan menebak. Sekarang diwajibkan, termasuk aturan ref bersifat per-snapshot.
- worker-lead SOUL: pembagian kerja eksplisit — lead mencatat APA, worker
  memutuskan BAGAIMANA. Dilarang menulis selector ke catatan kampanye.
- `tests/test_skills.py::TestNoBrittleInstructions` melarang querySelector,
  XPath, attribute selector, klik posisional, dan klik koordinat di semua file
  instruksi. Sudah diuji negatif: menangkap 5 jenis pelanggaran, tidak salah
  tuduh pada "#announcements" (nama channel Discord) maupun "click the claim
  button" (outcome-based, memang diizinkan).
- config.yaml mendokumentasikan trade-off `backend: off` vs `browser-use`
  beserta cara switch kalau ada proyek yang butuh.

### Selesai 2026-08-27 — task kompleks (puluhan langkah)

Riset guide nyata (Monad ~30-50 aksi di ~15 dApp, Abstract Chain streak 30 hari,
Base LP 30 hari) menunjukkan arsitektur sebelumnya TIDAK cukup. User memilih:
approval berjenjang, scope penuh, Monad sebagai acuan.

- **`guardrails.decide()` + `Tier`** — read/connect/testnet = otonom; mainnet
  dalam batas = otonom + lapor; unbounded grant (`setApprovalForAll`,
  `approve_unlimited`, `permit2`) = **manusia selalu, bahkan di testnet**
  (blind-approve itu kebiasaan, dan kebiasaan itu yang bikin rugi di mainnet).
  Network tak dikenal diperlakukan sebagai mainnet (fail-safe).
- **`ActionSpec` + `depends_on` / `group` / `tier` / `network`** — planner
  menolak aksi yang prasyaratnya belum selesai. Cycle & dependency tak dikenal
  gagal keras, bukan diam-diam.
- **Resume dari ledger** — `Store.completed_actions()` / `next_runnable()` /
  `blocked()`. Run mati di langkah 14/40 lanjut dari 14, tidak mengulang.
  Diturunkan dari ledger, bukan file pointer terpisah yang bisa drift.
- **`positions.py`** — state jangka panjang: LP/stake/badge dengan `until`,
  streak consecutive-day (gap me-reset, hari sama idempoten), `expiring_soon`,
  `at_risk_streaks`. CLI: `haa positions add|close|streak|list`.
- **`max_turns` dinaikkan** — lead 200, quests 400, daily 120 (1 dApp ≈ 8-15
  turn; 15 dApp = 120-225 turn, sebelumnya mentok di 120).
- **`knowledge/worked-example-monad.md`** — dekomposisi 4 layer (prerequisite
  gate / onboarding / long tail per dApp / recurring) + trap nyata.
- **Ekstensi browser = `kind: manual_setup`.** CDP tidak bisa install ekstensi
  Chrome (Primus, Miden). Blocker keras, butuh manusia sekali.

### Masih terbuka

- Alur Telegram end-to-end belum diuji terhadap Hermes sungguhan. **Bukan**
  karena kurang konfigurasi: sandbox ini memblokir TLS ke api.telegram.org dan
  ke installer Hermes (`SSL_ERROR_SYSCALL`), Hermes tidak terpasang, tidak ada
  browser, dan `DISPLAY` kosong. Harus dijalankan di mesin user.
- `docs/research/hermes-schema.md` + `sources.md` belum ditinjau ulang pasca-pivot
- `haa` belum punya subcommand untuk mendelegasikan task ke lead secara eksplisit

---

## 5. Fakta Terverifikasi (jangan asumsikan ulang)

```
# Hermes
~/.hermes/{config.yaml,.env,auth.json,SOUL.md,memories/,skills/,cron/,sessions/,logs/}
Profiles = home terpisah: ~/.hermes/profiles/<name>/{config.yaml,.env,SOUL.md}
Install : curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
Prereq  : git (+ curl, xz-utils di Linux). Python/Node diurus installer.
CLI     : hermes chat -q "..."   (BUKAN positional prompt)
Cron    : hermes cron create "0 9 * * *" "<prompt>" --name X --skill Y
Gateway : hermes gateway setup / run / start

# Browser CDP
browser.cdp_url  = "" # Optional persistent CDP endpoint for attaching to an
                      # existing Chromium/Chrome
browser.engine   = auto | chrome
/browser connect → http://127.0.0.1:9222  (CLI only, BUKAN gateway)

# Telegram
TELEGRAM_BOT_TOKEN, TELEGRAM_ALLOWED_USERS, TELEGRAM_HOME_CHANNEL,
TELEGRAM_CRON_THREAD_ID, TELEGRAM_WEBHOOK_URL
config: telegram.{reactions, channel_prompts, allowed_chats}

# Pola installer Hermes (setup-hermes.sh) — tiru urutan ini
uv → Python 3.11 → venv → dependencies → ripgrep → symlink hermes
→ sync bundled skills ke ~/.hermes/skills/ → next steps
```

### Key config Hermes yang TIDAK ADA (Hermes mengabaikan diam-diam)

`browser.camofox.url` · `memory.path` · `memory.persistence` · `cron.enabled` ·
`cron.jobs_dir` · `compression.summary_model` · `security.never_store_private_keys` ·
`security.stop_on_captcha` · `security.burner_only` ·
`security.require_approval_for_wallet` · `toolsets: [file_ops]` (yang benar `file`) ·
`system_prompt` (identity ada di `SOUL.md`)

---

## 6. Aturan Kerja

1. **Verifikasi sebelum klaim.** Setiap pernyataan tentang repo/sistem harus
   berasal dari tool call di giliran ini, bukan ingatan.
2. **Jalankan check-nya.** `python3 -m pytest tests/` harus lulus sebelum
   bilang selesai. Sebutkan fungsi apa yang benar-benar tereksekusi.
3. **Jangan bikin test yang meng-assert perilaku salah** lalu melemahkan test
   saat gagal. Kalau test gagal, cari tahu siapa yang salah.
4. **Test credential dibangun runtime** (`tests/fakes.py`) — jangan pernah
   menulis literal berbentuk API key asli. GitHub push protection menolak.
5. **Update file ini** setiap ada keputusan baru atau progress berarti.

### Perintah verifikasi

```bash
cd hermes-airdrop-agent
python3 -m pytest tests/                        # 599 test
./install.sh --dry-run                          # harus exit 0
PYTHONPATH=src python3 -m hermes_airdrop.cli browser check --offline
PYTHONPATH=src python3 -m hermes_airdrop.cli doctor --offline
for f in install.sh scripts/*.sh; do bash -n "$f"; done
```

---

## 7. Pertanyaan Terbuka (belum dijawab user)

1. Chrome jalan di **host** (GUI asli, tanpa Docker) atau di **container**?
   Ini menentukan apakah perlu `--no-sandbox` + VNC.
2. Berapa identitas agent paralel yang dibutuhkan, dan apakah tiap identitas
   perlu Chrome profile terpisah?
3. Struktur delegasi: berapa lapis di bawah orchestrator?

---

## 8. Progress Log

| Tanggal | Perubahan |
|---|---|
| 2026-08-25 | Riset sumber; backend Python 11 modul; 6 skill; 5 profile; 599 test; commit `fd01dc1` |
| 2026-08-25 | Koreksi: semua worker dapat browser; GUI default di compose |
| 2026-08-27 | **Task kompleks**: tiered approval, depends_on + planner, resume dari ledger, positions.py (LP/streak/expiry), max_turns dinaikkan, knowledge Monad. **768 test.** |
| 2026-08-26 | **Kontrak otonomi**: Autonomy contract di skill, alat persepsi diwajibkan, lead dilarang catat selector, `TestNoBrittleInstructions`. **704 test.** |
| 2026-08-26 | **Bug gitignore `skills/` ditemukan & diperbaiki** (6 SKILL.md tidak pernah ter-commit); model env-driven; install.sh symlink .env ke HERMES_HOME + profile; doctor deteksi `${VAR}`; `test_packaging.py`. **681 test.** |
| 2026-08-26 | `cron-jobs.sh` 5 job 3-layer + preflight CDP; README ditulis ulang; `browser.md` ditandai superseded. **620 test lulus.** |
| 2026-08-25 | **Pivot selesai:** Camofox → Chrome CDP di host (docker-compose.yml dihapus); install.sh jadi system installer 10 langkah; layer orchestrator + lead ditambahkan (7 profile); memory + knowledge base; Telegram gateway di installer; `browser_check` ditulis ulang untuk CDP. **617 test lulus.** |
