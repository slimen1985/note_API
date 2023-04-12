from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.user import get_user_by_username, create_user
from app.schemas.user import UserCreateModel, UserPublicModel
from app.core.security import get_password_hash

user_router = APIRouter()


@user_router.post("/users/register", response_model=UserPublicModel, status_code=201)
def register_new_user(user: UserCreateModel, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user.password = get_password_hash(user.password)
    return create_user(db=db, user=user)