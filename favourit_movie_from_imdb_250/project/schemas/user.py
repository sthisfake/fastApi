from datetime import datetime

from pydantic import BaseModel


class UserBaseLogin(BaseModel):
    email_or_username: str
    password: int

class UserBaseSignUp(BaseModel):
    full_name: str
    email: str    
    user_name : str
    password : str


class UserLogin(UserBaseLogin):
    ...

class UserSignUp(UserBaseSignUp):
    ...



class User(UserBaseSignUp):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
