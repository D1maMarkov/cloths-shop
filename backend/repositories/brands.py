from schemas.brands import SBrandAdd, SBrand, SPaginateBrand
from models.models import BrandImageOrm, BrandOrm
from fastapi.responses import FileResponse
from sqlalchemy.orm import joinedload
from database import new_session
from fastapi import UploadFile
from sqlalchemy import select
from settings import settings
import os


class BrandRepository:
    @classmethod
    async def add_brand(cls, data: SBrandAdd) -> int:
        async with new_session() as session:
            brand_dict = data.model_dump()
            
            brand = BrandOrm(**brand_dict)
            session.add(brand)
            await session.flush()
            await session.commit()
            return brand.id

    @classmethod
    async def add_image(cls, brand_id: int, file: UploadFile):
        async with new_session() as session:
            contents = file.file.read()
            
            if not os.path.exists(settings.BRANDS_PATH):
                os.makedirs(settings.BRANDS_PATH)
                
            with open(settings.BRANDS_PATH + file.filename, 'wb') as f:
                f.write(contents)

            file.file.close()
            
            brand = await session.get(BrandOrm, brand_id)
        
            image = BrandImageOrm(image=file.filename, brand_id=brand_id, brand=brand)
            session.add(image)
            await session.commit()

            return {"message": f"Successfully uploaded {file.filename}"}
    
    @classmethod
    async def get_image(cls, image_id: int):
        async with new_session() as session:
            image = await session.get(BrandImageOrm, image_id)
            
            return FileResponse(settings.BRANDS_PATH + image.image)

    @classmethod
    async def get_brand(cls, brand) -> SBrand:
        serialized_brand = SBrand(**brand.__dict__, viewed_name=brand.name)

        return serialized_brand

    @classmethod
    async def find_all_brands(cls) -> list[SBrand]:
        async with new_session() as session:
            query = select(BrandOrm)
            result = await session.execute(query)

            brand_models = result.scalars().all()
            
            serialized_brands = []
            for brand in brand_models:
                brand_dict = await cls.get_brand(brand)

                serialized_brands.append(brand_dict)
            
            return serialized_brands
            
    @classmethod
    async def get_paginate_brands(cls) -> list[SPaginateBrand]:
        async with new_session() as session:
            query = select(BrandOrm).join(BrandImageOrm)
            
            query = query.options(joinedload(BrandOrm.image))
            result = await session.execute(query)

            brand_models = result.unique().scalars().all()
            
            serialized_brands = []
            for brand in brand_models:
                brand_dict = brand.__dict__
                brand_dict["value"] = brand_dict["name"]

                if brand.image:
                    brand_dict["image"] = f'{settings.HOST}/brands/image/{brand.image.id}'

                serialized_brands.append(brand_dict)
            
            return serialized_brands