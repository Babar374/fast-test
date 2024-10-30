# crud.py
from sqlalchemy.orm import Session
from .models import Post
from .schema import PostCreate

def create_post(db: Session, post: PostCreate):
    db_post = Post(name=post.name, clas=post.clas)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()
