import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class ProductSettings(BaseSettings):
    PRODUCTS_PATH: str = os.getenv("PRODUCTS_PATH")

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return ProductSettings()
