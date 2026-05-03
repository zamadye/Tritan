'use client'
import { useState, useEffect, useCallback } from 'react'
import type { DashboardData } from '@/types'

export function useData() {
  const [data, setData] = useState<DashboardData | null>(null)
  const [agent, setAgent] = useState({ active: false, mode: 'demo' })
  const [account, setAccount] = useState<{ usdc_balance: number; wallet: string; positions: any[] } | null>(null)
  const [loading, setLoading] = useState(false)

  const refresh = useCallback(async () => {
    const [s, a, acc] = await Promise.all([
      fetch('/api/stats').then(r => r.json()).catch(() => null),
      fetch('/api/agent').then(r => r.json()).catch(() => ({ active: false, mode: 'demo' })),
      fetch('/api/account').then(r => r.json()).catch(() => null),
    ])
    if (s) setData(s)
    setAgent(a)
    if (acc) setAccount(acc)
  }, [])

  useEffect(() => {
    refresh()
    const t = setInterval(refresh, 30000)
    return () => clearInterval(t)
  }, [refresh])

  const agentAction = useCallback(async (action: string, mode?: string) => {
    setLoading(true)
    await fetch('/api/agent', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action, mode }),
    })
    setTimeout(() => { refresh(); setLoading(false) }, 2000)
  }, [refresh])

  return { data, agent, account, loading, refresh, agentAction }
}
