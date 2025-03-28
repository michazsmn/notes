from .models import notes
from .schemas import NoteIn
from sqlalchemy.orm import Session


def create_note(db : Session, data : NoteIn):
    note_instance = notes(**data.model_dump())
    db.add(note_instance)
    db.commit()
    db.refresh(note_instance)
    return note_instance

def get_notes(db : Session):
    return db.query(notes).all()

def get_note_by_id(db : Session, id : int):
    return db.query(notes).filter(notes.id == id).first()

def toggle_status(db : Session, id : int):
    note_query = db.query(notes).filter(notes.id == id).first()
    if note_query:
        setattr(note_query, "completed", not getattr(note_query, "completed"))
        db.commit()
        db.refresh(note_query)
    return note_query

def del_note(db : Session, id : int):
    note_query = db.query(notes).filter(notes.id == id).first()
    if note_query:
        db.delete(note_query)
        db.commit()
    return note_query

        
        