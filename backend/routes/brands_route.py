from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile
from repositories.brands_repository import BrandRepository
from schemas.brands import SBrand, SBrandAdd, SPaginateBrand
from services.brands_service import BrandService

router = APIRouter(prefix="/brands", tags=["brands"])

repository = BrandRepository()
service = BrandService(repository)


def get_service():
    return service


service_dependency = Annotated[dict, Depends(get_service)]


@router.get("/")
async def get_brands(service: service_dependency) -> list[SBrand]:
    brands = await service.find_all_brands()
    return brands


@router.get("/paginate-brands")
async def get_paginate_brands(service: service_dependency) -> list[SPaginateBrand]:
    brands = await service.get_paginate_brands()
    return brands


@router.post("/", status_code=201)
async def add_brand(brand: Annotated[SBrandAdd, Depends()], service: service_dependency):
    brand_dict = brand.model_dump()

    brand_id = await service.add_brand(brand_dict)
    return {"ok": True, "brand_id": brand_id}


@router.post("/image", status_code=201)
async def add_image(brand_id: int, image: UploadFile, service: service_dependency):
    image_response = await service.add_image(brand_id=brand_id, file=image)

    return image_response


@router.get("/image/{image_id}")
async def show_image(image_id: int, service: service_dependency):
    image = await service.get_image(image_id=image_id)
    return image
