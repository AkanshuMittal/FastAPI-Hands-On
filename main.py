from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"messages": "Hello World"}

@app.get("/posts")
def create_posts():
    return {"messages": "Hello Friends"}

@app.post("/createposts")
def create_posts():
    return {"messages": "Hey, How are you?"}
