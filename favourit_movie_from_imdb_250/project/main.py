from fastapi import FastAPI

from end_points import users
from end_points import movies

app = FastAPI(
    title="Fast API Backend",
    description="backend for small movie app.",
    version="0.0.1",
    contact={
        "name": "pouya",
        "email": "pouya.teimoury@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)


app.include_router(users.router)
app.include_router(movies.router)