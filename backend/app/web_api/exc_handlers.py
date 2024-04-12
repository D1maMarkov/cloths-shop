from domain.brand.exc import BrandNotFound, BrandsImageNotFound
from domain.category.exc import CategoryNotFound
from domain.product.exc import (
    ProductAlreadyExist,
    ProductNotFound,
    ProductsImageNotFound,
    ProductsNotFound,
)
from domain.user.exc import (
    UserByIdNotFound,
    UserNotFound,
    UserWithEmailAlreadyExist,
    UserWithUsernameAlreadyExist,
)
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


async def product_not_found_exc_handler(request: Request, exc: ProductNotFound) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": exc.message})


async def category_not_found_exc_handler(request: Request, exc: CategoryNotFound) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": exc.message})


async def product_image_not_found_exc_handler(request: Request, exc: ProductsImageNotFound) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": exc.message})


async def product_already_exist_exc_handler(request: Request, exc: ProductAlreadyExist) -> JSONResponse:
    return JSONResponse(status_code=409, content={"detail": exc.message})


async def products_not_found_exc_handler(request: Request, exc: ProductsNotFound) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": exc.message})


async def user_not_found_exc_handler(request: Request, exc: UserNotFound) -> JSONResponse:
    return JSONResponse(status_code=401, content={"detail": exc.message})


async def user_by_id_not_found_exc_handler(request: Request, exc: UserByIdNotFound) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": exc.message})


async def user_with_email_already_exist_exc_handler(request: Request, exc: UserWithEmailAlreadyExist) -> JSONResponse:
    return JSONResponse(status_code=409, content={"detail": exc.message})


async def user_with_username_already_exist_exc_handler(
    request: Request, exc: UserWithUsernameAlreadyExist
) -> JSONResponse:
    return JSONResponse(status_code=409, content={"detail": exc.message})


async def brand_not_found_exc_handler(request: Request, exc: BrandNotFound) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": exc.message})


async def brands_image_not_found_exc_handler(request: Request, exc: BrandsImageNotFound) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": exc.message})


def init_exc_handlers(app: FastAPI) -> None:
    app.add_exception_handler(ProductNotFound, product_not_found_exc_handler)
    app.add_exception_handler(ProductsNotFound, products_not_found_exc_handler)
    app.add_exception_handler(CategoryNotFound, category_not_found_exc_handler)
    app.add_exception_handler(ProductsImageNotFound, product_image_not_found_exc_handler)
    app.add_exception_handler(ProductAlreadyExist, product_already_exist_exc_handler)
    app.add_exception_handler(UserNotFound, user_not_found_exc_handler)
    app.add_exception_handler(UserByIdNotFound, user_by_id_not_found_exc_handler)
    app.add_exception_handler(UserWithEmailAlreadyExist, user_with_email_already_exist_exc_handler)
    app.add_exception_handler(UserWithUsernameAlreadyExist, user_with_username_already_exist_exc_handler)
    app.add_exception_handler(BrandNotFound, brand_not_found_exc_handler)
    app.add_exception_handler(BrandsImageNotFound, brands_image_not_found_exc_handler)
