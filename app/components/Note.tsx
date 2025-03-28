import { stat } from 'fs'
import React from 'react'

const Note = ({notetext, status} : {notetext : string, status : boolean}) => {

  return (
    <div>
      <div>Note: {notetext} </div>
      <div>Status: {status ? "Completed" : "Not completed"}</div>
    </div>
  )
}

export default Note