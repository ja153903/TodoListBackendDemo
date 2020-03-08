from sqlalchemy import Column, Integer, String, Date

from .base import Base

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    title = Column(String(length=255))
    description = Column(String(length=255))
    created_at = Column(Date)
