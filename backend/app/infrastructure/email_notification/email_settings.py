import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class EmailSettings(BaseSettings):
    backend_email: str = os.getenv("BACKEND_EMAIL")
    backend_email_password: str = os.getenv("BACKEND_EMAIL_PASSWORD")
    port: int = os.getenv("PORT")

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_email_settings():
    return EmailSettings()
