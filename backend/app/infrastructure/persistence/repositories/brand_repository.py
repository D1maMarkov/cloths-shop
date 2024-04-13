from domain.brand.brand import Brand
from domain.brand.exc import BrandNotFound
from domain.brand.repository import BrandRepositoryInterface
from infrastructure.persistence.models.brand_models import BrandImageOrm, BrandOrm
from infrastructure.persistence.repositories.mappers.brand_mappers import (
    from_orm_to_brand,
    from_orm_to_paginate_brand,
)
from infrastructure.persistence.repositories.repository import BaseRepository
from sqlalchemy import select
from sqlalchemy.orm import joinedload


class BrandRepository(BrandRepositoryInterface, BaseRepository):
    async def add_brand(self, data: dict) -> None:
        brand = BrandOrm(**data)
        self.db.add(brand)
        await self.db.commit()

    async def add_image(self, brand_id: int, filename: str) -> None:
        brand = await self.db.get(BrandOrm, brand_id)
        if brand is None:
            raise BrandNotFound("brand with this id not found")

        image = BrandImageOrm(image=filename, brand_id=brand_id, brand=brand)

        self.db.add(image)
        await self.db.commit()

    async def get_image(self, image_id: int):
        return await self.db.get(BrandImageOrm, image_id)

    async def find_all_brands(self) -> Brand:
        query = select(BrandOrm)
        result = await self.db.execute(query)

        brand_models = result.scalars().all()

        return [from_orm_to_brand(brand_model) for brand_model in brand_models]

    async def get_paginate_brands(self):
        query = select(BrandOrm).join(BrandImageOrm)

        query = query.options(joinedload(BrandOrm.image))
        result = await self.db.execute(query)

        brand_models = result.unique().scalars().all()

        return [from_orm_to_paginate_brand(brand) for brand in brand_models]
