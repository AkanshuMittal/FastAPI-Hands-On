from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schema, utils
from .database import engine, get_db
from typing import List
from .routers import post, user


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
        
        cursor = conn.cursor()   # for performing all the database operations or executing queries
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(2)
        

app.include_router(post.router)
app.include_router(user.router)