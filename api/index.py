from fastapi import FastAPI, Depends, HTTPException
from .schemas import *
from .models import *
from .services import *
from .db import get_db, Engine
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/notes/", response_model=list[Note])
async def get_all_notes(db : Session = Depends(get_db)):
    return get_notes(db)

@app.post("/notes/", response_model=Note)
async def post_notes(note : NoteIn, db : Session = Depends(get_db)):
    return create_note(db, note)

@app.put("/notes/{id}", response_model=Note)
async def update_note(id : int, db : Session = Depends(get_db)):
    db_update = toggle_status(db, id)
    if db_update:
        return db_update
    else:
        raise HTTPException(status_code=404, detail="invalid id")

@app.delete("/notes/{id}", response_model=Note)
async def delete_note(id : int, db : Session = Depends(get_db)):
    deleted_note = del_note(db, id)
    if deleted_note:
        return deleted_note
    else:
        raise HTTPException(status_code=404, detail="invalid id")