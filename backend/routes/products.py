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

product_repository = ProductRepository()

def get_product_repository():
    return product_repository

product_repository_dependency = Annotated[dict, Depends(get_product_repository)]

additional_repository = AdditionalForProductSRepository()

def get_additional_repository():
    return additional_repository

additional_repository_dependency = Annotated[dict, Depends(get_additional_repository)]

def get_additional_repository():
    return additional_repository

@router.post("/get-filtered")
async def get_products(
    data: SFiltered, 
    repository: product_repository_dependency
) -> list[SProduct]:
    products = await repository.get_filtered_products(data)
    return products

@router.post("/search")
async def get_searched_products(
    data: SSearch,
    repository: product_repository_dependency
) -> list[SProduct]:
    products = await repository.get_searched_products(data.search)
    return products

@router.get("/product/{id}")
async def get_product(
    id: int,
    repository: product_repository_dependency
) -> SProduct:
    product = await repository.get_product(id)
    return product

@router.post("/")
async def add_product(
    product: Annotated[SProductAdd, Depends()],
    repository: product_repository_dependency
):
    product_id = await repository.add_one_product(product)
    return {"ok": True, "product_id": product_id}

@router.post("/upload")
async def upload(
    product_id: int,
    image: UploadFile,
    repository: product_repository_dependency
):
    image_response = await repository.add_image(product_id=product_id, file=image)
    return image_response

@router.get("/image/{image_id}")
async def show_image(
    image_id: int,
    repository: product_repository_dependency    
):
    image = await repository.get_image(image_id=image_id)
    return image

@router.get("/images")
async def show_images(repository: product_repository_dependency):
    images = await repository.get_all_images()
    return images

@router.post("/size")
async def add_size(
    product_id: int, 
    repository: additional_repository_dependency,
    size: str = Query(enum=sizes),
):
    size = await repository.add_size(product_id=product_id, size=size)
    return size

@router.get("/sizes")
async def get_sizes(repository: additional_repository_dependency) -> list[SBaseDataField]:
    sizes = await repository.get_sizes()
    return sizes

@router.post("/color")
async def add_color(
    color: Annotated[SBaseDataFieldAdd, Depends()],
    repository: additional_repository_dependency
):
    color = await repository.add_color(color)
    return color

@router.get("/colors")
async def get_colors(repository: additional_repository_dependency):
    colors = await repository.get_colors()
    return colors

@router.get("/populars")
async def get_populars(repository: product_repository_dependency):
    products = await repository.get_populars()
    return products

@router.get("/new-arrivals")
async def get_new_arrivals(repository: product_repository_dependency):
    products = await repository.get_new_arrivals()
    return products

@router.get("/price-range")
async def get_price_range(repository: product_repository_dependency) -> list[int]:
    range = await repository.get_price_range()
    return range

@router.get("/product-colors/{name}")
async def get_colors(
    name: str,
    repository: product_repository_dependency    
) -> list[SProduct]:
    products = await repository.get_colors(name=name)
    return products

'''@router.get("/allimages")
async def get_all_images():
    images = await ProductRepository.get_all_images()
    return images
'''