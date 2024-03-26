from contextlib import asynccontextmanager

from database import create_tables, delete_tables

# from database import delete_tables
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.brands_route import router as brands_router
from routes.cart_route import router as cart_router
from routes.categories_router import router as categories_router
from routes.favs_route import router as favs_router
from routes.products_route import router as products_router
from routes.user import router as user_router
from settings import settings
from starlette.middleware.sessions import SessionMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(SessionMiddleware, secret_key=settings.SESSION_SECRET_KEY)

origins = ["http://127.0.0.1:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=[
        "Access-Control-Allow-Headers",
        "Set-Cookie" "Content-Type",
        "Authorization",
        "Access-Control-Allow-Origin",
    ],
)

app.include_router(router=user_router)
app.include_router(router=categories_router)
app.include_router(router=products_router)
app.include_router(router=brands_router)
app.include_router(router=cart_router)
app.include_router(router=favs_router)
