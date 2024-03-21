from schemas.common import SBaseDataField, SBaseDataFieldAdd, SFiltered, SSearch
from repositories.additional_for_products import AdditionalForProductSRepository
from schemas.products import SProduct, SProductAdd, SBaseDataField
from fastapi import APIRouter, Depends, Query, UploadFile
from repositories.products import ProductRepository
from typing import Annotated
from enums import sizes


router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.post("/get-filtered")
async def get_products(data: SFiltered) -> list[SProduct]:
    products = await ProductRepository.get_filtered_products(data)
    return products

@router.post("/search")
async def get_searched_products(data: SSearch) -> list[SProduct]:
    products = await ProductRepository.get_searched_products(data.search)
    return products

@router.get("/product/{id}")
async def get_product(id: int) -> SProduct:
    product = await ProductRepository.get_product(id)
    return product

@router.post("/")
async def add_product(
    product: Annotated[SProductAdd, Depends()]
):
    product_id = await ProductRepository.add_one_product(product)
    return {"ok": True, "product_id": product_id}

@router.post("/upload")
async def upload(
    product_id: int,
    image: UploadFile
):
    image_response = await ProductRepository.add_image(product_id=product_id, file=image)
    return image_response

@router.get("/image/{image_id}")
async def show_image(image_id: int):
    image = await ProductRepository.get_image(image_id=image_id)
    return image

@router.get("/images")
async def show_images():
    images = await ProductRepository.get_all_images()
    return images

@router.post("/size")
async def add_size(product_id: int, size: str = Query(enum=sizes)):
    size = await AdditionalForProductSRepository.add_size(product_id=product_id, size=size)
    return size

@router.get("/sizes")
async def get_sizes() -> list[SBaseDataField]:
    sizes = await AdditionalForProductSRepository.get_sizes()
    return sizes

@router.post("/color")
async def add_color(
    color: Annotated[SBaseDataFieldAdd, Depends()]
):
    color = await AdditionalForProductSRepository.add_color(color)
    return color

@router.get("/colors")
async def get_colors():
    colors = await AdditionalForProductSRepository.get_colors()
    return colors

@router.get("/populars")
async def get_populars():
    products = await ProductRepository.get_populars()
    return products

@router.get("/new-arrivals")
async def get_new_arrivals():
    products = await ProductRepository.get_new_arrivals()
    return products

@router.get("/price-range")
async def get_price_range() -> list[int]:
    range = await ProductRepository.get_price_range()
    return range

@router.get("/product-colors/{name}")
async def get_colors(name) -> list[SProduct]:
    products = await ProductRepository.get_colors(name=name)
    return products

'''@router.get("/allimages")
async def get_all_images():
    images = await ProductRepository.get_all_images()
    return images
'''