import { NextResponse } from 'next/server'
import { exec } from 'child_process'
import { promisify } from 'util'
import { ROOT } from '@/lib/paths'

const execAsync = promisify(exec)

export async function POST() {
  try {
    // Run the Python sync script
    const { stdout, stderr } = await execAsync(
      `cd ${ROOT} && .venv/bin/python agent/sync_polymarket.py`,
      { timeout: 30000 }
    )

    return NextResponse.json({
      ok: true,
      message: 'Sync completed',
      output: stdout,
    })
  } catch (e: any) {
    return NextResponse.json({
      ok: false,
      error: e.message || 'Sync failed',
      stderr: e.stderr,
    }, { status: 500 })
  }
}
