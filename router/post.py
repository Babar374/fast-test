from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from blog import schema
from sqlalchemy.orm import Session
from blog import database
from blog import models


route = APIRouter(
    tags=['post'],
)


@route.post("/posts/", response_model=schema.PostCreate, status_code=status.HTTP_201_CREATED, summary="Create a new post", response_description="crete")
def create_post(post: schema.PostCreate, db: Session = Depends(database.get_db)):
    # return crud.create_post(db=db, post=post)
    new_post = models.Post(
        name=post.name,
        clas=post.clas,
        user_id=post.user_id  # Use user_id here
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

#
@route.get("/posts/")
def read_posts(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Post).all()
    return blogs


@route.delete("/posts/{id}")
def delete_post(id:int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Post).filter(models.Post.id == id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} not found")
    db.delete(blog)
    db.commit()
    return {"message": "Post deleted"}


# @app.put('/posts/{id}', status_code=HTTP_202_ACCEPTED)
# def update_post(id, request: schema.PostCreate, db: Session = Depends(get_db)):
#     update_data = db.query(models.Post).filter(models.Post.id == id)
#     if update_data.first() is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     update_data.update(request.dict())
#     db.commit()
#     return 'updated'


@route.put('/posts/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_post(id: int, request: schema.PostCreate, db: Session = Depends(database.get_db)):
    update_data = db.query(models.Post).filter(models.Post.id == id)

    if update_data.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    # Convert the Pydantic model to a dictionary
    update_data.update(request.dict())
    # update_data.update(request)
    db.commit()
    return {"detail": "Post updated"}


@route.get('/posts/{id}/', response_model=schema.responseUpdatemodel, status_code=status.HTTP_200_OK)
def get_each_posts(id, response: schema.responseUpdatemodel, db: Session = Depends(database.get_db)):
    blog = db.query(models.Post).filter(models.Post.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return blog