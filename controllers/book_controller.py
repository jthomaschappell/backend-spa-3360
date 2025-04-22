from fastapi import APIRouter
from services.book_service import BookService
from schemas.book_schema import BookResponse

router = APIRouter(prefix="/api/book")

@router.get("/{book_title}", response_model=BookResponse)
async def get_books(book_title: str):
    return await BookService.get_book(book_title)
