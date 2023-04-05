import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.note import NoteModel
from app.models.note import Note
from app.crud.note import get_note_by_id, get_note_list


note_router = APIRouter()
logger = logging.getLogger("notes_API")


@note_router.get('/note/{note_id}', response_model=NoteModel)
def get_note(note_id: int, db: Session = Depends(get_db)) -> Note:
    if db_note := get_note_by_id(db, note_id):
        logger.info(msg=f"Get note {db_note}")
        return db_note
    else:
        logger.error(f"Note does\'t with id={note_id} exist")
        raise HTTPException(status_code=404, detail=f"Note does\'t with id={note_id} exist")




