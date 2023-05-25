import fastapi
from fastapi import Depends , HTTPException
from sqlalchemy.orm import Session
from db.db_setup import get_db
from schemas.course import Course as doros
from db.models.course import Course
from db.models.user import User
from typing import List
from db.models.user_course import UserCourse
from schemas.course import CourseUserInsert


router = fastapi.APIRouter()

@router.get("/courses", response_model= List[doros] ,  status_code=200) 
async def courses( db: Session = Depends(get_db)):

    CourseReturn = []

    #get all the courses 
    courses = db.query(Course).offset(0).all()

    #map to the pydantic model
    for course in courses :
        item = doros(id= course.id  , name = course.name , language=course.language ,
                     course_lenght= course.language , course_capacity= course.course_capacity , 
                     is_special=course.is_special , level=course.level , level_number=course.level_number,
                     start_date=course.start_date , price=course.price)
        
        CourseReturn.append(item)


    return CourseReturn


@router.get("/course/{id}" , response_model=doros , status_code=200)
async def get_course(id : int ,db:Session = Depends(get_db)):

    #get the requested course 

    course  = db.query(Course).filter(Course.id == id).first()

    if course != None :
        course_return = doros(id= course.id  , name = course.name , language=course.language ,
                     course_lenght= course.language , course_capacity= course.course_capacity , 
                     is_special=course.is_special , level=course.level , level_number=course.level_number,
                     start_date=course.start_date)
        
        return course_return
    
    else : 
        raise HTTPException(status_code = 404, detail=  "course doesnt exist") 


@router.post("/insert"  , status_code=201 )
async def insert_user_course( courseInsert :CourseUserInsert , db:Session = Depends(get_db)):

    course  = db.query(Course).filter(Course.id == courseInsert.course_id).first()
    user = db.query(User).filter(User.id == courseInsert.user_id).first()

    if course != None:

        if user != None:

            is_already_insert = db.query(UserCourse).filter(UserCourse.user_id == courseInsert.user_id and UserCourse.course_id == courseInsert.course_id )

            if is_already_insert == None :

                user_course = UserCourse(phone_number_related = courseInsert.phone_number , user_id =courseInsert.user_id , 
                                        course_id = courseInsert.course_id )
                
                db.add(user_course)
                db.commit()
                db.refresh(user_course)

                db.query(Course).filter(Course.id == courseInsert.course_id ).update({'course_capacity' : Course.course_capacity -1 })
                db.commit()

                return {"massage" : "succecfully inserted"}
            
            else :
                raise HTTPException(status_code = 403, detail=  "user already enrolled in course")

        
        else :
            raise HTTPException(status_code = 404, detail=  "user doesnt exist")  

    
    else:
        raise HTTPException(status_code = 404, detail=  "course or user doesnt exist")  

        

