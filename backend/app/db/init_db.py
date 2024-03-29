import logging

from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.core.config import Settings

from app.schemas.user import UserCreateModel
from app.schemas.note import NoteCreateModel

from app.crud.user import create_init_user
from app.crud.note import create_init_note

settings = Settings()
logger = logging.getLogger('notes_API')


def init_db_user(db: Session):
    create_user(db)


def init_db_note(db: Session):
    create_note(db)


def create_user(db: Session):
    user = settings.INIT_USER
    try:
        db_user = UserCreateModel(
            username=user['username'],
            email=user['email'],
            password=user['password'],
            is_active=user['is_active'],
            role_id=user['role_id']
        )
    except ValidationError as e:
        logger.error(f"An error occur while creating model {e}")
    else:
        create_init_user(db, db_user)


def create_note(db: Session):
    for note in settings.INIT_NOTE:
        db_note = NoteCreateModel(
            title=note['title'],
            content=note['content'],
            user_id=note['user_id']
        )
        create_init_note(db, db_note)
