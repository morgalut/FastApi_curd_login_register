"""
This module configures the application settings using Pydantic's BaseSettings.
It also loads environment variables from a .env file if present.
"""

import os  # Standard import before third-party imports
from pydantic_settings import BaseSettings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings(BaseSettings):
    """
    Settings class that loads environment variables or default settings.
    Defines the DATABASE_URL for SQLite.
    """
    DATABASE_URL: str = f"sqlite:///{os.path.join(BASE_DIR, '../tasks.db')}"
    
    class Config:
        """
        Configuration class for Settings.
        Specifies that environment variables are loaded from the .env file.
        """
        env_file = ".env"

settings = Settings()
