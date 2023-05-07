from sqlalchemy.orm import Session
# from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserSignUp

from db.models.user import User

import bcrypt


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