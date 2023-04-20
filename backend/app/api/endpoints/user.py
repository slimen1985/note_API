from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.user import get_user_by_username, create_user
from app.schemas.user import UserCreateModel, UserPublicModel
from app.core.security import get_password_hash, verify_password

user_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@user_router.get("/register")
def get_register_user(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@user_router.post("/register")
def register_new_user(request: Request, username: str = Form(...), email: str = Form(...),
                      password: str = Form(...), role_id: int = Form(...),
                      is_active: bool = Form(...), db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = UserCreateModel(username=username, email=email, password=password, role_id=role_id, is_active=is_active)
    user.password = get_password_hash(user.password)
    create_user(db=db, user=user)
    message = f"User '{username}' has been registered successfully!"
    return templates.TemplateResponse("register.html", {"request": request, "message": message})


@user_router.get("/login")
def get_login_user(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@user_router.post("/login")
def login_user(request: Request, username: str = Form(...), password: str = Form(...),
               db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return RedirectResponse(url="/notes")


@user_router.post("/authenticate")
def authenticate_user(request: Request, username: str = Form(...), password: str = Form(...),
                      db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return templates.TemplateResponse("authenticated.html", {"request": request, "username": user.username,
                                                             "message": "You have successfully logged in!",
                                                             "url": "/notes"})
