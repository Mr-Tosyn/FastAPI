from fastapi import FastAPI
#THE MAIN THE MAIN
# FAST DIE
app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "This is a simple API created using FastAPI"}

 