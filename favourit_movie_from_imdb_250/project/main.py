from fastapi import FastAPI

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