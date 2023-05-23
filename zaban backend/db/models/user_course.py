from sqlalchemy import Column,Integer, String , Boolean , ForeignKey
from ..db_setup import Base
from sqlalchemy.orm import relationship


class UserCourse(Base):
    __tablename__ = "user_course"

    id = Column(Integer, primary_key=True, autoincrement= True)
    user_id = Column(Integer, ForeignKey('users.id') , nullable=False , ) 
    course_id = Column(Integer, ForeignKey('course.id') , nullable=False , ) 

    course_user = relationship('User' , back_populates='user_courses')
    course_courses = relationship('Course' , back_populates='courses_course')