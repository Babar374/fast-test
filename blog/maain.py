# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal
import crud
from schema import PostCreate

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/posts/", response_model=PostCreate)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)

@app.get("/posts/")
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_posts(db, skip=skip, limit=limit)
