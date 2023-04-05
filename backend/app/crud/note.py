import logging
from typing import List
from sqlalchemy.orm import Session
from app.models.note import Note

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
