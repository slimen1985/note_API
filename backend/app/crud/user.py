import logging
from sqlalchemy.orm import Session
from app.models.user import User

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
