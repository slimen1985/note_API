from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .mixin import Timestamp
from .role import Role


class User(Timestamp, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)

    role = relationship("Role", back_populates="user")
    note = relationship("Note", back_populates="user_note")

    @staticmethod
    def create(**kwargs):
        user = User()
        for key, value in kwargs.items():
            setattr(user, key, value)
        return user


