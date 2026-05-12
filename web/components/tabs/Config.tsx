'use client'
import { useState, useEffect } from 'react'
import { ChevronDown, Save, RotateCcw, Info } from 'lucide-react'
import { ModeBadge } from '@/components/ui'

type FieldDef = {
  key: string; label: string; desc: string; hint?: string
  type: 'number' | 'select'
  options?: string[]; unit?: string; min?: number; max?: number; step?: number
}

type Section = { title: string; icon: string; desc: string; fields: FieldDef[] }

const SECTIONS: Section[] = [
  {
    title: 'Mode & Bankroll', icon: '🛡️',
    desc: 'Basic trading mode and capital allocation',
    fields: [
      { key: 'AGENT_MODE', label: 'Agent Mode', desc: 'demo = simulasi harga real tanpa transaksi. live = eksekusi order nyata ke Polymarket.', hint: 'Mulai dengan demo untuk collect data 300 trade dulu', type: 'select', options: ['demo', 'live'] },
      { key: 'DEMO_BANKROLL', label: 'Demo Bankroll', desc: 'Modal virtual untuk demo. Gunakan nilai besar ($500+) untuk data collection.', type: 'number', min: 10, max: 10000, step: 10, unit: 'USD' },
      { key: 'LIVE_BANKROLL', label: 'Live Bankroll Fallback', desc: 'Fallback jika CLOB API gagal baca balance. Set 0 agar agent tidak bet jika balance tidak terbaca.', type: 'number', min: 0, max: 10000, step: 1, unit: 'USD' },
    ],
  },
  {
    title: 'Bet Sizing', icon: '💰',
    desc: 'Position sizing and risk management per trade',
    fields: [
      { key: 'MIN_BET_SIZE', label: 'Min Bet', desc: 'Ukuran bet minimum. Terlalu kecil = profit tidak cover biaya LLM.', type: 'number', min: 0.5, max: 100, step: 0.5, unit: 'USD' },
      { key: 'MAX_BET_SIZE', label: 'Max Bet', desc: 'Ukuran bet maksimum. Kelly formula akan size di bawah ini. Rekomendasi: 1-2% bankroll.', type: 'number', min: 1, max: 500, step: 0.5, unit: 'USD' },
      { key: 'KELLY_FRACTION', label: 'Kelly Fraction', desc: '0.25 = quarter Kelly (konservatif). Jangan di atas 0.5 — risiko ruin tinggi.', hint: '0.25 direkomendasikan untuk pemula', type: 'number', min: 0.05, max: 0.5, step: 0.05 },
      { key: 'MAX_OPEN_POSITIONS', label: 'Max Open Positions', desc: 'Maksimum trade terbuka bersamaan. Lebih banyak = lebih banyak data tapi butuh bankroll lebih besar.', type: 'number', min: 1, max: 50, step: 1 },
      { key: 'MAX_OPEN_PER_CATEGORY', label: 'Max Per Category', desc: 'Batas posisi per kategori (sports/crypto/geo). Mencegah over-exposure ke satu kategori.', type: 'number', min: 1, max: 20, step: 1 },
    ],
  },
  {
    title: 'Edge & Signal Gate', icon: '📊',
    desc: 'Threshold kapan agent boleh masuk market',
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
    title: 'Exit Strategy', icon: '🚪',
    desc: 'Kapan ambil profit atau cut loss',
    fields: [
      { key: 'EXIT_TAKE_PROFIT', label: 'Take Profit Floor', desc: 'TP minimum sebagai % return. TP aktual bisa lebih tinggi (dinamis berdasarkan edge awal).', type: 'number', min: 0.05, max: 1.0, step: 0.05, unit: '%' },
      { key: 'EXIT_STOP_LOSS', label: 'Stop Loss', desc: 'Exit saat rugi mencapai % ini. Untuk sports: tidak berlaku, tunggu resolved.', type: 'number', min: 0.05, max: 0.50, step: 0.01, unit: '%' },
      { key: 'TRAILING_STOP_PCT', label: 'Trailing Stop', desc: 'Exit jika profit turun % ini dari peak. Aktif hanya jika peak ≥ 10%.', type: 'number', min: 0.02, max: 0.20, step: 0.01, unit: '%' },
      { key: 'EXIT_MAX_HOURS', label: 'Max Hold (Non-Sports)', desc: 'Maksimum jam hold untuk crypto/geo/other. Sports tunggu resolved.', type: 'number', min: 1, max: 168, step: 1, unit: 'jam' },
    ],
  },
  {
    title: 'Scan & Market Filter', icon: '🔍',
    desc: 'Filter market mana yang di-scan agent',
    fields: [
      { key: 'SCAN_INTERVAL_ACTIVE_MINUTES', label: 'Scan Active Hours', desc: 'Interval scan 14:00-22:00 UTC. 3 = scan setiap 3 menit.', type: 'number', min: 1, max: 30, step: 1, unit: 'menit' },
      { key: 'SCAN_INTERVAL_MINUTES', label: 'Scan Off-Peak', desc: 'Interval scan di luar jam aktif.', type: 'number', min: 5, max: 60, step: 5, unit: 'menit' },
      { key: 'MIN_VOLUME_24H', label: 'Min Volume 24h', desc: 'Market dengan volume rendah = spread lebar, sulit exit.', type: 'number', min: 100, max: 100000, step: 100, unit: 'USD' },
      { key: 'MIN_LIQUIDITY', label: 'Min Liquidity', desc: 'Likuiditas rendah = order besar bisa gerakkan harga (slippage).', type: 'number', min: 100, max: 50000, step: 100, unit: 'USD' },
      { key: 'MAX_DAYS_TO_RESOLVE', label: 'Max Days to Resolve', desc: 'Hanya trade market yang resolve dalam N hari.', type: 'number', min: 1, max: 90, step: 1, unit: 'hari' },
    ],
  },
  {
    title: 'AI & Cost Control', icon: '🤖',
    desc: 'Budget dan limit untuk AI analysis',
    fields: [
      { key: 'MAX_LLM_CALLS_PER_CYCLE', label: 'Max AI Analyses/Scan', desc: 'Maksimum market yang dianalisis AI per scan. Lebih banyak = lebih mahal.', type: 'number', min: 1, max: 20, step: 1 },
      { key: 'LLM_DAILY_COST_LIMIT_USD', label: 'Daily AI Budget', desc: 'Batas biaya AI per hari. Agent berhenti analisis jika sudah mencapai limit.', type: 'number', min: 0.5, max: 20, step: 0.5, unit: 'USD' },
      { key: 'LLM_MAX_TOKENS', label: 'Max Tokens/Call', desc: 'Maksimum token output per panggilan AI. 1500 cukup untuk analisis market.', type: 'number', min: 500, max: 4000, step: 100 },
    ],
  },
  {
    title: 'Bankroll Compounding', icon: '📈',
    desc: 'Auto-scale bet size berdasarkan win/loss streak',
    fields: [
      { key: 'WIN_STREAK_TO_INCREASE', label: 'Wins to Level Up', desc: 'Berapa win berturut-turut sebelum Kelly multiplier naik satu level.', type: 'number', min: 1, max: 10, step: 1 },
      { key: 'LOSS_STREAK_TO_DECREASE', label: 'Losses to Level Down', desc: 'Berapa loss berturut-turut sebelum Kelly multiplier turun satu level.', type: 'number', min: 1, max: 10, step: 1 },
      { key: 'BANKROLL_STEP_SIZE', label: 'Step Size per Level', desc: '0.10 = naik/turun 10% per level. Level +2 = Kelly × 1.20.', type: 'number', min: 0.05, max: 0.30, step: 0.05, unit: '%' },
      { key: 'MAX_BANKROLL_LEVEL', label: 'Max Level', desc: 'Level maksimum compounding. Level 5 dengan step 10% = Kelly × 1.50.', type: 'number', min: 1, max: 10, step: 1 },
    ],
  },
]

