from fastapi import FastAPI
from pip._internal.network import auth

from blog import models
from blog.database import engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

from router import post
from router import user
from router import authorization

app.include_router(post.route)
app.include_router(user.route)
app.include_router(authorization.router)
