from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/calculate/{operator}")
async def calculator(operator: str, a: float, b: float):
    if operator == 'add':
        result = a + b
    elif operator == 'sub':
        result = a - b
    elif operator == 'multiplication':
        result = a * b
    elif operator == 'division':
        if b == 0:
            raise HTTPException(status_code=400, detail= "Can not devide by Zero")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail= "Invalid Operation")
    
    return {
        "operation": operator,
        "a": a,
        "b": b,
        "result": result
    }