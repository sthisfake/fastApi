from sqlalchemy.orm import Session
# from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserSignUp
from schemas.jwt import JWT

from db.models.user import User

import bcrypt
import jwt
import datetime
import os

from schemas.setting import settings

def get_users(db: Session ):
    return db.query(User).offset(0).limit(100).all()

def create_user(db: Session, user: UserSignUp):

    #hash the password first
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), salt)
    hashed_password = hashed_password.decode('utf-8')

    db_user = User(full_name = user.full_name , email = user.email , userName = user.userName , password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def new_sign_up(db: Session, user: UserSignUp):

    #TODO: check if the uesr exist first 
    db.query(User).filter(User.email == user.email )

    #hash the password first
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), salt)
    hashed_password = hashed_password.decode('utf-8')

    db_user = User(full_name = user.full_name , email = user.email , userName = user.userName , password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # create the jwt token 

    # exp with 1 hour from current time
    payload = {"sub": db_user.id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}

    #generate the token
    token = jwt.encode(payload, settings.SECRET , algorithm="HS256")

    jwt_token_string = JWT(token = token)
    return jwt_token_string

