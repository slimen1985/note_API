from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .user import User


class Note(Base):
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user_note = relationship("User", back_populates="note")


class NoteCreate(BaseModel):
    title: str
    content: str
    user_id: int


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    is_active: Optional[bool] = None



