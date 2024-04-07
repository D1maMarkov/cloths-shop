from typing import Annotated

from application.contracts.brands.add_brand_request import AddBrandRequest
from application.usecases.brands.add_brand import AddBrand
from application.usecases.brands.brands_image import AddBrandsImage, GetBrandsImage
from application.usecases.brands.get_brands import GetAllBrands, GetAllPaginateBrands
from domain.brand.brand import Brand, PaginateBrand
from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import FileResponse
from web_api.depends.brand import (
    get_add_brand_interactor,
    get_add_brands_image_interactor,
    get_find_brands_image_interactor,
    get_find_brands_interactor,
    get_fint_paginate_brands_interactor,
)

router = APIRouter(prefix="/brands", tags=["brands"])


@router.get("/", response_model=list[Brand])
async def get_brands(get_brands_interactor: GetAllBrands = Depends(get_find_brands_interactor)) -> list[Brand]:
    return await get_brands_interactor()


@router.get("/paginate-brands", response_model=list[PaginateBrand])
async def get_paginate_brands(
    get_paginate_brands_interacor: GetAllPaginateBrands = Depends(get_fint_paginate_brands_interactor),
) -> list[PaginateBrand]:
    return await get_paginate_brands_interacor()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_brand(
    brand: Annotated[AddBrandRequest, Depends()], add_product_interactor: AddBrand = Depends(get_add_brand_interactor)
) -> None:
    return await add_product_interactor(brand)


@router.post("/image", status_code=status.HTTP_201_CREATED)
async def add_image(
    brand_id: int,
    image: UploadFile,
    add_brands_image_interactor: AddBrandsImage = Depends(get_add_brands_image_interactor),
) -> None:
    return await add_brands_image_interactor(brand_id=brand_id, file=image)


@router.get("/image/{image_id}")
async def show_image(
    image_id: int, get_brands_image_interactor: GetBrandsImage = Depends(get_find_brands_image_interactor)
) -> FileResponse:
    return await get_brands_image_interactor(image_id)
