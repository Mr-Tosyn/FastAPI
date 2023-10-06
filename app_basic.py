from fastapi import FastAPI
from uuid import UUID

app = FastAPI


# Now we will create a book api, that performs CRUD operations
# on a book resource. Ww will list to store books in memory
# we will use a dictionary to store the book data.
# the book data will have the following feilds:
# - id: int
# - tittle: str
# - author : str
# - year: int
# - pages: int
# - language: str

# Create a dic to store the books in memory. 
Books = {}

#create a dictonary to store book data
book_data = {"id": 0, "tittle": "", "author": "", "year": 0, "pages": 0, "language": ""}


@app.get("/")
def home():
    return {"message": "Hello from the books AP"}


# Get all books
@app.get("/books") # GET method to get a resource
def get_books():
    return Books


# Get a single book using a path parameter
# You can declare path "paremeters" or "variabl" with the same syntax used by python format strings
# The value of the path parameter item_id will be passed to your function as the argument item-id
@app.get("/books/{id}") # Get method to get a resource
def get_book_by_id(id: str):
    book = books.get(id)
    if not book:
        return {"error": "book not found"}
    
    return book


#Add a book.
@app.post("/books") # p method to create a new resource
def add_book(
    tittle: str, author: str, year: int, page: int, language: str 
):  # these parameters are called "query parameters", The 

