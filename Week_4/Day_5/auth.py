import jwt
import os
import datetime

SECRET_KEY = "my_super_secret_key"

def create_token(username):
    payload = {
        "username": username,
        "role": "student",
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5)
    }
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )
    with open("token.txt", 'w') as file:
        file.write(token)
        
    return token

def verify_token():
    with open("token.txt", 'r') as file:
        token = file.read()
        
    try:
        decode = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )
        return decode
    
    except FileNotFoundError:
        return None
    except jwt.InvalidTokenError:
        return None

def logout():
    if os.path.exists("token.txt"):
        os.remove("token.txt")
        print("Logged out successfully.")
    else:
        print("You dont have any account. Log in first")