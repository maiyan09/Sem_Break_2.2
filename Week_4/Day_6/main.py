from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel
from database import load_users, save_users
from auth import create_token, verify_token
from security import hash_password, verify_password

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_token(token)
        return payload
    except Exception:
        return {"error": "Invalid or expired token"}

class User(BaseModel):
    username: str
    password: str

    
@app.post("/register")
def register(user: User):
    users = load_users()

    for i in users:
        if i["username"] == user.username:
            return {
                "message": "Username already exists"
            }

    print(user.password)
    print(type(user.password))
    print(len(user.password))
    users.append({
        "username": user.username,
        "password": hash_password(user.password)
    })

    save_users(users)
    print(user.password)
    print(type(user.password))
    print(len(user.password))

    return {
        "message": "User registered successfully"
    }

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    users = load_users()
    
    for i in users:
        if i["username"] == form_data.username:
            if verify_password(form_data.password, i["password"]):
                token = create_token(form_data.username)
                return {
                    "access_token": token,
                    "token_type": "bearer"
                }
    
    raise HTTPException(
        status_code=401,
            detail="Invalid username or password"
        )
        
@app.get("/profile")
def profile(current_user = Depends(get_current_user)):
    return {
        "username": current_user["username"],
        "role": current_user["role"]
    }