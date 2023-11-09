from fastapi import FastAPI, File, UploadFile, Form
from typing import Annotated

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my Upload API"}

# Form for Signup route
@app.post("/signup")
async def signup(
    username: Annotated[str, Form()],
    firstname: Annotated[str, Form()],
    lastname: Annotated[str, Form()],
    email: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    print(username, firstname, lastname)
    return {"username": username, "firstname": firstname, "lastname": lastname, "password": password}
    

# Login route
@app.post("/login")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
   return {"username": username, "password": password}

# User Details
@app.post("/user")
async def user(
    age: Annotated[int, Form()],
    name: Annotated[str, Form()],
    DOB: Annotated[str, Form()],
    gender: Annotated[str, Form()],
    nationality: Annotated[str, Form()]
):
    return {"age": age, "name":name, "Date of Birth":DOB}

# Upload a single file
@app.post("/file/")
async def upload_file(
    file: Annotated[bytes, File()],
):
    return {"file_size": len(file)}

# Save file to disk
def save_to_disk(uploaded_file: UploadFile):
    with open(uploaded_file.filename, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())      
        
# Using FileUpload
@app.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile
):
    save_to_disk(file)
    return {"filename": file.filename, "content_type": file.content_type}
    