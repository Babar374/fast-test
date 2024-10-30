# models.py
from sqlalchemy import Column, Integer, String
from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    clas = Column(String, index=True)


class usser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)