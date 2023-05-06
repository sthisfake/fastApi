import fastapi
from fastapi import Depends
from typing import List
from schemas.user import User
from sqlalchemy.orm import Session
from db.db_setup import async_get_db , get_db

router = fastapi.APIRouter()


# @router.get("/users" ,response_model=List[User] )
# async def get_all_users(db: Session = Depends(get_db)):
