import httpx
from schemas.book_schema import BookResponse

class BookRepository:
    @staticmethod
    async def get_book(book_title: str) -> BookResponse: 
        url = f"https://openlibrary.org/search.json?title={book_title}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()["docs"][0]
                return BookResponse(
                    author=data["author_name"][0] if isinstance(data["author_name"], list) else data["author_name"],
                    cover_id=str(data["cover_i"]),
                    title=data["title"]
                )
            else:
                raise Exception(f"Failed to fetch book: {response.status_code}")




# from schemas.swapi_schema import FilmResponse


# class SWAPIRepository:
#     @staticmethod
#     async def get_all_films() -> FilmResponse | None:
#         url = "https://swapi.dev/api/films/"
#         async with httpx.AsyncClient() as client:
#             response = await client.get(url)
#             if response.status_code == 200:
#                 return FilmResponse(**response.json())
#         return None


"""
Instead of taking 
"""