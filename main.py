from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

app = FastAPI()

@app.get("/")
def root():
    return {"messages": "Hello World"}

# @app.get("/posts")
# def create_posts():
#     return {"messages": "Hello Friends"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

my_posts = [{"title": "title of psot 1", "content": "Content of post 1", "id": 1}, {"title": "favourite fruits", "content": "I like grapes", "id": 2}]
# @app.post("/createposts")
# def create_post(payload : dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title : {payload['title']} content : {payload['content']}"}

# @app.post("/create_posts")
# def create_posts():
#     return {"messages": "Hello, How are you?"}


@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": "post"}



