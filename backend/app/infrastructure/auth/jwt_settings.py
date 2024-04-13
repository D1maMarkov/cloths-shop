import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class JwtSettings(BaseSettings):
    secret_key: str = os.getenv("SECRET_KEY")
    algorithm: str = os.getenv("ALGORITHM")
    expires_in: int = os.getenv("EXPIRES_IN")

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_jwt_settings() -> JwtSettings:
    return JwtSettings()
