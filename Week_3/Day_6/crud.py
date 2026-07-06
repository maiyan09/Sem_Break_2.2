from sqlalchemy.orm import Session
from schemas import BookCreate
from models import Book

def create_book(book : BookCreate, db: Session):
    db_book = Book(
        title = book.title,
        author= book.author,
        published_year = book.published_year,
        genre = book.genre,
        available = book.available
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book