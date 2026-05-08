'use client'
import { useState, useEffect } from 'react'

type FieldDef = {
  key: string; label: string; desc: string
  type: 'number' | 'select'
  options?: string[]; unit?: string; min?: number; max?: number; step?: number
}

type Section = { title: string; icon: string; fields: FieldDef[] }

const SECTIONS: Section[] = [
  {
    title: 'Mode & Bankroll', icon: 'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z',
    fields: [
      { key: 'AGENT_MODE', label: 'Agent Mode', desc: 'demo = simulasi harga real tanpa transaksi. live = eksekusi order nyata ke Polymarket.', type: 'select', options: ['demo', 'live'] },
      { key: 'DEMO_BANKROLL', label: 'Demo Bankroll', desc: 'Modal virtual untuk demo. Gunakan nilai besar ($500+) untuk data collection 300 trade.', type: 'number', min: 10, max: 10000, step: 10, unit: 'USD' },
      { key: 'LIVE_BANKROLL', label: 'Live Bankroll Fallback', desc: 'Fallback jika CLOB API gagal baca balance. Set 0 agar agent tidak bet jika balance tidak terbaca.', type: 'number', min: 0, max: 10000, step: 1, unit: 'USD' },
    ],
  },
  {
    title: 'Bet Sizing', icon: 'M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6',
    fields: [
      { key: 'MIN_BET_SIZE', label: 'Min Bet', desc: 'Ukuran bet minimum. Terlalu kecil = profit tidak cover biaya LLM.', type: 'number', min: 0.5, max: 100, step: 0.5, unit: 'USD' },
      { key: 'MAX_BET_SIZE', label: 'Max Bet', desc: 'Ukuran bet maksimum. Kelly formula akan size di bawah ini. Rekomendasi: 1-2% bankroll.', type: 'number', min: 1, max: 500, step: 0.5, unit: 'USD' },
      { key: 'KELLY_FRACTION', label: 'Kelly Fraction', desc: '0.25 = quarter Kelly (konservatif). Jangan di atas 0.5 — risiko ruin tinggi.', type: 'number', min: 0.05, max: 0.5, step: 0.05 },
      { key: 'MAX_OPEN_POSITIONS', label: 'Max Open Positions', desc: 'Maksimum trade terbuka bersamaan. Lebih banyak = lebih banyak data tapi butuh bankroll lebih besar.', type: 'number', min: 1, max: 50, step: 1 },
      { key: 'MAX_OPEN_PER_CATEGORY', label: 'Max Per Category', desc: 'Batas posisi per kategori (sports/crypto/geo). Mencegah over-exposure ke satu kategori.', type: 'number', min: 1, max: 20, step: 1 },
    ],
  },
  {
    title: 'Edge & Signal Gate', icon: 'M22 7L13.5 15.5 8.5 10.5 2 17M16 7h6v6',
    fields: [
      { key: 'MIN_STAT_EDGE', label: 'Min Statistical Edge', desc: 'Gap minimum antara p_base (model) dan harga pasar. 0.08 = butuh gap 8%.', type: 'number', min: 0.03, max: 0.30, step: 0.01, unit: '%' },
      { key: 'MIN_STAT_EDGE_HIGH_RISK', label: 'Min Edge (High Risk)', desc: 'Edge minimum untuk crypto, geopolitik, politics. Lebih tinggi karena volatilitas besar.', type: 'number', min: 0.05, max: 0.40, step: 0.01, unit: '%' },
      { key: 'MIN_CONFIDENCE', label: 'Min Confidence', desc: 'Confidence minimum dari AI. 0.65 = AI harus 65% yakin harga akan bergerak ke arah prediksi.', type: 'number', min: 0.50, max: 0.95, step: 0.01, unit: '%' },
      { key: 'MIN_CONFIDENCE_CRYPTO', label: 'Min Confidence (Crypto)', desc: 'Override untuk market crypto. Lebih tinggi karena sangat volatile.', type: 'number', min: 0.50, max: 0.95, step: 0.01, unit: '%' },
      { key: 'MIN_CONFIDENCE_GEOPOLITIK', label: 'Min Confidence (Geo)', desc: 'Override untuk market geopolitik.', type: 'number', min: 0.50, max: 0.95, step: 0.01, unit: '%' },
      { key: 'EDGE_THRESHOLD', label: 'Edge Threshold', desc: 'Gap minimum antara p_true (AI) dan harga pasar sebelum bet.', type: 'number', min: 0.02, max: 0.20, step: 0.01, unit: '%' },
    ],
  },
  {
    title: 'Exit Strategy', icon: 'M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9',
    fields: [
      { key: 'EXIT_TAKE_PROFIT', label: 'Take Profit Floor', desc: 'TP minimum sebagai % return. TP aktual bisa lebih tinggi (dinamis berdasarkan edge awal).', type: 'number', min: 0.05, max: 1.0, step: 0.05, unit: '%' },
      { key: 'EXIT_STOP_LOSS', label: 'Stop Loss', desc: 'Exit saat rugi mencapai % ini. Untuk sports: tidak berlaku, tunggu resolved.', type: 'number', min: 0.05, max: 0.50, step: 0.01, unit: '%' },
      { key: 'TRAILING_STOP_PCT', label: 'Trailing Stop', desc: 'Exit jika profit turun % ini dari peak. Aktif hanya jika peak ≥ 10%.', type: 'number', min: 0.02, max: 0.20, step: 0.01, unit: '%' },
      { key: 'EXIT_MAX_HOURS', label: 'Max Hold (Non-Sports)', desc: 'Maksimum jam hold untuk crypto/geo/other. Sports tunggu resolved.', type: 'number', min: 1, max: 168, step: 1, unit: 'jam' },
      { key: 'MIN_HOLD_MINUTES', label: 'Min Hold', desc: 'Jangan exit dalam N menit pertama. Beri waktu harga bergerak.', type: 'number', min: 5, max: 120, step: 5, unit: 'menit' },
    ],
  },
  {
    title: 'Scan & Market Filter', icon: 'M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM21 21l-4.35-4.35',
    fields: [
      { key: 'SCAN_INTERVAL_ACTIVE_MINUTES', label: 'Scan Active Hours', desc: 'Interval scan 14:00-22:00 UTC. 3 = scan setiap 3 menit.', type: 'number', min: 1, max: 30, step: 1, unit: 'menit' },
      { key: 'SCAN_INTERVAL_MINUTES', label: 'Scan Off-Peak', desc: 'Interval scan di luar jam aktif.', type: 'number', min: 5, max: 60, step: 5, unit: 'menit' },
      { key: 'MIN_VOLUME_24H', label: 'Min Volume 24h', desc: 'Market dengan volume rendah = spread lebar, sulit exit.', type: 'number', min: 100, max: 100000, step: 100, unit: 'USD' },
      { key: 'MIN_LIQUIDITY', label: 'Min Liquidity', desc: 'Likuiditas rendah = order besar bisa gerakkan harga (slippage).', type: 'number', min: 100, max: 50000, step: 100, unit: 'USD' },
      { key: 'MAX_DAYS_TO_RESOLVE', label: 'Max Days to Resolve', desc: 'Hanya trade market yang resolve dalam N hari.', type: 'number', min: 1, max: 90, step: 1, unit: 'hari' },
    ],
  },
  {
    title: 'AI & Cost Control', icon: 'M12 2a2 2 0 0 1 2 2c0 .74-.4 1.39-1 1.73V7h1a7 7 0 0 1 7 7h1a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v1a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-1H2a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1h1a7 7 0 0 1 7-7h1V5.73c-.6-.34-1-.99-1-1.73a2 2 0 0 1 2-2z',
    fields: [
      { key: 'MAX_LLM_CALLS_PER_CYCLE', label: 'Max AI Analyses/Scan', desc: 'Maksimum market yang dianalisis AI per scan. Lebih banyak = lebih mahal.', type: 'number', min: 1, max: 20, step: 1 },
      { key: 'LLM_DAILY_COST_LIMIT_USD', label: 'Daily AI Budget', desc: 'Batas biaya AI per hari. Agent berhenti analisis jika sudah mencapai limit.', type: 'number', min: 0.5, max: 20, step: 0.5, unit: 'USD' },
      { key: 'LLM_MAX_TOKENS', label: 'Max Tokens/Call', desc: 'Maksimum token output per panggilan AI. 1500 cukup untuk analisis market.', type: 'number', min: 500, max: 4000, step: 100 },
    ],
  },
  {
    title: 'Bankroll Compounding', icon: 'M18 20V10M12 20V4M6 20v-6',
    fields: [
      { key: 'WIN_STREAK_TO_INCREASE', label: 'Wins to Level Up', desc: 'Berapa win berturut-turut sebelum Kelly multiplier naik satu level.', type: 'number', min: 1, max: 10, step: 1 },
      { key: 'LOSS_STREAK_TO_DECREASE', label: 'Losses to Level Down', desc: 'Berapa loss berturut-turut sebelum Kelly multiplier turun satu level.', type: 'number', min: 1, max: 10, step: 1 },
      { key: 'BANKROLL_STEP_SIZE', label: 'Step Size per Level', desc: '0.10 = naik/turun 10% per level. Level +2 = Kelly × 1.20.', type: 'number', min: 0.05, max: 0.30, step: 0.05, unit: '%' },
      { key: 'MAX_BANKROLL_LEVEL', label: 'Max Level', desc: 'Level maksimum compounding. Level 5 dengan step 10% = Kelly × 1.50.', type: 'number', min: 1, max: 10, step: 1 },
    ],
  },
]

