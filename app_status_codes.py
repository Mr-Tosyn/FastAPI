# Status COde
# 200 - Default status code for a successful HTTP request. which means "OK"
# 201 - The request has been fulfilled and resulted in a new resource being created. which means "Created"
# 400 - The server cannot or will not process the request due to an apparent client error. which means "Bad Request"
# 300 - The request has more than one possible responses. which means "Multiple Choices"
# 404 - The requested resource could not be found but may be available in the future. which means "Not Found"
# 500 - A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. which means "Internal Server Error"


from fastapi import FastAPI, HTTPException
from uuid import UUID
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Use Pydantic to create a model for the book data
class Book(BaseModel):
    id: str
    title: str
    author: str
    year_published: int
    pages: int
    language: str
    
class BookCreate(BaseModel):
    title: str
    author: str
    year_published: int
    pages: int 
    language: str
    
class BookUpdate(BaseModel):
    title: str
    pages: int
    
class Books(BaseModel):
    books: list[Book]
    
class Response(BaseModel):
    message: Optional[str] = None
    data: Optional[Book | Books] = None
    

books: dict[str, Book] = {}

@app.get("/", status_code=200)
def home():
    return {"message": "Welcome to my Book API"}

# Get all books
@app.get("/books", status_code=200)
def get_books():
    return books

@app.get("/books/{id}", status_code=200)
def get_book_by_id(id: UUID):
    book = books.get(str(id))
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Create a book
@app.post("/books", status_code=201)
def add_book(my_book: BookCreate):
    book = Book(id=str(UUID(int=len(books) + 1)), **my_book.dict())
    books[book.id] = book
    
    return Response(message="Book created successfully", data=book)

# Update a book
@app.put("/books/{id}", status_code=200)
def update_book(id: UUID, my_book: BookUpdate):
    book = books.get(str(id))
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.title = my_book.title
    book.pages = my_book.pages
    
    return Response(message="Book updated successfully", data=book) 

# Delete a book
@app.delete("/books/{id}", status_code=200)
def delete_book(id: UUID):
    book = books.get(str(id))
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    del books[book.id]
    
    return Response(message="Book deleted successfully", data=book)