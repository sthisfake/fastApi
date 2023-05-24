import fastapi
from fastapi import Depends , HTTPException
from sqlalchemy.orm import Session
from db.db_setup import get_db
from schemas.user import UserSignUp , UserReturn , UserLogin
from schemas.course import Course as doros
from db.models.user import User
from db.models.course import Course
from typing import List

from validate_email import validate_email  
import bcrypt

router = fastapi.APIRouter()

@router.post("/signup", response_model=UserReturn ,  status_code=201)
async def sign_up(user: UserSignUp , db: Session = Depends(get_db)):

    #check the validatation of email 
    is_valid = validate_email(user.email)  

    if is_valid == False :
        raise HTTPException(status_code = 406, detail=  "email is not valid")

    # check if the uesr exist first 

    check = db.query(User).filter(User.email == user.email ).first()

    if check != None :
        raise HTTPException(status_code = 403, detail=  "user already exists")
    
    #check the password lenght 

    password_lenght = len(user.password)
    if(password_lenght < 5):
        raise HTTPException(status_code = 403, detail=  "password lenghth is less than 5")

    #hash the password first
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), salt)
    hashed_password = hashed_password.decode('utf-8')

    #add the user to database
    db_user = User(first_name = user.firstname , last_name = user.lastname , email = user.email , password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    userReturn = UserReturn(id = db_user.id ,  firstname=db_user.first_name , lastname=db_user.last_name , email=db_user.email )
    return userReturn
    

@router.post("/login", response_model=UserReturn ,  status_code=200)    
async def login(user: UserLogin , db: Session = Depends(get_db)):

    # check if the uesr exist first 
    original_user = db.query(User).filter(User.email == user.email ).first()

    if original_user != None :
        passwordEnterd = user.password
        passwordEnterd = passwordEnterd.encode('utf-8')
        real_hash_password = original_user.password
        real_hash_password = real_hash_password.encode('utf-8')

        result = bcrypt.checkpw(passwordEnterd , real_hash_password)

        if result:
            userReturn = UserReturn(id = original_user.id ,  firstname=original_user.first_name ,
                                     lastname=original_user.last_name , email=original_user.email )
            return userReturn
        
        else :
            raise HTTPException(status_code = 401, detail=  "email or password is wrong")
        
    else :
        raise HTTPException(status_code = 404, detail=  "user doesnt exist")
    

