from sqlalchemy import Column,Integer, String , Text
from ..db_setup import Base
from sqlalchemy.orm import relationship





class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement= True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(45), unique=True,  nullable=False)
    password =  Column(String(100), unique=True, nullable=False)

    user_courses = relationship('UserCourse' , back_populates='course_user')