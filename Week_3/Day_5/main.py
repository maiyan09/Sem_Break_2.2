from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import Boolean, create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, Session, declarative_base

app = FastAPI()
DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key = True, index = True)
    task = Column(String)
    is_completed = Column(Boolean, default=False)
    
Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def home():
    return{
        "message": "Welcome to TODO API"
    }
        
@app.post('/todo')
def create_todo(task: str, db: Session = Depends(get_db)):
    todo = Todo(task = task)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    
    return{
        "message": "Task Added Successfully..",
        "data": todo
    }
    
@app.get('/todos')
def all_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos

# Search by ID
@app.get('/todo/{id}')
def src_by_id(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {
        "message": f"Todo of id {id}",
        "data": todo
    }

# Update
@app.put('/todo/{id}')
def update_todo(id: int, task: str, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo.task = task
    db.commit()
    db.refresh(todo)
    
    return {
        "message": "Todo Updated",
        "data": todo
    }

# Delete
@app.delete('/todo/{id}')
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found.")
    
    db.delete(todo)
    db.commit()
    
    return {
        "message": "Todo deleted successfully."
    }