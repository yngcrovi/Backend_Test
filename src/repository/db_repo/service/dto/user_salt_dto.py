from pydantic import BaseModel

class UserSaltGetDTO(BaseModel):
    salt: bytes