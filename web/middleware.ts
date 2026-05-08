import { NextRequest, NextResponse } from 'next/server'

// Auth disabled — private dev dashboard, not public
// Re-enable by uncommenting below when exposing publicly

export function middleware(req: NextRequest) {
  return NextResponse.next()
}

export const config = {
  matcher: '/api/:path*',
}
