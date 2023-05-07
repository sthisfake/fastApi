from sqlalchemy.orm import Session
from db.models.movie import Movie

def get_movies(db: Session):
    return db.query(Movie).offset(0).limit(100).all()

def get_movie_id(db : Session , id : int):
    return db.query(Movie).filter(Movie.rank == id).first()