from pydantic import BaseModel

class BookResponse(BaseModel):
    author: str
    cover_id: str
    title: str
