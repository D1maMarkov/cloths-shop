import os

from fastapi import UploadFile
from fastapi.responses import FileResponse
from repositories.brands_repository import BrandRepository
from schemas.brands import SBrand, SBrandAdd, SPaginateBrand
from settings import get_settings


class BrandService:
    def __init__(self, repository: BrandRepository) -> None:
        self.repository = repository

    async def find_all_brands(self) -> list[SBrand]:
        brand_models = await self.repository.find_all_brands()
        brands = [SBrand(**brand.__dict__, viewed_name=brand.name) for brand in brand_models]

        return brands

    async def get_paginate_brands(self) -> list[SPaginateBrand]:
        brand_models = await self.repository.get_paginate_brands()
        brands = [SPaginateBrand(**brand.__dict__) for brand in brand_models]

        return brands

    async def get_image(self, image_id: int):
        image = await self.repository.get_image(image_id=image_id)

        return FileResponse(get_settings().BRANDS_PATH + image.image)

    async def add_image(self, brand_id: int, file: UploadFile):
        contents = file.file.read()

        if not os.path.exists(get_settings().BRANDS_PATH):
            os.makedirs(get_settings().BRANDS_PATH)

        with open(get_settings().BRANDS_PATH + file.filename, "wb") as f:
            f.write(contents)

        file.file.close()

        message = await self.repository.add_image(brand_id=brand_id, filename=file.filename)

        return message

    async def add_brand(self, data: SBrandAdd) -> int:
        brand_dict = data.model_dump()
        brand_id = await self.repository.add_brand(brand_dict)

        return brand_id
