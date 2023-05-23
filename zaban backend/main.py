from fastapi import FastAPI
from api import users

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


app.include_router(users.router)