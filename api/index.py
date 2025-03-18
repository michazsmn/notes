from fastapi import FastAPI, Depends, HTTPException
from .schemas import *
from .models import *
from .services import *
from .db import get_db, Engine
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/notes/", response_model=list[Note])
def get_all_notes(db : Session = Depends(get_db)):
    return get_notes(db)

@app.post("/notes/", response_model=Note)
def post_notes(note : NoteIn, db : Session = Depends(get_db)):
    return create_note(db, note)
