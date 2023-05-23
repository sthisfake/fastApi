from pydantic import BaseModel

class Course(BaseModel):
    id : int
    name : str
    language : str
    course_lenght : str
    course_capacity : str
    is_special : bool
    level : str
    level_number : int
    start_date : str


    class config:
        orm_mode = True   