from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from repository.db_repo.service.user_service.user_service import user_service
from repository.db_repo.service.user_service.user_salt_service import user_salt_service
from .hash_password import make_hash_password


route = APIRouter(
    prefix='/registration',
    tags=['Registration']
)

class UserRegistration(BaseModel):
    username: str
    password: str

async def user_exists(user: UserRegistration):
    username = {'username': user.username}
    check_exist = await user_service.select_user(username)
    if check_exist:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User exists",
        )
    else: 
        return user.model_dump()

@route.post("")
async def registration(
    user_data: Annotated[dict, Depends(user_exists)],
) -> JSONResponse:
    key_salt = make_hash_password(user_data['password'])
    user_data['hash_password'] = key_salt['key']
    del user_data['password']
    id_username = await user_service.insert_user(user_data)
    salt_data = {
        'id_username': id_username,
        'salt': key_salt['salt']
    }
    await user_salt_service.insert_salt(salt_data)
    user_data['id'] = id_username
    response = JSONResponse(
            content={},
            status_code = 200
            )
    return response