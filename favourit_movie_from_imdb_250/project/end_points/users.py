import fastapi
from fastapi import Depends , HTTPException
from typing import List
from schemas.user import User , UserSignUp , UserLogin
from sqlalchemy.orm import Session
from db.db_setup import   get_db
from end_points.controllers.users import get_users , get_user ,new_sign_up , new_login , add_to_fav , user_fav
from schemas.movie import Movie



router = fastapi.APIRouter()

@router.get("/users" , response_model=List[User])
async def get_all_users( db: Session = Depends(get_db)):
    all_users = get_users(db)
    return all_users



@router.post("/signup"  , status_code = 201)
async def sign_up(user: UserSignUp , db: Session = Depends(get_db)):
    return new_sign_up(db=db, user=user)

@router.post("/login"  , status_code = 200)
async def login(user: UserLogin , db: Session = Depends(get_db)):
    return new_login(db=db, user=user)

@router.get("/user/{id}" , status_code=200)
async def get_user_info(id : int  , db: Session = Depends(get_db)):
    return get_user(id= id , db = db)

@router.post("/user/{id}/fav" , status_code=201)
async def new_fav_movie(id : int , movie : Movie ,  db: Session = Depends(get_db)):
    return add_to_fav(movie = movie , db = db , id = id)

@router.get("/user/{id}/fav" , status_code=200)
async def all_fav_movie(id : int ,db: Session = Depends(get_db) ):
    return user_fav(id = id , db = db )

    