from pydantic import BaseModel

class UserPostDTO(BaseModel):
    id: int
    username: str
    hash_password: bytes