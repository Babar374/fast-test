# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

# class Post(Base):
#     __tablename__ = "posts"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     clas = Column(String, index=True)
#     usser_id = Column(Integer, ForeignKey('users.id'))
#     creator = relationship("usser", back_populates="posts")
#
#
# class usser(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, index=True)
#     password = Column(String, index=True)
#     posts = relationship("Post", back_populates="creator")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    clas = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)  # Updated to `user_id`
    creator = relationship("User", back_populates="posts")  # Updated to `User`

class User(Base):  # Updated class name to `User`
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    posts = relationship("Post", back_populates="creator")
