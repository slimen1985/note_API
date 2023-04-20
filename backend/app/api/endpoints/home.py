from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.user import get_user_by_username
from app.core.security import verify_password

home_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@home_router.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@home_router.post("/")
def login(request: Request, username: str = Form(...), password: str = Form(...),
          db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=username)
    if not user:
        return templates.TemplateResponse("register.html", {"request": request})
    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return templates.TemplateResponse("authenticated.html", {"request": request, "username": user.username})