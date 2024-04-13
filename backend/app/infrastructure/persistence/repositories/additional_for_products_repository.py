from domain.additional_for_product.repository import (
    AdditionalForProductSRepositoryInterface,
)
from domain.common.base_data_field import BaseDataField
from domain.product.exc import ProductNotFound
from infrastructure.persistence.models.additional_for_product_models import (
    ProductColorOrm,
    ProductSizeOrm,
)
from infrastructure.persistence.models.product_models import ProductOrm
from infrastructure.persistence.repositories.mappers.color_mapper import (
    from_orm_to_color,
)
from infrastructure.persistence.repositories.mappers.size_mapper import (
    from_orm_to_sizes,
)
from infrastructure.persistence.repositories.repository import BaseRepository
from sqlalchemy import select


class AdditionalForProductSRepository(BaseRepository, AdditionalForProductSRepositoryInterface):
    async def add_size(self, size: dict) -> None:
        product = await self.db.get(ProductOrm, size["product_id"])
        if product is None:
            raise ProductNotFound("product with this id not found")

        product_size = ProductSizeOrm(**size, product=product)

        self.db.add(product_size)
        await self.db.commit()

    async def get_sizes(self) -> list[str]:
        query = select(ProductSizeOrm).order_by(ProductSizeOrm.size)
        sizes = await self.db.execute(query)
        sizes = sizes.unique().scalars().all()

        return from_orm_to_sizes(sizes)

    async def add_color(self, color: dict) -> None:
        product_color = ProductColorOrm(**color)

        self.db.add(product_color)
        await self.db.commit()

    async def get_colors(self) -> list[BaseDataField]:
        query = select(ProductColorOrm)
        colors = await self.db.execute(query)
        colors = colors.scalars().all()

        return [from_orm_to_color(color) for color in colors]
