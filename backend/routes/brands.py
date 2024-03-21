from schemas.brands import SBrand, SBrandAdd, SPaginateBrand
from fastapi import APIRouter, Depends, UploadFile
from repositories.brands import BrandRepository
from typing import Annotated


router = APIRouter(
    prefix="/brands",
    tags=["brands"]
)

@router.get("/")
async def get_brands() -> list[SBrand]:
    brands = await BrandRepository.find_all_brands()
    return brands

@router.get("/paginate-brands")
async def get_paginate_brands() -> list[SPaginateBrand]:
    brands = await BrandRepository.get_paginate_brands()
    return brands

@router.post("/")
async def add_brand(
    brand: Annotated[SBrandAdd, Depends()]
):
    brand_id = await BrandRepository.add_brand(brand)
    return {"ok": True, "brand_id": brand_id}

@router.post("/image")
async def add_image(
    brand_id: int,
    image: UploadFile
):
    image_response = await BrandRepository.add_image(
        brand_id=brand_id, 
        file=image
    )
    return image_response

@router.get("/image/{image_id}")
async def show_image(image_id: int):
    image = await BrandRepository.get_image(image_id=image_id)
    return image