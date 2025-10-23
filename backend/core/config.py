from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str 
    RD_ACCESS_TOKEN: str 

    class Config:
        env_file = ".env"

settings = Settings()
