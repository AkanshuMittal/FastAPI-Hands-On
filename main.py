from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"messages": "Hello World"}

@app.get("/posts")
def create_posts():
    return {"messages": "Hello Friends"}

@app.post("/create_posts")
def create_post(payload : dict = Body(...)):
    print(payload)
    return {"messages": "successfully created posts"}

@app.post("/createposts")
def create_posts():
    return {"new_post": f"title"}
