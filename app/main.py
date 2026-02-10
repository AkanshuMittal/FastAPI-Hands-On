from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schema
from .database import engine, get_db
from typing import List

models.Base.metadata.create_all(bind=engine)

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
    return {"Hello World"}

# @app.get("/posts")
# def create_posts():
#     return {"messages": "Hello Friends"}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@app.get("/posts", response_model=List[schema.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("SELECT * FROM posts")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return posts

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


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schema.Post)
def create_posts(post: schema.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *", 
    #                 (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post


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
def get_post(id: int, response: Response, db: Session = Depends(get_db), response_model=schema.Post):
    # cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id),))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                              detail=f"post with id: {id} was not found")
    return post

##  Delete the post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#update the post
@app.put("/posts/{id}")
def update_post(id: int, updated_post: schema.PostCreate, db: Session = Depends(get_db), response_model=schema.Post):
    # cursor.execute("UPDATE posts SET title=%s, content=%s, published=%s WHERE id =%s RETURNING *", 
    #                 (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    
    return post_query.first()



@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user