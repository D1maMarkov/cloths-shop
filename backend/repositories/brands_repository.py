from database import new_session
from models.models import BrandImageOrm, BrandOrm
from sqlalchemy import select
from sqlalchemy.orm import joinedload


class BrandRepository:
    @classmethod
    async def add_brand(cls, data: dict) -> int:
        async with new_session() as session:
            brand = BrandOrm(**data)
            session.add(brand)
            await session.flush()
            await session.commit()
            return brand.id

    @classmethod
    async def add_image(cls, brand_id: int, filename: str):
        async with new_session() as session:
            brand = await session.get(BrandOrm, brand_id)

            image = BrandImageOrm(image=filename, brand_id=brand_id, brand=brand)

            session.add(image)
            await session.commit()

            return {"message": f"Successfully uploaded {filename} for {brand.name}"}

    @classmethod
    async def get_image(cls, image_id: int):
        async with new_session() as session:
            image = await session.get(BrandImageOrm, image_id)

            return image

    @classmethod
    async def find_all_brands(cls):
        async with new_session() as session:
            query = select(BrandOrm)
            result = await session.execute(query)

            brand_models = result.scalars().all()

            return brand_models

    @classmethod
    async def get_paginate_brands(cls):
        async with new_session() as session:
            query = select(BrandOrm).join(BrandImageOrm)

            query = query.options(joinedload(BrandOrm.image))
            result = await session.execute(query)

            brand_models = result.unique().scalars().all()

            return brand_models
