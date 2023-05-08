from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET="some default string value"  

settings = Settings()