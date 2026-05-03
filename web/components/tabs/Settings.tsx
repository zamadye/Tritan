'use client'
import { useState, useEffect } from 'react'
import { Card } from '@/components/ui'

function Field({ label, envKey, value, onChange }: { label: string; envKey: string; value: string; onChange: (k: string, v: string) => void }) {
  return (
    <div>
      <label className="text-[10px] text-[#6b7280] uppercase tracking-widest block mb-1">{label}</label>
      <input value={value} onChange={e => onChange(envKey, e.target.value)}
        className="w-full bg-[#0d0d1a] border border-[#2a2a4a] rounded-lg px-3 py-2 text-xs text-[#e2e8f0] focus:border-[#6366f1] outline-none" />
    </div>
  )
}

function SaveBtn({ onClick, label = 'Save & Restart' }: { onClick: () => void; label?: string }) {
  return (
    <button onClick={onClick} className="bg-[#4f46e5] hover:bg-[#4338ca] text-white text-xs px-4 py-2 rounded-lg transition-colors font-medium">
      💾 {label}
    </button>
  )
}

export function Settings() {
  const [env, setEnv] = useState<Record<string, string>>({})
  const [saved, setSaved] = useState(false)

  useEffect(() => { fetch('/api/settings').then(r => r.json()).then(setEnv) }, [])

  const set = (k: string, v: string) => setEnv(prev => ({ ...prev, [k]: v }))

  const save = async (keys: string[]) => {
    const updates = Object.fromEntries(keys.map(k => [k, env[k] || '']))
    await fetch('/api/settings', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(updates) })
    setSaved(true); setTimeout(() => setSaved(false), 2000)
  }

  return (
    <div className="space-y-5 max-w-2xl">
      <h2 className="text-base font-semibold text-[#e2e8f0]">⚙️ Settings</h2>
      {saved && <div className="bg-green-500/20 border border-green-500/40 text-green-400 text-xs px-4 py-2 rounded-lg">✓ Saved & agent restarted</div>}

      <Card title="Strategy">
        <div className="grid grid-cols-2 gap-4 mb-4">
          <Field label="Signal Strength Threshold" envKey="MIN_CONFIDENCE" value={env.MIN_CONFIDENCE||''} onChange={set} />
          <Field label="Min Price Gap Required" envKey="EDGE_THRESHOLD" value={env.EDGE_THRESHOLD||''} onChange={set} />
          <Field label="Min Bet ($)" envKey="MIN_BET_SIZE" value={env.MIN_BET_SIZE||''} onChange={set} />
          <Field label="Max Bet ($)" envKey="MAX_BET_SIZE" value={env.MAX_BET_SIZE||''} onChange={set} />
        </div>
        <SaveBtn onClick={() => save(['MIN_CONFIDENCE','EDGE_THRESHOLD','MIN_BET_SIZE','MAX_BET_SIZE'])} />
      </Card>

      <Card title="Exit Rules">
        <div className="grid grid-cols-2 gap-4 mb-4">
          <Field label="Take Profit (%)" envKey="EXIT_TAKE_PROFIT" value={env.EXIT_TAKE_PROFIT||''} onChange={set} />
          <Field label="Trailing Stop (%)" envKey="TRAILING_STOP_PCT" value={env.TRAILING_STOP_PCT||''} onChange={set} />
          <Field label="Stop Loss (%)" envKey="EXIT_STOP_LOSS" value={env.EXIT_STOP_LOSS||''} onChange={set} />
          <Field label="Max Hold (hours)" envKey="EXIT_MAX_HOURS" value={env.EXIT_MAX_HOURS||''} onChange={set} />
        </div>
        <SaveBtn onClick={() => save(['EXIT_TAKE_PROFIT','TRAILING_STOP_PCT','EXIT_STOP_LOSS','EXIT_MAX_HOURS'])} />
      </Card>

      <Card title="Scan & AI Settings">
        <div className="grid grid-cols-2 gap-4 mb-4">
          <Field label="Scan off-peak (min)" envKey="SCAN_INTERVAL_MINUTES" value={env.SCAN_INTERVAL_MINUTES||''} onChange={set} />
          <Field label="Scan active (min)" envKey="SCAN_INTERVAL_ACTIVE_MINUTES" value={env.SCAN_INTERVAL_ACTIVE_MINUTES||''} onChange={set} />
          <Field label="Max AI Analyses per Scan" envKey="MAX_LLM_CALLS_PER_CYCLE" value={env.MAX_LLM_CALLS_PER_CYCLE||''} onChange={set} />
          <Field label="Daily AI Budget ($)" envKey="LLM_DAILY_COST_LIMIT_USD" value={env.LLM_DAILY_COST_LIMIT_USD||''} onChange={set} />
        </div>
        <SaveBtn onClick={() => save(['SCAN_INTERVAL_MINUTES','SCAN_INTERVAL_ACTIVE_MINUTES','MAX_LLM_CALLS_PER_CYCLE','LLM_DAILY_COST_LIMIT_USD'])} />
      </Card>
    </div>
  )
}
