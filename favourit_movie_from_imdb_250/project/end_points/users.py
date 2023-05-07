import fastapi
from fastapi import Depends
from typing import List
from schemas.user import User , UserSignUp
from sqlalchemy.orm import Session
from db.db_setup import   get_db
from end_points.controllers.users import get_users , create_user



router = fastapi.APIRouter()

@router.get("/users" , response_model=List[User])
async def get_all_users( db: Session = Depends(get_db)):
    all_users = get_users(db)
    return all_users

@router.post("/users" , response_model=User , status_code=201)
async def create_new_user(user: UserSignUp , db: Session = Depends(get_db)):
    return create_user(db=db, user=user)     



    