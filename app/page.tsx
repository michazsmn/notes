import Head from 'next/head'
import { useState, useEffect } from 'react';
import NotesList from './components/NotesList';

export default async function Home() {

  
  
  return (
    <main className="flex flex-col items-center space-y-6">
      <NotesList/>
    </main>
  );
}
