from application.usecases.brands.add_brand import AddBrand
from application.usecases.brands.brands_image import AddBrandsImage, GetBrandsImage
from application.usecases.brands.get_brands import GetAllBrands, GetAllPaginateBrands
from fastapi import Depends
from infrastructure.configs.brand_config import BrandSettings, get_settings
from infrastructure.file_service.file_service import FileService, get_file_service
from infrastructure.persistence.repositories.brand_repository import BrandRepository
from sqlalchemy.ext.asyncio import AsyncSession
from web_api.depends.get_db import get_db


def get_repository(db: AsyncSession = Depends(get_db)) -> BrandRepository:
    return BrandRepository(db)


def get_find_brands_interactor(repository: BrandRepository = Depends(get_repository)) -> GetAllBrands:
    return GetAllBrands(repository)


def get_fint_paginate_brands_interactor(repository: BrandRepository = Depends(get_repository)) -> GetAllPaginateBrands:
    return GetAllPaginateBrands(repository)


def get_add_brand_interactor(repository: BrandRepository = Depends(get_repository)) -> AddBrand:
    return AddBrand(repository)


def get_add_brands_image_interactor(
    repository: BrandRepository = Depends(get_repository),
    file_service: FileService = Depends(get_file_service),
    settings: BrandSettings = Depends(get_settings),
) -> AddBrandsImage:
    return AddBrandsImage(repository, file_service, settings)


def get_find_brands_image_interactor(
    repository: BrandRepository = Depends(get_repository), settings: BrandSettings = Depends(get_settings)
) -> GetBrandsImage:
    return GetBrandsImage(repository, settings)
