from sqlalchemy import Column,Integer, String , Boolean , Float
from ..db_setup import Base
from sqlalchemy.orm import relationship


from db.models.user_course import UserCourse

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, autoincrement= True)
    name = Column(String(100), nullable=False)
    language = Column(String(45), nullable=False)
    course_lenght = Column(String(45), nullable=False)
    course_capacity = Column(Integer, nullable=False)
    is_special =  Column(Boolean , nullable=False)    
    level = Column(String(45)) 
    level_number = Column(Integer) 
    start_date = Column(String(45))
    price = Column(Float ,nullable=False )

    users  = relationship('UserCourse' , back_populates='courses')