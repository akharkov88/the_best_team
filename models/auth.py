from pydantic import BaseModel


class BaseUser(BaseModel):
    # email: str
    username: str

class UserRoles(BaseUser):
    roles: str

class UserCreate(UserRoles):
    password: str






class User(BaseUser):
    id: int
    roles: str

    class Config:
        orm_mode = True

class UserCreate2(BaseModel):
    id: int
    roles: str
    password: str
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
class Username(BaseModel):
    username: str
