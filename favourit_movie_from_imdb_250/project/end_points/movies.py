import fastapi
from fastapi import Depends
from typing import List
from schemas.movie import Movie
from sqlalchemy.orm import Session
from db.db_setup import   get_db
from end_points.controllers.movies import get_movies , get_movie_id

router = fastapi.APIRouter()

@router.get("/movies" , response_model=List[Movie])
async def get_all_movies(db: Session = Depends(get_db)):
    all_movies = get_movies(db)
    return all_movies

@router.get("/movie/{id}" , response_model= Movie)
async def get_movie_by_id(id : int , db : Session = Depends(get_db)):
    movie = get_movie_id(db , id)
    return movie

