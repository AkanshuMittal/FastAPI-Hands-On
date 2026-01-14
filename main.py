from fastapi import FastAPI, Response, status, HTTPException 
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


def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p

def find_post_index(id):
    for i,p in enumerate(my_posts):
        if p["id"]==id:
            return i
        
# @app.post("/createposts")
# def create_post(payload : dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title : {payload['title']} content : {payload['content']}"}

# @app.post("/create_posts")
# def create_posts():
#     return {"messages": "Hello, How are you?"}


# @app.post("/posts")
# def create_posts(post: Post):
#     print(post)
#     print(post.dict())
#     return {"data": "post"}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


# # Get one post 
# @app.get("/posts/{id}")
# def get_post(id):
#     print(id)
#     return {"post_detail": f"Here is the post {id}"}


# @app.get("/posts/{id}")
# def get_posts(id: int):   # validation
#     post = find_post(id)
#     print(post)
#     return {"post_detail": post}

# @app.get("/posts/{id}")
# def get_post(id: int, response: Response):
#     post = find_post(id)
#     if not post:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"message": f"post with id: {id} was not found"}
#     return {"post_detail": post}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                              detail=f"post with id: {id} was not found")
    return {"post_detail": post}

@app.delete("/posts/{id}")
def delete_post(id: int):
    index = find_post_index(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    my_posts.pop(index)
    return {"message": "Post successfully deleted"}

