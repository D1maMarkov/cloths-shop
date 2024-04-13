from typing import Annotated

from application.contracts.products.add_product_request import AddProductRequest
from application.contracts.products.filter_products_request import FilterProductsRequest
from application.contracts.products.price_range_response import PriceRangeResponse
from application.contracts.products.search_products_request import SearchProductsRequest
from application.usecases.product.add_product import AddProduct
from application.usecases.product.get_prices import GetProductsPrices
from application.usecases.product.get_products import (
    GetFilteredProducts,
    GetNewArrivals,
    GetPopulars,
    GetProductById,
    GetProductsColors,
    GetSearchedProducts,
)
from application.usecases.product.products_image import (
    AddProductsImage,
    GetProductsImage,
)
from domain.product.product import CatalogProduct, Product
from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import FileResponse
from web_api.depends.product.add_product import get_add_product_interactor
from web_api.depends.product.get_prices import get_price_range_interactor
from web_api.depends.product.get_products import (
    get_filtered_interactor,
    get_find_product_interactor,
    get_find_products_colors_interactor,
    get_new_arrivals_interactor,
    get_populars_interactor,
    get_searched_interactor,
)
from web_api.depends.product.products_image import (
    get_add_products_image_interactor,
    get_show_products_image_interactor,
)

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/get-filtered", response_model=list[CatalogProduct])
async def get_products(
    data: FilterProductsRequest, get_filtered_interactor: GetFilteredProducts = Depends(get_filtered_interactor)
) -> list[CatalogProduct]:
    return await get_filtered_interactor(data)


@router.post("/search", response_model=list[CatalogProduct])
async def get_searched_products(
    data: SearchProductsRequest, get_searched_interactor: GetSearchedProducts = Depends(get_searched_interactor)
) -> list[CatalogProduct]:
    return await get_searched_interactor(data.search)


@router.get("/product/{id}", response_model=Product)
async def get_product(
    id: int, get_find_product_interactor: GetProductById = Depends(get_find_product_interactor)
) -> Product:
    return await get_find_product_interactor(id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_product(
    product: Annotated[AddProductRequest, Depends()],
    add_product_interactor: AddProduct = Depends(get_add_product_interactor),
) -> None:
    return await add_product_interactor(product)


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload(
    product_id: int,
    image: UploadFile,
    add_products_image_interactor: AddProductsImage = Depends(get_add_products_image_interactor),
) -> str:
    return await add_products_image_interactor(product_id=product_id, file=image)


@router.get("/image/{image_id}")
async def show_image(
    image_id: int, show_image_interactor: GetProductsImage = Depends(get_show_products_image_interactor)
) -> FileResponse:
    return await show_image_interactor(image_id)


@router.get("/populars", response_model=list[CatalogProduct])
async def get_populars(populars_interactor: GetPopulars = Depends(get_populars_interactor)) -> list[CatalogProduct]:
    return await populars_interactor()


@router.get("/new-arrivals", response_model=list[CatalogProduct])
async def get_new_arrivals(
    new_arrivals_interactor: GetNewArrivals = Depends(get_new_arrivals_interactor),
) -> list[CatalogProduct]:
    return await new_arrivals_interactor()


@router.get("/price-range", response_model=PriceRangeResponse)
async def get_price_range(
    price_range_interactor: GetProductsPrices = Depends(get_price_range_interactor),
) -> PriceRangeResponse:
    return await price_range_interactor()


@router.get("/product-colors/{name}", response_model=list[CatalogProduct])
async def get_product_colors(
    name: str, get_products_colors_interactor: GetProductsColors = Depends(get_find_products_colors_interactor)
) -> list[CatalogProduct]:
    return await get_products_colors_interactor(name)
