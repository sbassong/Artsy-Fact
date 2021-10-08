import bcrypt
import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv('APP_SECRET')

#accepts a payload which contains secret info
def create_token(payload):
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

#checks if the token is valid and decode it back to it's raw values
def read_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.InvalidSignatureError:
        return "Signature Invalid"
    except jwt.InvalidTokenError:
        return "Token Invalid"


#handles hashing password
def gen_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

#compares password on login?
def compare_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

#accepts one argument of req (flask request object), reads the token from the request headers
def strip_token(req):
    try:
        token = req.headers['Authorization'].split(' ')[1]
        return token
    except:
        return None
