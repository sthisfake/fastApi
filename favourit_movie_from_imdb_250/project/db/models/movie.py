from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .mixins import Timestamp
from ..db_setup import Base

class Movie(Timestamp , Base):
    __tablename__ = "movie"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, nullable=False)
    year = Column(String(10), index=True, nullable=False)
    plot = Column(Text, index=True, nullable=False)
    rank =  Column(Integer, unique=True, index=True)
    poster = Column(Text,  index=True)
    director = Column(Text,  index=True , nullable=False)
    actors =  Column(Text,  index=True , nullable=False)

    fav_by_users = relationship("favourit_movies", back_populates="the_movie", uselist=True)



class FavouritMovie(Base):
    __tablename__ = "favourit_movies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer , ForeignKey("users.id") , nullable=False )
    movie_id = Column(Integer , ForeignKey("movie.id")  , nullable=False )

    like_by = relationship("users", back_populates="like_by", uselist=False)
    the_movie = relationship("movie", back_populates="fav_by_users", uselist=False)