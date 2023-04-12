import logging
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.note import Note as NoteModel, NoteCreate, NoteUpdate, Note

logger = logging.getLogger('notes_API')


def create_init_note(db: Session, note: Note) -> Note:
    db_note = Note(
        title=note.title,
        content=note.content,
        user_id=note.user_id
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    logger.info(f'Created note {db_note}')
    return db_note


def get_note_by_id(db: Session, id_: int) -> Note:
    return db.query(Note).filter(Note.id == id_).first()


def get_note_list(db: Session) -> List[Note]:
    return db.query(Note).all()


def create_note(db: Session, note: NoteCreate) -> NoteModel:
    db_note = NoteModel(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def update_note(db: Session, db_note: NoteModel, note: NoteUpdate) -> NoteModel:
    for field, value in note:
        setattr(db_note, field, value)
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(db: Session, db_note: NoteModel) -> None:
    db.delete(db_note)
    db.commit()

