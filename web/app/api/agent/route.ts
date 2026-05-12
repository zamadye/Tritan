import { NextResponse } from 'next/server'
import { exec } from 'child_process'
import { promisify } from 'util'
import fs from 'fs'
import { ROOT, readJSON } from '@/lib/paths'

const execAsync = promisify(exec)

// Whitelists — prevent injection
const ALLOWED_ACTIONS = new Set(['start', 'stop', 'restart', 'scan', 'switch_mode', 'sync'])
const ALLOWED_MODES = new Set(['demo', 'live'])

export async function GET() {
  try {
    // Check if agent is running via pgrep
    const { stdout } = await execAsync('pgrep -f "main.py run" || true')
    const active = stdout.trim().length > 0
    // Read mode from .env
    const envContent = fs.readFileSync(`${ROOT}/.env`, 'utf-8')
    const modeMatch = envContent.match(/^AGENT_MODE=(.+)$/m)
    const mode = modeMatch?.[1]?.trim() || 'demo'

    // Get live stats if in live mode
    let liveStats = null
    if (mode === 'live') {
      liveStats = readJSON('live_stats.json') || null
    }

    return NextResponse.json({
      active,
      mode,
      liveStats,
      timestamp: new Date().toISOString(),
    })
  } catch {
    return NextResponse.json({ active: false, mode: 'demo' })
  }
}

export async function POST(req: Request) {
  const body = await req.json()
  const action: string = body.action ?? ''
  const mode: string = body.mode ?? ''

  // Whitelist validation
  if (!ALLOWED_ACTIONS.has(action)) {
    return NextResponse.json({ ok: false, error: 'Invalid action' }, { status: 400 })
  }
  if (action === 'switch_mode' && !ALLOWED_MODES.has(mode)) {
    return NextResponse.json({ ok: false, error: 'Invalid mode' }, { status: 400 })
  }

  try {
    if (action === 'start') {
      await execAsync(`cd ${ROOT} && setsid .venv/bin/python main.py run >> /tmp/tritan-agent.log 2>&1 &`)
    }
    if (action === 'stop') {
      await execAsync('pkill -f "main.py run" || true')
    }
    if (action === 'restart') {
      await execAsync('pkill -f "main.py run" || true')
      await new Promise(r => setTimeout(r, 1000))
      const { spawn } = await import('child_process')
      const fs2 = await import('fs')
      const logFd = fs2.openSync('/tmp/tritan-agent.log', 'a')
      spawn('.venv/bin/python', ['main.py', 'run'], {
        cwd: ROOT, detached: true, stdio: ['ignore', logFd, logFd],
      }).unref()
      fs2.closeSync(logFd)
    }
    if (action === 'scan') {
      const { spawn } = await import('child_process')
      spawn('.venv/bin/python', ['main.py', 'scan'], { cwd: ROOT, detached: true, stdio: 'ignore' }).unref()
    }
    if (action === 'switch_mode') {
      // Update .env file
      let envContent = fs.readFileSync(`${ROOT}/.env`, 'utf-8')
      envContent = envContent.replace(/^AGENT_MODE=.*/m, `AGENT_MODE=${mode}`)
      fs.writeFileSync(`${ROOT}/.env`, envContent)

      // If switching to live, trigger sync
      if (mode === 'live') {
        try {
          await execAsync(`cd ${ROOT} && .venv/bin/python agent/sync_polymarket.py`, { timeout: 30000 })
        } catch (e) {
          console.error('Sync failed:', e)
        }
      }

      // Restart agent with new mode
      await execAsync('pkill -f "main.py run" || true')
      await new Promise(r => setTimeout(r, 1500))
      const { spawn } = await import('child_process')
      const fs2 = await import('fs')
      const logFd = fs2.openSync('/tmp/tritan-agent.log', 'a')
      spawn('.venv/bin/python', ['main.py', 'run'], {
        cwd: ROOT, detached: true, stdio: ['ignore', logFd, logFd],
      }).unref()
      fs2.closeSync(logFd)
    }
    if (action === 'sync') {
      // Manual sync trigger
      try {
        const { stdout } = await execAsync(
          `cd ${ROOT} && .venv/bin/python agent/sync_polymarket.py`,
          { timeout: 30000 }
        )
        return NextResponse.json({ ok: true, output: stdout })
      } catch (e: any) {
        return NextResponse.json({ ok: false, error: e.message }, { status: 500 })
      }
    }
    return NextResponse.json({ ok: true })
  } catch (e: any) {
    return NextResponse.json({ ok: false, error: 'Command failed' }, { status: 500 })
  }
}
