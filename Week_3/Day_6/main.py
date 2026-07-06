from fastapi import FastAPI, Depends
from database import SessionLocal
import schemas
import crud
from sqlalchemy.orm import Session

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/books")
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(book, db)