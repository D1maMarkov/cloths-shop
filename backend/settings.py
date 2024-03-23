from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os


load_dotenv()

class Settings(BaseSettings):
    SECRET_KEY : str = os.getenv("SECRET_KEY")
    ALGORITHM : str = os.getenv("ALGORITHM")
    SESSION_SECRET_KEY : str = os.getenv("SESSION_SECRET_KEY")
    DATABASE_URL : str = os.getenv("DATABASE_URL")

    PRODUCTS_PATH : str = "static/products/"
    BRANDS_PATH : str = "static/brands/"

    HOST : str = "http://127.0.0.1:8000"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()