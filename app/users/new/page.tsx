import React from 'react'
import Link from 'next/link'
import ButtonComponent from '@/app/components/ButtonComponent'


const page2 = () => {
  return (
    <main>
      <h1>Hello</h1>
      <Link href="/users">Users</Link>
      <ButtonComponent />
    </main>
  )
}

export default page2