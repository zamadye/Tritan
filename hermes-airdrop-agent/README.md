# Hermes Airdrop Agent

Kirim task airdrop ke bot Telegram. Sistem memahaminya, mengerjakannya, dan
melapor balik. Anda tidak perlu membuka terminal.

```bash
./install.sh --dry-run   # lihat 10 langkahnya dulu, tidak mengubah apa pun
./install.sh
nano .env                # API key model + token bot Telegram
./scripts/start-browser.sh
hermes --profile worker-orchestrator gateway run
```

Lalu cukup kirim pesan ke bot Anda.

---

## Alur kerja

```
Telegram  ──►  orchestrator  ──►  lead  ──►  workers
  (Anda)         layer 1         layer 2      layer 3
                 │                │            │
                 │                │            └─ satu aksi, diverifikasi
                 │                └─ paham aturan SATU proyek
                 └─ parse task, screening, delegasi, lapor
```

Anda kirim teks seperti ini:

```
🔈 MemeBitcoin Airdrop
➖ Register  https://www.memebitcoin.org/register?r=vngqrra7
➖ Connect Twitter
➖ Complete Easy Task
➖ Submit Email Address
➖ Submit EVM Address
➖ Complete Daily Mission
```

Orchestrator mengekstrak nama proyek, URL, referral code, dan daftar task. Lalu
**membuka situsnya sendiri** — pengumuman Telegram cepat basi, situs yang
berwenang. Kalau proyeknya baru, discreening dulu sebelum ada yang dikerjakan.

---

## Kenapa ada 3 layer

Karena airdrop tidak bisa dipertukarkan. Dua contoh nyata:

| | MemeBitcoin | Elyon |
|---|---|---|
| Langkah | 6 | 3 |
| Butuh Twitter | ya | tidak |
| Butuh email | ya | tidak |
| Daily mission | **ada** | **tidak ada** |
| Selesai | berjalan mingguan | satu sore |

Keduanya berbagi kata "airdrop" dan hampir tidak ada yang lain. Layer 2
(`worker-lead`) ada supaya ada satu agent yang **paham aturan proyek itu
spesifik** — bukan menebak dari proyek lain.

`knowledge/airdrop-task-patterns.md` berisi tipe task atomik (register, connect
wallet, connect social, submit email, complete task, daily mission, on-chain)
beserta cara mengenali tiap-tiapnya dari pengumuman mentah.

| Layer | Profile | Model | Tugas |
|---|---|---|---|
| 1 | `worker-orchestrator` | kuat | Terima task, screening, delegasi, lapor |
| 2 | `worker-lead` | kuat | Punya satu proyek: format, aturan, urutan |
| 3 | `worker-analyzer` | kuat | Skor proyek 4 dimensi |
| 3 | `worker-daily` | hemat | Check-in harian |
| 3 | `worker-quests` | kuat | Onboarding + quest sequence |
| 3 | `worker-discord` | sedang | Baca komunitas, **draft** balasan |
| 3 | `worker-monitor` | sedang | Verifikasi, laporan, alert |

Tiap profile punya `SOUL.md` sendiri — itu system prompt-nya. (Hermes tidak
punya key `system_prompt`; identitas ada di `SOUL.md`.)

---

## Browser: Chrome asli via CDP

Airdrop itu ~100% GUI: connect wallet, klik claim, approve, sign, baca quest
board. Tidak ada CLI untuk semua itu. Jadi browser-nya adalah produknya.

Chrome jalan **di mesin Anda dengan window sungguhan**. Tanpa Docker, tanpa
`--no-sandbox`, tanpa VNC.

```bash
./scripts/start-browser.sh
```

Script itu membuka Chrome dengan remote debugging di `:9222`, lalu **memeriksa
port-nya benar-benar terbuka**. Ini bukan formalitas:

> Chrome 136 and later **silently refuse** to open the remote debugging port
> when `--remote-debugging-port` is combined with the *default* user-data-dir…
> The browser launches normally but nothing ever listens on 9222.
> **There is no error message.**
> — dokumentasi browser Hermes

Jadi "Chrome-nya kelihatan kebuka" tidak membuktikan apa pun. Script memaksa
`--user-data-dir` khusus dan memverifikasi lewat HTTP ke `/json/version`.

Login sekali di window itu — sesinya tersimpan di profil, jadi tidak perlu
diulang.

