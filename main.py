from schemas.book_schema import BookResponse
from services.book_service import BookService
import fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import book_controller

app = fastapi.FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.include_router(book_controller.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}