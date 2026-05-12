'use client'
import { useState, useEffect, useCallback } from 'react'
import type { DashboardData } from '@/types'

export function useData() {
  const [data, setData] = useState<DashboardData | null>(null)
  const [agent, setAgent] = useState({ active: false, mode: 'demo' })
  const [account, setAccount] = useState<{ usdc_balance: number; wallet: string; positions: any[] } | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const refresh = useCallback(async () => {
    try {
      const [s, a, acc] = await Promise.all([
        fetch('/api/stats').then(r => { if (!r.ok) throw new Error(`stats ${r.status}`); return r.json() }),
        fetch('/api/agent').then(r => { if (!r.ok) throw new Error(`agent ${r.status}`); return r.json() }),
        fetch('/api/account').then(r => { if (!r.ok) throw new Error(`account ${r.status}`); return r.json() }).catch(() => null),
      ])
      if (s) { setData(s); setError(null) }
      setAgent(a)
      if (acc) setAccount(acc)
      // Sync localStorage user.mode with server-side agent_mode
      if (s?.agent_mode || a?.mode) {
        const serverMode = s?.agent_mode || a?.mode
        try {
          const stored = localStorage.getItem('tritan_user')
          if (stored) {
            const user = JSON.parse(stored)
            if (user.mode !== serverMode) {
              user.mode = serverMode
              localStorage.setItem('tritan_user', JSON.stringify(user))
            }
          }
        } catch {}
      }
    } catch (e: any) {
      setError(e.message || 'Failed to load data')
    }
  }, [])

  useEffect(() => {
    refresh()
    const t = setInterval(refresh, 30000)
    return () => clearInterval(t)
  }, [refresh])

  const agentAction = useCallback(async (action: string, mode?: string) => {
    setLoading(true)
    try {
      await fetch('/api/agent', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action, mode }),
      })
    } catch {}
    setTimeout(() => { refresh(); setLoading(false) }, 2000)
  }, [refresh])

  return { data, agent, account, loading, error, refresh, agentAction }
}
