from routes.categories import router as categories_router
from routes.products import router as products_router
from routes.brands import router as brands_router
from routes.cart import router as cart_router
from routes.favs import router as favs_router
from routes.user import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database import create_tables, delete_tables
from contextlib import asynccontextmanager
from starlette.middleware.sessions import SessionMiddleware
from settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    #await delete_tables()
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
    allow_headers=["Access-Control-Allow-Headers", 'Set-Cookie' 'Content-Type', 'Authorization', 'Access-Control-Allow-Origin'],
)

app.include_router(router=user_router)
app.include_router(router=categories_router)
app.include_router(router=products_router)
app.include_router(router=brands_router)
app.include_router(router=cart_router)
app.include_router(router=favs_router)

