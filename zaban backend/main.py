from fastapi import FastAPI
from api import users , course
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="backend for zaban project",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Gwen",
        "email": "gwen@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to a list of allowed origins or specific domains
    allow_methods=["*"],  # Set this to a list of allowed HTTP methods
    allow_headers=["*"],  # Set this to a list of allowed HTTP headers
)



app.include_router(users.router)
app.include_router(course.router)