from fastapi import FastAPI, Response, status, HTTPException 
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    #rating: Optional[int] = None
    
# database connection
while True:
    try:
        conn = psycopg2.connect(host="localhost", dbname="fastapi", user="postgres", password="akanshu2307@#", cursor_factory=RealDictCursor)
        cursor = conn.cursor()   # for performing all the database operations or executing queries
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(2)


@app.get("/")
def root():
    return {"messages": "Hello World"}

# @app.get("/posts")
# def create_posts():
#     return {"messages": "Hello Friends"}

@app.get("/posts")
def get_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return {"data": posts}

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
    cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *", 
                    (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


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
    cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                              detail=f"post with id: {id} was not found")
    return {"post_detail": post}

##  Delete the post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_post_index(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#update the post
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_post_index(id)

    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict

    return {"data": post_dict}




