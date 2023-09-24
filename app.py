from fastapi import FastAPI
from uuid import UUID

app = FastAPI()

# Create a dictionary to store the books in memory
books = {}

''''
CRUD Operations
Create - POST
Read - GET
Update - PUT
Delete - DELETE
'''

book_data = {
    "id": 0,
    "title": "",
    "author": "",
    "year_published": 2000,
    "pages": 0,
    "language": "",
}

@app.get("/")
def home():
    return {"message": "Welcome to the Book API"}

# Get all books
@app.get("/books")
def get_books():
    return books

# Create a book
@app.post("/books")
def create_book(
    title: str, author: str, year_published: int, pages: int, language: str
):
    new_book = book_data.copy()
    new_book["id"] = str(UUID(int=len(books) + 1))
    new_book["title"] = title
    new_book["author"] = author
    new_book["year_published"] = year_published
    new_book["pages"] = pages
    new_book["language"] = language
    
    books[new_book["id"]] = new_book
    
    return {"message": "Book created successfully", "data": new_book}

# Update a book
@app.put("/books/{id}")
def update_book(
    id: str, title: str, author: str, year_published: int, pages: int, language: str
):
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}
    
    book["title"] = title
    book["author"] = author
    book["year_published"] = year_published
    book["pages"] = pages
    book["language"] = language
    
    return {"message": "Book updated successfully", "data": book}

# Delete a book
@app.delete("/books/{id}")
def delete_book(id: str):
    book = books.get(id)
    if not book:
        return {"error": "Book not found"}
    
    del books[id]
    
    return {"message": "Book deleted successfully"}
    