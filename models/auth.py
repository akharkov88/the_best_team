from pydantic import BaseModel


class BaseUser(BaseModel):
    # email: str
    username: str

class UserRoles(BaseUser):
    name: str
    surname: str

class UserCreate(UserRoles):
    password: str






class User(BaseUser):
    id: int
    name: str
    surname: str

    class Config:
        orm_mode = True

class UserCreate2(BaseModel):
    id: int
    name: str
    surname: str
    password: str
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
class Username(BaseModel):
    username: str
