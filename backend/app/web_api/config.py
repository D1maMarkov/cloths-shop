import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    SESSION_SECRET_KEY: str = os.getenv("SESSION_SECRET_KEY")

    HOST: str = "http://127.0.0.1:8000"

    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL")

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()