const ALLOWED = new Set(SECTIONS.flatMap(s => s.fields.map(f => f.key)))

function SvgIcon({ d, size = 16 }: { d: string; size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d={d} />
    </svg>
  )
}

function Field({ def, value, onChange }: { def: FieldDef; value: string; onChange: (k: string, v: string) => void }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
        <span style={{ fontSize: 12, fontWeight: 600, color: '#e2e8f0' }}>{def.label}</span>
        {def.unit && <span style={{ fontSize: 10, color: '#4b5563', background: '#1e1e3a', padding: '1px 6px', borderRadius: 6 }}>{def.unit}</span>}
      </div>
      <p style={{ fontSize: 11, color: '#6b7280', lineHeight: 1.5 }}>{def.desc}</p>
      {def.type === 'select' ? (
        <select value={value} onChange={e => onChange(def.key, e.target.value)}
          style={{ background: '#0d0d1a', border: '1px solid #2a2a4a', borderRadius: 10, padding: '10px 12px', fontSize: 13, color: '#e2e8f0', outline: 'none', cursor: 'pointer' }}>
          {def.options?.map(o => <option key={o} value={o}>{o}</option>)}
        </select>
      ) : (
        <input type="number" value={value} min={def.min} max={def.max} step={def.step}
          onChange={e => onChange(def.key, e.target.value)}
          style={{ background: '#0d0d1a', border: '1px solid #2a2a4a', borderRadius: 10, padding: '10px 12px', fontSize: 13, color: '#e2e8f0', outline: 'none', fontFamily: 'ui-monospace, monospace' }} />
      )}
    </div>
  )
}

