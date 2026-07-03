from fastapi import FastAPI, HTTPException

app = FastAPI()

students = {
    1 : {
        "name": "Maiyan",
        "age": 23,
        "dep": "CSE"
    },
    2 : {
        "name": "Sajid",
        "age": 20,
        "dep": "EEE"
    },
    3 : {
        "name": "Rakib",
        "age": 22,
        "dep": "Civil"
    },
    4 : {
        "name": "Kadir",
        "age": 24,
        "dep": "Law"
    },
    5 : {
        "name": "Zakir",
        "age": 22,
        "dep": "BBA"
    }
}

@app.get("/")
async def first_page():
    return {
        "Greet": "Welcome to Student API"
    }
    
@app.get('/students')
async def get_students():
    return students

@app.get('/students/search/{student_id}')
async def get_student_by_id(student_id: int):
    return students[student_id]
    
@app.delete('/students/delete/{student_id}')
async def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Invalid student id")
    
    del students[student_id]
    return {"message": "Student deleted successfully"}