from pydantic import BaseModel

class JWT(BaseModel):
    token : str

class Eror(BaseModel):
    error : str