export function Config() {
  const [env, setEnv] = useState<Record<string, string>>({})
  const [status, setStatus] = useState<{ ok: boolean; msg: string } | null>(null)
  const [saving, setSaving] = useState(false)
  const [expanded, setExpanded] = useState<string | null>('Mode & Bankroll')

  useEffect(() => { fetch('/api/settings').then(r => r.json()).then(setEnv) }, [])

  const set = (k: string, v: string) => setEnv(prev => ({ ...prev, [k]: v }))

  const save = async (keys: string[]) => {
    setSaving(true)
    const updates = Object.fromEntries(keys.filter(k => ALLOWED.has(k)).map(k => [k, env[k] ?? '']))
    const res = await fetch('/api/settings', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(updates) })
    const data = await res.json()
    setSaving(false)
    setStatus({ ok: data.ok, msg: data.ok ? `Saved: ${data.updated?.join(', ')}` : data.error })
    setTimeout(() => setStatus(null), 3000)
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      <div>
        <div style={{ fontSize: 15, fontWeight: 700, color: '#e2e8f0' }}>Configuration</div>
        <div style={{ fontSize: 11, color: '#6b7280', marginTop: 2 }}>Berlaku untuk Demo & Live · Restart otomatis setelah save</div>
      </div>

      {status && (
        <div style={{
          display: 'flex', alignItems: 'center', gap: 8, padding: '10px 14px', borderRadius: 12, fontSize: 12,
          background: status.ok ? 'rgba(34,197,94,0.1)' : 'rgba(239,68,68,0.1)',
          border: `1px solid ${status.ok ? 'rgba(34,197,94,0.3)' : 'rgba(239,68,68,0.3)'}`,
          color: status.ok ? '#22c55e' : '#ef4444',
        }}>
          {status.ok ? '✓' : '✕'} {status.msg}
        </div>
      )}

      {SECTIONS.map(section => {
        const isOpen = expanded === section.title
        return (
          <div key={section.title} style={{ background: '#13132a', border: '1px solid #2a2a4a', borderRadius: 16, overflow: 'hidden' }}>
            <button onClick={() => setExpanded(isOpen ? null : section.title)}
              style={{ width: '100%', display: 'flex', alignItems: 'center', gap: 10, padding: '14px 16px', background: 'transparent', border: 'none', cursor: 'pointer', textAlign: 'left' }}>
              <span style={{ color: '#a5b4fc', flexShrink: 0, display: 'flex' }}>
                <SvgIcon d={section.icon} />
              </span>
              <span style={{ fontSize: 13, fontWeight: 600, color: '#e2e8f0', flex: 1 }}>{section.title}</span>
              <span style={{ color: '#6b7280', display: 'flex', transform: isOpen ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }}>
                <SvgIcon d="M6 9l6 6 6-6" />
              </span>
            </button>

            {isOpen && (
              <div style={{ padding: '0 16px 16px', borderTop: '1px solid #1e1e3a' }}>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: 16, paddingTop: 16 }}>
                  {section.fields.map(f => (
                    <Field key={f.key} def={f} value={env[f.key] ?? ''} onChange={set} />
                  ))}
                </div>
                <button onClick={() => save(section.fields.map(f => f.key))} disabled={saving}
                  style={{
                    marginTop: 16, display: 'flex', alignItems: 'center', gap: 8,
                    padding: '11px 18px', borderRadius: 12, border: 'none', cursor: 'pointer',
                    background: saving ? '#1e1e3a' : 'linear-gradient(135deg,#4f46e5,#6366f1)',
                    color: saving ? '#6b7280' : 'white', fontSize: 13, fontWeight: 600, transition: 'all 0.15s',
                  }}>
                  <SvgIcon d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2zM17 21v-8H7v8M7 3v5h8" size={14} />
                  {saving ? 'Saving...' : 'Save & Restart Agent'}
                </button>
              </div>
            )}
          </div>
        )
      })}
    </div>
  )
}
