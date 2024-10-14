from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import Annotated
from src.auth.hash_password import compare_hash_password
from src.repository.db_repo.service.user_service.user_service import user_service


route = APIRouter(
    tags=['Log_in_out']
)

class UserLogin(BaseModel):
    username: str
    password: str

async def user_exists(user: UserLogin) -> UserLogin:
    username = {'username': user.username}
    check_exist = await user_service.select_user(username)
    if check_exist:
        user = user.model_dump()
        user['hash_password'] = check_exist.hash_password
        user['id'] = check_exist.id
        user['salt'] = check_exist.salt
        return user
    else: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not exists",
        )
    
@route.post("/login")
async def login(
    user_data: Annotated[dict, Depends(user_exists)],
) -> JSONResponse:
    if not compare_hash_password(user_data['password'], user_data['salt'], user_data['hash_password']):
        return JSONResponse(content = {'response': 'error password'}, status_code = 401)
    response = JSONResponse(
        content = {}, 
            status_code = 200
        )
    return response

@route.post("/logout")
async def logout() -> JSONResponse:
    response = JSONResponse(content = {'response': 'User logout!'}, status_code = 200)
    return response