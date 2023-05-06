from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from .mixins import Timestamp
from ..db_setup import Base

class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    userName = Column(String(100), unique=True, index=True, nullable=False)
    password =  Column(Text, unique=True, index=True, nullable=False)

    fav_movies = relationship("favourit_movies", back_populates="like_by", uselist=True)
