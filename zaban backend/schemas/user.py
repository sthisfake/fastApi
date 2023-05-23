from pydantic import BaseModel


class UserBase(BaseModel):
    first_name : str
    last_name : str
    email : str
    password : str


class UserCreated(UserBase):
    ...




class User(UserBase):
    id : int

    class config:
        orm_mode = True      


class UserSignUp(BaseModel):
    firstname : str
    lastname : str
    email  : str
    password : str 


class UserReturn(BaseModel):
    id : str
    firstname : str
    lastname : str
    email : str

class UserLogin(BaseModel):
    email : str
    password : str 
