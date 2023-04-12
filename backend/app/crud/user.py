import logging
from typing import Optional

from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreateModel

logger = logging.getLogger('notes_API')


def create_init_user(db: Session, user: User) -> User:
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        is_active=user.is_active,
        role_id=user.role_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info(f'Created user {db_user}')
    return db_user


def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreateModel) -> User:
    db_user = User(username=user.username, password=user.password, email=user.email, role_id=user.role_id, is_active=user.is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


