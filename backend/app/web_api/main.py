from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.persistence.database import create_tables, delete_tables
from starlette.middleware.sessions import SessionMiddleware
from web_api.config import get_settings
from web_api.exc_handlers import init_exc_handlers
from web_api.routers.additional_for_product_router import router as additional_router
from web_api.routers.auth_router import router as auth_router
from web_api.routers.brand_router import router as brands_router
from web_api.routers.cart_router import router as cart_router
from web_api.routers.category_router import router as categories_router
from web_api.routers.favs_router import router as favs_router
from web_api.routers.order_router import router as orders_router
from web_api.routers.product_router import router as products_router
from web_api.routers.user_router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(SessionMiddleware, secret_key=get_settings().SESSION_SECRET_KEY)

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

app.include_router(router=auth_router)
app.include_router(router=user_router)
app.include_router(router=categories_router)
app.include_router(router=products_router)
app.include_router(router=additional_router)
app.include_router(router=brands_router)
app.include_router(router=cart_router)
app.include_router(router=favs_router)
app.include_router(router=orders_router)

init_exc_handlers(app)
