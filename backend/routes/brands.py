from schemas.brands import SBrand, SBrandAdd, SPaginateBrand
from fastapi import APIRouter, Depends, UploadFile
from repositories.brands import BrandRepository
from typing import Annotated


router = APIRouter(
    prefix="/brands",
    tags=["brands"]
)

repository = BrandRepository()

def get_repository():
    return repository

repository_dependency = Annotated[dict, Depends(get_repository)]

@router.get("/")
async def get_brands(repository: repository_dependency) -> list[SBrand]:
    brands = await repository.find_all_brands()
    return brands

@router.get("/paginate-brands")
async def get_paginate_brands(repository: repository_dependency) -> list[SPaginateBrand]:
    brands = await repository.get_paginate_brands()
    return brands

@router.post("/", status_code=201)
async def add_brand(
    brand: Annotated[SBrandAdd, Depends()],
    repository: repository_dependency
):
    brand_id = await repository.add_brand(brand)
    return {"ok": True, "brand_id": brand_id}

@router.post("/image", status_code=201)
async def add_image(
    brand_id: int,
    image: UploadFile,
    repository: repository_dependency
):
    image_response = await repository.add_image(
        brand_id=brand_id, 
        file=image
    )
    return image_response

@router.get("/image/{image_id}")
async def show_image(
    image_id: int, 
    repository: repository_dependency
):
    image = await repository.get_image(image_id=image_id)
    return image