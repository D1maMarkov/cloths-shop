from domain.common.base_data_field import BaseDataField
from infrastructure.persistence.models.additional_for_product_models import (
    ProductColorOrm,
    ProductSizeOrm,
)
from infrastructure.persistence.models.product_models import ProductOrm
from infrastructure.persistence.repositories.repository import BaseRepository
from sqlalchemy import select
from web_api.exc.product_exc import ProductNotFound


class AdditionalForProductSRepository(BaseRepository):
    async def add_size(self, size: dict) -> None:
        product = await self.db.get(ProductOrm, size["product_id"])
        if product is None:
            raise ProductNotFound()

        product_size = ProductSizeOrm(**size, product=product)

        self.db.add(product_size)
        await self.db.commit()

    async def get_sizes(self) -> list[str]:
        query = select(ProductSizeOrm.size).order_by(ProductSizeOrm.size)
        sizes = await self.db.execute(query)
        sizes = sizes.unique().scalars().all()

        return sizes

    async def add_color(self, color: dict) -> None:
        product_color = ProductColorOrm(**color)

        self.db.add(product_color)
        await self.db.commit()

    async def get_colors(self) -> list[BaseDataField]:
        query = select(ProductColorOrm)
        colors = await self.db.execute(query)
        colors = colors.scalars().all()

        return colors
