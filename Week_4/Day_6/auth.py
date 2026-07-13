import jwt
import datetime

SECRET_KEY = "My_Super_Secret_Key_123"

def create_token(username):
    
    payload = {
        "username": username,
        "role": "Student",
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5)
    }
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )
    return token

def verify_token(token):
    decode = jwt.decode(
        token,
        SECRET_KEY,
        algorithms= ["HS256"]
    )
    return decode