import Link from 'next/link'
import React from 'react'

const test = () => {
  return (
    <main>
      <h1>Hello</h1>
      <Link href="/users/new">Users</Link>
    </main>

  )
}

export default test