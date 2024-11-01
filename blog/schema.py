# from pydantic import BaseModel
#
# class Post(BaseModel):
#
#     name: str
#     clas: str

# schema.py
from pydantic import BaseModel
from sqlalchemy.testing.pickleable import User
from typing import Optional

class PostCreate(BaseModel):
    name: str
    clas: str
    user_id: int

    class Config:
        from_attributes = True


class responseUpdatemodel(PostCreate):
    class Config:
        # orm_mode = True
        from_attributes = True

class userschema(BaseModel):
    name: str
    email: str
    password: str


class usershow(BaseModel):
    name: str
    email: str
    # from_attributes: bool = True
    class Config:
        # orm_mode= True
        from_attributes: bool = True


class login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str]=None