# from fastapi import FastAPI
# from blog.schema import Post
#
# app = FastAPI()
#
# @app.get("/")
# def index():
#     return {"data":
#                 {"Hello": "World"}}
#
#
# @app.get("/items/{item_id}")
# def item(item_id: int):
#     return {"data": item_id}
#
#
# @app.get('/item/{id}/comments')
# def comments(id):
#     return {'data':{'1','2'}}
#
#
# @app.get('/blog')
# def blog(limit, published:bool):
#     if published:
#         return {'data':{'1','2'}}
#     else:
#         return {'data':f"{limit} blogs from db"}
#
#
# @app.post('/blog')
# def create(request: Post):
#     return request



# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.status import HTTP_202_ACCEPTED
from passlib.context import CryptContext

from blog import models
from blog import schema
from blog.database import engine, SessionLocal
from blog import crud
from blog.schema import PostCreate, responseUpdatemodel

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

@app.post("/posts/", response_model=PostCreate, status_code=status.HTTP_201_CREATED, summary="Create a new post", response_description="crete")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)

@app.get("/posts/")
def read_posts(db: Session = Depends(get_db)):
    blogs = db.query(models.Post).all()
    return blogs


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT, response_description="Deleted post")
def delete_post(id, db: Session = Depends(get_db)):
    db.query(models.Post).filter(models.Post.id == id).delete(synchronize_session=False)
    db.commit()
    # return {"message": "Post deleted"}


# @app.put('/posts/{id}', status_code=HTTP_202_ACCEPTED)
# def update_post(id, request: schema.PostCreate, db: Session = Depends(get_db)):
#     update_data = db.query(models.Post).filter(models.Post.id == id)
#     if update_data.first() is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     update_data.update(request.dict())
#     db.commit()
#     return 'updated'


@app.put('/posts/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, request: PostCreate, db: Session = Depends(get_db)):
    update_data = db.query(models.Post).filter(models.Post.id == id)
    if update_data.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    # Convert the Pydantic model to a dictionary
    update_data.update(request.dict())
    # update_data.update(request)
    db.commit()
    return {"detail": "Post updated"}


@app.get('/posts/{id}/', response_model=schema.responseUpdatemodel, status_code=status.HTTP_200_OK)
def get_each_posts(id, response: responseUpdatemodel, db: Session = Depends(get_db)):
    blog = db.query(models.Post).filter(models.Post.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return blog

from blog import hashing
# from passlib.context import CryptContext
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #know we follow clean code step
@app.post('/users', response_model=schema.usershow)
def create_users(request: schema.userschema, db: Session = Depends(get_db)):
    # hash_password = pwd_context.hash(request.password)
    new_user = models.usser(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password) )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user