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
- `tests/` — **599 test lulus**, termasuk yang menjalankan `install.sh --dry-run`
- `docs/research/` — hermes-schema.md, browser.md, sources.md
- Skema config Hermes sudah diekstrak dari `DEFAULT_CONFIG` (89 top-level key)

### Yang PERLU DIROMBAK (bukan diulang dari nol)

- `docker-compose.yml` + semua `browser.camofox.*` → ganti ke `browser.cdp_url`
- `install.sh` → naikkan dari "cek & suruh install" jadi **installer sistem**
  yang benar-benar memasang dependency (pola: `setup-hermes.sh` Hermes)
- Tambah setup **Telegram gateway** (belum ada sama sekali)
- Tambah setup **memory + knowledge base** (belum ada)
- `browser_check.py` → audit CDP, bukan Camofox/VNC

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
| 2026-08-25 | **Pivot: Camofox → Chrome CDP. Telegram jadi UI utama. install.sh jadi system installer.** (belum dikerjakan) |
