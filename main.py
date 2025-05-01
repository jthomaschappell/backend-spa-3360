import os
from schemas.book_schema import BookResponse
from services.book_service import BookService
import fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import book_controller
from controllers import purchased_items_controller

app = fastapi.FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(book_controller.router)
app.include_router(purchased_items_controller.router)
@app.get("/")
def read_root():
    return {"message": "Hello World"}