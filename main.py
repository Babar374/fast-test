from wsgiref.util import request_uri

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"data":
                {"Hello": "World"}}


@app.get("/items/{item_id}")
def item(item_id: int):
    return {"data": item_id}


@app.get('/item/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}


@app.get('/blog')
def blog(limit, published:bool):
    if published:
        return {'data':{'1','2'}}
    else:
        return {'data':f"{limit} blogs from db"}