from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Note(Base):
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, index=True, nullable=False)
    content = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False, default=2)

    owner = relationship("User", back_populates="notes")
