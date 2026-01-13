from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

app = FastAPI()

@app.get("/")
def root():
    return {"messages": "Hello World"}

@app.get("/posts")
def create_posts():
    return {"messages": "Hello Friends"}

# @app.post("/createposts")
# def create_post(payload : dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title : {payload['title']} content : {payload['content']}"}

# @app.post("/create_posts")
# def create_posts():
#     return {"messages": "Hello, How are you?"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post.dict())
    return {"data": "post"}



