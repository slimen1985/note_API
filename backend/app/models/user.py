from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .mixin import Timestamp
from .role import Role
from .note import Note


class User(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean, nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)

    role = relationship("Role", back_populates="user")
    notes = relationship("Note", back_populates="user")