```bash
haa browser check            # audit config + probe CDP
haa browser check --offline  # audit config saja
```

```
browser readiness
  main                 browser · http://127.0.0.1:9222 · visible · engine=chrome
  worker-orchestrator  browser · http://127.0.0.1:9222 · visible · engine=chrome
  worker-lead          browser · http://127.0.0.1:9222 · visible · engine=chrome
  worker-analyzer      browser · http://127.0.0.1:9222 · visible · engine=chrome
  worker-daily         browser · http://127.0.0.1:9222 · visible · engine=chrome
  worker-discord       browser · http://127.0.0.1:9222 · visible · engine=chrome
  worker-monitor       browser · http://127.0.0.1:9222 · visible · engine=chrome
  worker-quests        browser · http://127.0.0.1:9222 · visible · engine=chrome
```

Tanpa `browser` di toolsets, tanpa `cdp_url`, atau dengan `headed: false` →
**error**, bukan warning. Window yang terlihat adalah satu-satunya cara Anda
mengambil alih saat agent berhenti di CAPTCHA.

> `/browser connect` **tidak** dipakai. Itu slash command khusus CLI
> interaktif dan tidak di-dispatch gateway — dari Telegram tidak akan jalan.
> Karena itu `browser.cdp_url` di `config.yaml`.

---

## Install

`install.sh` adalah **system installer**, bukan sekadar pengecek. Dia
memasang, bukan menyuruh Anda memasang.

| Langkah | Yang dilakukan |
|---|---|
| 1 | Paket sistem — deteksi apt/dnf/yum/pacman/zypper/brew, pasang git, curl, xz, ripgrep |
| 2 | Python 3.10+ (install kalau belum ada) |
| 3 | Node.js (install kalau belum ada) |
| 4 | Chromium-family browser |
| 5 | Hermes Agent framework |
| 6 | Control plane `haa` (venv + symlink) |
| 7 | config + profiles + `SOUL.md` → `~/.hermes/` |
| 8 | skills → `~/.hermes/skills/` |
| 9 | memory + knowledge base |
| 10 | `.env` + Telegram gateway + cron + verifikasi |

```bash
./install.sh --dry-run    # cetak semua langkah, tidak mengubah apa pun
./install.sh
```

Prasyarat: hanya `git` (dan `curl` + `xz-utils` di Linux). Sisanya diurus
installer.

Idempotent — dijalankan ulang memperbaiki instalasi yang gagal separuh tanpa
merusak state. `.env` dan `config.yaml` yang sudah ada **tidak pernah**
ditimpa; sebagai gantinya ditulis file `.new` untuk dibandingkan.

| Flag | Efek |
|---|---|
| `--dry-run` | cetak semua langkah, ubah tidak ada |
| `--skip-chrome` | lewati instalasi browser |
| `--skip-hermes` | pakai Hermes yang sudah ada |
| `--no-gateway` | lewati setup Telegram |
| `--no-cron` | jangan jadwalkan job |

---

## Jadwal

Dipasang lewat **cron Hermes**, bukan crontab sistem. Hanya cron Hermes yang
menegakkan `approvals.cron_mode: deny` — crontab sistem tidak bisa.

| Waktu | Job | Layer |
|---|---|---|
| 08:30 harian | `airdrop-orchestrator` — review state, flag yang butuh keputusan | 1 |
| 09:00 harian | `airdrop-daily` — jalankan aksi harian tiap proyek | 2 |
| 13:00 harian | `airdrop-verify` — verifikasi + cek hash bukti | 3 |
| 20:00 Minggu | `airdrop-weekly` — laporan mingguan | 3 |
| 11:00 Senin | `airdrop-discord` — scan komunitas | 3 |

Orchestrator jalan **sebelum** worker dengan sengaja: dialah yang memutuskan
apakah pekerjaan hari ini layak dikerjakan.

Setiap job browser dimulai dengan preflight `haa browser check`. Chrome jalan
di host, jadi kalau window-nya ditutup job berhenti segera dan memberi tahu —
bukan menghabiskan sejam untuk menemukan semua klik gagal.

```bash
hermes cron list
hermes cron run <job_id>
hermes cron pause <job_id>
```

---

## Otonomi: agent yang menentukan, bukan skrip

