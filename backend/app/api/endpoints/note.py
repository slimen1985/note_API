import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session

from app.db.session import get_db
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.schemas.note import NoteModel
from app.models.note import Note, NoteCreate, NoteUpdate
from app.crud.note import get_note_by_id, get_note_list, delete_note, update_note, create_note

note_router = APIRouter()
logger = logging.getLogger("notes_API")
templates = Jinja2Templates(directory="templates")


@note_router.get('/note/{note_id}', response_model=NoteModel)
def get_note(note_id: int, request: Request, db: Session = Depends(get_db)) -> Note:
    if db_note := get_note_by_id(db, note_id):
        logger.info(msg=f"Get note {db_note}")
        return templates.TemplateResponse("note.html", {"request": request, "note": db_note})
    else:
        logger.error(f"Note does\'t with id={note_id} exist")
        raise HTTPException(status_code=404, detail=f"Note does\'t with id={note_id} exist")


@note_router.get('/notes', response_class=HTMLResponse)
async def get_notes(request: Request, db: Session = Depends(get_db)):
    notes = get_note_list(db)
    return templates.TemplateResponse("notes.html", {"request": request, "notes": notes})


@note_router.post('/note', response_model=NoteModel)
def create_note_endpoint(note: NoteCreate, db: Session = Depends(get_db)) -> Note:
    created_note = create_note(db, note)
    logger.info(msg=f"Created note {created_note}")
    return created_note


@note_router.put('/note/{note_id}', response_model=NoteModel)
def update_note_endpoint(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)) -> Note:
    if db_note := get_note_by_id(db, note_id):
        updated_note = update_note(db, db_note, note)
        logger.info(msg=f"Updated note {updated_note}")
        return updated_note
    else:
        logger.error(f"Note does\'t with id={note_id} exist")
        raise HTTPException(status_code=404, detail=f"Note does\'t with id={note_id} exist")


@note_router.delete('/note/{note_id}')
def delete_note_endpoint(note_id: int, db: Session = Depends(get_db)):
    if db_note := get_note_by_id(db, note_id):
        delete_note(db, db_note)
        logger.info(msg=f"Deleted note with id={note_id}")
        return {"detail": f"Note with id={note_id} has been deleted"}
    else:
        logger.error(f"Note does\'t with id={note_id} exist")
        raise HTTPException(status_code=404, detail=f"Note does\'t with id={note_id} exist")



