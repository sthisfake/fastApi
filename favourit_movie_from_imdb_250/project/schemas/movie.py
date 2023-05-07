from datetime import datetime

from pydantic import BaseModel

class Movie(BaseModel):
    id : int 
    title : str 
    year : str
    plot : str
    rank : int
    poster : str 
    director : str
    actors : str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
