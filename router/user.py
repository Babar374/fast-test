from fastapi import APIRouter
from fastapi import Depends
from blog import schema
from blog import database
from sqlalchemy.orm import Session
from blog import models
from blog import hashing
route = APIRouter(
    tags=['user'],
)


@route.post('/users', response_model=schema.usershow)
def create_users(request: schema.userschema, db: Session = Depends(database.get_db)):
    # hash_password = pwd_context.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password) )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user