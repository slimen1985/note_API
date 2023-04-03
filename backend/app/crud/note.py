import logging
from sqlalchemy.orm import Session
from app.models.note import Note

logger = logging.getLogger('notes_API')


def create_init_note(db: Session, note: Note) -> Note:
    db_note = Note(
        title=note.title,
        content=note.content,
        owner_id=note.user_id
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    logger.info(f'Created note {db_note}')
    return db_note
