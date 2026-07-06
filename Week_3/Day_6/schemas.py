from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int
    genre: str
    available: bool = True
    
class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    published_year: int | None = None
    genre: str | None = None
    available: bool | None = None