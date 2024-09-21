from pydantic_settings import BaseSettings
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings(BaseSettings):
    DATABASE_URL: str = f"sqlite:///{os.path.join(BASE_DIR, '../tasks.db')}"
    
    class Config:
        env_file = ".env"

settings = Settings()
