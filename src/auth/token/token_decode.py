from jose import JWTError, jwt
from data_for_token import SECRET_KEY, ALGORITHM

def decode_token(token: str) -> dict | bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return False   