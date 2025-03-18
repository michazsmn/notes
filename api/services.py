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
