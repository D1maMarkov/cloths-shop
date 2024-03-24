from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile
from repositories.additional_for_products_repository import (
    AdditionalForProductSRepository,
)
from repositories.products_repository import ProductRepository
from schemas.common import SBaseDataField, SBaseDataFieldAdd, SFiltered, SSearch
from schemas.products import SProduct, SProductAdd, SSize
from services.additional_for_products_service import AdditionalForProductService
from services.products_service import ProductService

router = APIRouter(prefix="/products", tags=["products"])

product_repository = ProductRepository()
product_service = ProductService(product_repository)


def get_product_service():
    return product_service


product_service_dependency = Annotated[dict, Depends(get_product_service)]


additional_repository = AdditionalForProductSRepository()
additional_service = AdditionalForProductService(additional_repository)


def get_additional_service():
    return additional_service


additional_service_dependency = Annotated[dict, Depends(get_additional_service)]


@router.post("/get-filtered")
async def get_products(data: SFiltered, service: product_service_dependency) -> list[SProduct]:
    products = await service.get_filtered_products(data)
    return products


@router.post("/search")
async def get_searched_products(data: SSearch, service: product_service_dependency) -> list[SProduct]:
    products = await service.get_searched_products(data.search)
    return products


@router.get("/product/{id}")
async def get_product(id: int, service: product_service_dependency) -> SProduct:
    product = await service.get_product(id)
    return product


@router.post("/", status_code=201)
async def add_product(product: Annotated[SProductAdd, Depends()], service: product_service_dependency):
    product_id = await service.add_one_product(product)
    return {"ok": True, "product_id": product_id}


@router.post("/upload", status_code=201)
async def upload(product_id: int, image: UploadFile, service: product_service_dependency):
    image_response = await service.add_image(product_id=product_id, file=image)
    return image_response


@router.get("/image/{image_id}")
async def show_image(image_id: int, service: product_service_dependency):
    image = await service.get_image(image_id=image_id)
    return image


@router.post("/size", status_code=201)
async def add_size(size: Annotated[SSize, Depends()], service: additional_service_dependency):
    size = await service.add_size(size)
    return size


@router.get("/sizes")
async def get_sizes(service: additional_service_dependency) -> list[SBaseDataField]:
    sizes = await service.get_sizes()
    return sizes


@router.post("/color", status_code=201)
async def add_color(color: Annotated[SBaseDataFieldAdd, Depends()], service: additional_service_dependency):
    color = await service.add_color(color)
    return color


@router.get("/colors")
async def get_colors(service: additional_service_dependency) -> list[SBaseDataField]:
    colors = await service.get_colors()
    return colors


@router.get("/populars")
async def get_populars(service: product_service_dependency):
    products = await service.get_populars()
    return products


@router.get("/new-arrivals")
async def get_new_arrivals(service: product_service_dependency):
    products = await service.get_new_arrivals()
    return products


@router.get("/price-range")
async def get_price_range(service: product_service_dependency) -> list[int]:
    range = await service.get_price_range()
    return range


@router.get("/product-colors/{name}")
async def get_product_colors(name: str, service: product_service_dependency) -> list[SProduct]:
    products = await service.get_colors(name=name)
    return products


"""@router.get("/allimages")
async def get_all_images():
    images = await ProductRepository.get_all_images()
    return images
"""
