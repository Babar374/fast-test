from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status
from blog.hashing import Hash
from blog import jwtoken
from blog import database
from blog import models

from blog import schema
router = APIRouter()


@router.post('/login')
def login(request: schema.login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Email or password incorrect')
    if not Hash.verify(user.password, request.password):
        raise
    access_token = jwtoken.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}