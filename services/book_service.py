from repositories.book_repository import BookRepository
from schemas.book_schema import BookResponse


class BookService:
    @staticmethod
    async def get_book(book_title: str) -> BookResponse:
        return await BookRepository.get_book(book_title)
    