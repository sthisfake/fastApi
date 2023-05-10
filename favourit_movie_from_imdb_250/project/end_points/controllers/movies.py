from sqlalchemy.orm import Session
from db.models.movie import Movie
from fastapi import HTTPException

def get_movies(db: Session):
    return db.query(Movie).offset(0).limit(100).all()

def get_movie_id(db : Session , id : int):
    movie =  db.query(Movie).filter(Movie.rank == id).first()

    if movie == None :
        raise HTTPException(status_code = 404, detail=  "movie doesnt exist")
    
    else : 
        return movie