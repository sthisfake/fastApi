from sqlalchemy.orm import Session
# from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserSignUp , UserLogin
from schemas.jwt import JWT , Eror
from schemas.movie import Movie

from db.models.user import User
from db.models.movie import FavouritMovie
from db.models.movie import Movie

import bcrypt
import jwt
import datetime
import os

from schemas.setting import settings
from validate_email import validate_email  
from fastapi import HTTPException

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

    #check the validatation of email 
    is_valid = validate_email(user.email)  

    if is_valid == False :
        raise HTTPException(status_code = 406, detail=  "email is not valid")

    # check if the uesr exist first 

    check = db.query(User).filter(User.email == user.email ).first()

    if check != None :
        raise HTTPException(status_code = 403, detail=  "user already exists")

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

def new_login(db: Session, user: UserLogin):

    # check if the uesr exist first 
    is_email  = validate_email(user.email_or_username)

    if is_email :
        original_user = db.query(User).filter(User.email == user.email_or_username ).first()

    else :
        original_user = db.query(User).filter(User.userName == user.email_or_username ).first()


    if original_user != None :
        passwordEnterd = user.password
        passwordEnterd = passwordEnterd.encode('utf-8')
        real_hash_password = original_user.password
        real_hash_password = real_hash_password.encode('utf-8')

        result = bcrypt.checkpw(passwordEnterd , real_hash_password)

        if result:
            
            # create the jwt token 

            # exp with 1 hour from current time
            payload = {"sub": original_user.id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}

            #generate the token
            token = jwt.encode(payload, settings.SECRET , algorithm="HS256")

            jwt_token_string = JWT(token = token)
            return jwt_token_string
        
        else :
            raise HTTPException(status_code = 401, detail=  "email or password is wrong")
        
    else :
        raise HTTPException(status_code = 404, detail=  "user doesnt exist")

def get_user(db: Session, id: int):
    
    user = db.query(User).filter(User.id == id).first()

    if user == None :
        raise HTTPException(status_code = 404, detail=  "user doesnt exist")

    else:
        return user

def add_to_fav(db: Session, movie : Movie , id : int):

    user = db.query(User).filter(User.id == id).first()
    if user == None :
        raise HTTPException(status_code = 404, detail=  "user doesnt exist")
    
    
    db_movie = db.query(Movie).filter(Movie.id == movie.id).first()
    if db_movie == None :
        raise HTTPException(status_code = 404, detail=  "movie doesnt exist")



    movie_id = movie.id
    new_fav = FavouritMovie(user_id = id , movie_id = movie_id )
    db.add(new_fav)
    db.commit()
    db.refresh(new_fav)

    return {"massage" : "movie added to fav list"}

def user_fav(db :Session , id :int ):
    
    user = db.query(User).filter(User.id == id).first()
    if user == None :
        raise HTTPException(status_code = 404, detail=  "user doesnt exist")
    
    liked_movies = db.query(Movie).join(FavouritMovie).filter(FavouritMovie.user_id == id).all()
    return liked_movies
        

