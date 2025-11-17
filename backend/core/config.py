from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Dashboard-Automacao"
    RD_ACCESS_TOKEN: str
    RD_CRM_TOKEN: str

    class Config:
        env_file = ".env"

settings = Settings()
settings.RD_ACCESS_TOKEN = settings.RD_ACCESS_TOKEN.strip()
settings.RD_CRM_TOKEN = settings.RD_CRM_TOKEN.strip()