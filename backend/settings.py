import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    SESSION_SECRET_KEY = os.getenv("SESSION_SECRET_KEY")

    PRODUCTS_PATH = "static/products/"
    BRANDS_PATH = "static/brands/"

    HOST = "http://127.0.0.1:8000"