Task airdrop itu dinamis, UI-nya dinamis, dan tiap proyek beda. Jadi tidak ada
satu pun selector, XPath, koordinat, atau urutan klik di seluruh proyek ini —
dan ada test yang melarangnya muncul.

```
querySelector / getElementById    → dilarang
XPath (//button, /html/body)      → dilarang
[name=..] / [id=..] / [class=..]  → dilarang
"klik tombol kedua"               → dilarang
klik koordinat (340, 512)         → dilarang
```

Yang agent dapat adalah **tujuan** ("selesaikan daily mission di Loqua") dan
sebuah browser. Caranya dia putuskan sendiri, dibaca ulang dari halaman hidup
setiap kali.

Mekanismenya `browser_snapshot`: mengembalikan *accessibility tree* halaman
beserta ref ID (`@e1`, `@e7`) untuk tiap elemen interaktif. **Ref dibuat ulang
tiap snapshot** — bukan selector yang disimpan. Jadi UI yang di-redesign tidak
merusak apa pun.

| Alat | Untuk apa |
|---|---|
| `browser_snapshot` | Default. Cari elemen lewat tree, bukan menebak |
| `browser_vision` | Kalau tree ambigu — sederet tombol seragam, ikon tanpa label, widget canvas |
| `browser_get_images` | Kalau aksinya bergantung gambar |
| `browser_scroll` / `browser_press` / `browser_type` | Interaksi fisik |

Pembagian kerja antar layer:

- **Lead** mencatat *apa* yang proyek minta (dari task list situs itu sendiri)
- **Worker** memutuskan *bagaimana* — elemen mana, tab mana, klik mana

Begitu lead menulis selector ke dalam catatan kampanye, dia sudah membangun
hal rapuh yang desain ini hindari: seminggu lagi salah, di proyek berikutnya
juga salah, dan gagalnya terlihat seperti worker-nya bodoh padahal
instruksinya yang basi.

**Kalau ada proyek yang butuh lebih:** set `browser.backend: "browser-use"` di
config. Agent lalu menulis Python untuk mengendalikan halaman — lebih ekspresif
untuk alur tidak biasa (drag, tunggu network idle, iterasi N baris), tapi itu
eksekusi kode arbitrer di host dan langkahnya tidak lagi ter-log satu per satu.
Dimatikan secara default dengan sengaja.

## Filter proyek

Dua belas rating **0–3**, dari checklist "Sniper" di HTX Insights' *"The Last
Time I'll Talk About Backpack…"* (2026-03-23):

- **Team** — insight, eksekusi, integritas. Ketiganya wajib; satu `0` menolkan dimensi
- **Product** — PMF, kualitas delivery, tanggung jawab. Bobot tertinggi
- **Narrative** — naratif Web3, keselarasan tren Web2, premium
- **Timing** — FOMO, biaya, crowding. **Terbalik**: 0 itu bagus

```bash
haa analyze --project "Foo" --url https://foo.xyz \
  --team-insight 3 --team-execution 3 --team-integrity 3 \
  --product-pmf 3 --product-delivery 3 --product-responsibility 3 \
  --narrative-web3 3 --narrative-web2 2 --narrative-premium 2 \
  --timing-fomo 1 --timing-cost 1 --timing-crowding 1 --save-to
```

Veto keras memaksa `SKIP` dan membatasi skor di 4.0, supaya laporan tidak
pernah terbaca "9/10 tapi di-skip": delivery tidak bisa dipakai, semua orang
sudah farming, operator ragu, atau biaya tinggi saat puncak FOMO.

Rating `1` itu jujur — artinya "sudah dilihat, tidak bisa dikonfirmasi". Cukup
banyak `1` menurunkan confidence di bawah 0.70, yang mengarahkan keputusan ke
manusia.

Scoring-nya kode, bukan LLM. Dua kali jalan dengan rating sama memberi verdict
sama selamanya, jadi keputusan bisa diaudit berbulan-bulan kemudian.

---

## Guardrails

| Kondisi | Perilaku |
|---|---|
| CAPTCHA / Cloudflare challenge | Berhenti. **Tidak pernah** diselesaikan |
| MFA / one-time code | Berhenti. Operator yang menyelesaikan |
| Wallet signature / approval prompt | Berhenti. Signing keputusan manusia |
| Sesi expired | Berhenti. Tidak re-auth sendiri |
| Private key / mnemonic / keystore terdeteksi | Ditolak — di `.env`, di ledger, di `wallets add` |
| Aksi spend (`bridge`, `swap`, `approve`, `transfer`, …) | Selalu butuh approval; **tidak bisa** di-pre-approve dari config |
| Di atas `HAA_MAX_SPEND_USD` | Berhenti |
| Tool gagal identik berulang | `tool_loop_guardrails` Hermes menghentikan paksa |