const ALLOWED = new Set(SECTIONS.flatMap(s => s.fields.map(f => f.key)))

function Field({ def, value, onChange }: { def: FieldDef; value: string; onChange: (k: string, v: string) => void }) {
  return (
    <div className="flex flex-col gap-1.5">
      <div className="flex items-center gap-2">
        <span className="text-xs font-semibold" style={{ color: 'var(--text2)' }}>{def.label}</span>
        {def.unit && <span className="text-[10px] px-1.5 py-0.5 rounded-md" style={{ color: 'var(--dim)', background: 'var(--border2)' }}>{def.unit}</span>}
      </div>
      <p className="text-[11px] leading-relaxed" style={{ color: 'var(--dim)' }}>{def.desc}</p>
      {def.hint && (
        <div className="flex items-start gap-1.5 text-[10px] p-2 rounded-lg" style={{ background: 'var(--accent-bg)', color: 'var(--accent-light)' }}>
          <Info size={12} className="flex-shrink-0 mt-0.5" />
          <span>{def.hint}</span>
        </div>
      )}
      {def.type === 'select' ? (
        <select value={value} onChange={e => onChange(def.key, e.target.value)} className="input">
          {def.options?.map(o => <option key={o} value={o}>{o}</option>)}
        </select>
      ) : (
        <input type="number" value={value} min={def.min} max={def.max} step={def.step}
          onChange={e => onChange(def.key, e.target.value)}
          className="input mono" />
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
    <div className="flex flex-col gap-3 fade-in">
      <div className="flex items-start justify-between">
        <div>
          <div className="text-base font-bold" style={{ color: 'var(--text)' }}>Configuration</div>
          <div className="text-xs mt-0.5" style={{ color: 'var(--dim)' }}>Berlaku untuk Demo & Live · Restart otomatis setelah save</div>
        </div>
        <ModeBadge mode={(env.AGENT_MODE as 'live' | 'demo') || 'demo'} />
      </div>

      {status && (
        <div className="flex items-center gap-2 p-3 rounded-xl text-xs font-medium" style={{
          background: status.ok ? 'var(--green-bg)' : 'var(--red-bg)',
          border: `1px solid ${status.ok ? 'var(--green-border)' : 'var(--red-border)'}`,
          color: status.ok ? 'var(--green)' : 'var(--red)',
        }}>
          {status.ok ? '✓' : '✕'} {status.msg}
        </div>
      )}

      {SECTIONS.map(section => {
        const isOpen = expanded === section.title
        return (
          <div key={section.title} className="section-card">
            <button onClick={() => setExpanded(isOpen ? null : section.title)}
              className="w-full flex items-center gap-3 p-4 text-left" style={{ background: 'transparent', border: 'none', cursor: 'pointer' }}>
              <span className="text-base flex-shrink-0">{section.icon}</span>
              <div className="flex-1 min-w-0">
                <div className="text-sm font-semibold" style={{ color: 'var(--text2)' }}>{section.title}</div>
                <div className="text-[10px] mt-0.5" style={{ color: 'var(--dim)' }}>{section.desc}</div>
              </div>
              <ChevronDown size={16} style={{ color: 'var(--dim)', transform: isOpen ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }} />
            </button>

            {isOpen && (
              <div className="px-4 pb-4" style={{ borderTop: '1px solid var(--border2)' }}>
                <div className="flex flex-col gap-4 pt-4">
                  {section.fields.map(f => (
                    <Field key={f.key} def={f} value={env[f.key] ?? ''} onChange={set} />
                  ))}
                </div>
                <button onClick={() => save(section.fields.map(f => f.key))} disabled={saving}
                  className="btn btn-primary mt-4 w-full">
                  <Save size={14} />
                  {saving ? 'Saving...' : 'Save & Restart Agent'}
                </button>
              </div>
            )}
          </div>
        )
      })}

      {/* Reset to defaults */}
      <div className="text-center py-2">
        <button onClick={async () => {
          if (!confirm('Reset all config to defaults? This will restart the agent.')) return
          setSaving(true)
          const res = await fetch('/api/settings', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ _reset: true }) })
          const data = await res.json()
          setSaving(false)
          if (data.ok) {
            const fresh = await fetch('/api/settings').then(r => r.json())
            setEnv(fresh)
            setStatus({ ok: true, msg: 'Reset to defaults' })
          } else {
            setStatus({ ok: false, msg: data.error || 'Reset failed' })
          }
          setTimeout(() => setStatus(null), 3000)
        }} className="btn btn-ghost btn-sm text-xs">
          <RotateCcw size={12} /> Reset to defaults
        </button>
      </div>
    </div>
  )
}
