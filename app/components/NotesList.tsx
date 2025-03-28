"use client"

import React from 'react'
import { useState, useEffect } from 'react';
import Note  from './Note'

const NotesList = () => {

  const [responseData, setResponseData] = useState(null);
  let headers = new Headers()

  headers.append('Content-Type', 'application/json');

  useEffect(() => {
    fetch("http://localhost:8000/notes", {
      mode: 'no-cors', //Remove later
      method: "GET",
      headers: headers
    })
      .then((response) => response.json())
      .then((data) => {
        setResponseData(data);
        })
      .catch((error) => console.error(error));
  }, []);

  return (
    <div>

    </div>
  )
}

export default NotesList