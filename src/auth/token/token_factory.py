import time
from jose import jwt
from .data_for_token import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_SECOND

def create_token(data: dict, time_expires: float) -> str:
    data.update({"exp": time_expires})
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_access_token(token_data: dict) -> str:
    access_token_expires = time.time() + ACCESS_TOKEN_EXPIRE_SECOND
    access_token = create_token(data={'id': token_data['id'], 'username': token_data['username']}, time_expires=access_token_expires)
    return access_token

def get_access_token(user_data: dict) -> str:
    token = create_access_token(user_data)
    return token