Aturan terpenting, ada di `daily-executor`: **jangan pernah log `ok` untuk aksi
yang tidak diverifikasi.** Operasi yang mencatat keberhasilan yang tidak
dikonfirmasi lebih buruk daripada yang tidak melakukan apa-apa, karena operator
terus percaya sistemnya jalan.

Bukti dinilai berjenjang (`knowledge/verification-rules.md`): hash on-chain dan
state yang bertahan setelah reload itu kuat; toast yang hilang dalam 3 detik
itu lemah; "tidak ada error" **bukan** bukti.

---

## Data

```
data/
├── campaigns/<slug>/
│   ├── info.json          # kampanye + verdict analyzer
│   ├── progress.json      # tally + log aksi append-only
│   └── screenshots/
├── logs/evidence.jsonl    # audit trail ber-hash
└── wallets.json           # alamat saja, mode 0600
```

JSON polos, tulis atomik. Di-git-ignore — ini audit trail Anda, backup sendiri.

```bash
haa plan                     # apa yang jatuh tempo hari ini
haa report --days 7          # rollup mingguan
haa evidence tail -n 20
haa evidence verify          # hash ulang semua bukti
```

`haa evidence verify` menghitung ulang hash tiap screenshot. Mismatch berarti
bukti berubah setelah dicatat — itu yang memimpin laporan, karena ledger adalah
satu-satunya cara membedakan "saya melakukan ini" dari "saya rasa saya
melakukan ini".

---

## Batas scope

**Yang tidak dilakukan sistem ini: membantu Anda menyajikan banyak wallet
sebagai banyak orang.**

Tidak ada fingerprint spoofing, tidak ada rotasi proxy per-wallet, tidak ada
timing jitter untuk mengalahkan clustering. Ketiganya ada untuk satu tujuan:
membuat wallet satu operator terlihat seperti beberapa orang asing supaya
sistem deteksi fraud mengalokasikan reward berkali-kali. Protokol yang
mendeteksi itu bukan rusak — dia bekerja.

Ini konsekuensi langsung dari browser-nya: **satu Chrome asli dengan satu
profil asli**. Itu memang persis seperti satu partisipan sungguhan.

Juga di luar scope: auto-posting Discord (melanggar ToS mereka dan
membahayakan akun yang kampanye Anda butuhkan — agent men-draft, Anda yang
kirim), dan menyelesaikan CAPTCHA.

Yang **masuk**: wallet tiering (`main` / `farming` / `high-risk`) sebagai
manajemen risiko biasa — layak dilakukan walau Anda cuma punya satu wallet.
Wallet `main` tidak pernah dipakai farming; ditegakkan di kode, bukan imbauan.

---

## Verifikasi

```bash
make test      # 620 test
make lint
./install.sh --dry-run
haa browser check --offline
haa doctor --offline
```

Test-nya menjalankan kode sungguhan: mengeksekusi `install.sh --dry-run` dan
memastikan tidak ada file berubah, mem-parse tiap YAML lewat validator,
memanggil `main()` end-to-end, dan memastikan audit **menolak** profile tanpa
browser / tanpa `cdp_url` / dengan `headed: false`.

Satu test memastikan tidak ada test run yang membuat file di repo — ditambahkan
setelah `haa init` ketahuan menulis `.env` ke working tree.

## Dokumentasi riset

- `docs/research/hermes-schema.md` — asal-usul skema config + key yang tidak ada
- `docs/research/browser.md` — temuan browser (sebagian masih menyebut setup Camofox lama)
- `docs/research/sources.md` — sumber terverifikasi, termasuk 2 URL yang 404
- `AGENTS.md` — memory proyek: keputusan terkunci, progress, hal yang jangan diulang

## Yang belum selesai

- `README` bagian riset `docs/research/browser.md` masih mendeskripsikan setup
  Camofox/VNC yang sudah tidak dipakai
- Alur Telegram belum diuji terhadap bot sungguhan (butuh `TELEGRAM_BOT_TOKEN`)

## Lisensi

MIT
