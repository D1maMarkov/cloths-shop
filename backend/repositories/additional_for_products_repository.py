from database import new_session
from models.products import ProductColorOrm, ProductOrm, ProductSizeOrm
from sqlalchemy import select


class AdditionalForProductSRepository:
    @classmethod
    async def add_size(cls, size: dict):
        async with new_session() as session:
            product = await session.get(ProductOrm, size["product_id"])

            product_size = ProductSizeOrm(**size, product=product)

            session.add(product_size)
            await session.commit()

    @classmethod
    async def get_sizes(cls) -> list[str]:
        async with new_session() as session:
            query = select(ProductSizeOrm.size).order_by(ProductSizeOrm.size)
            sizes = await session.execute(query)
            sizes = sizes.unique().scalars().all()

            return sizes

    @classmethod
    async def add_color(cls, color: dict):
        async with new_session() as session:
            product_color = ProductColorOrm(**color)

            session.add(product_color)
            await session.commit()

    @classmethod
    async def get_colors(cls):
        async with new_session() as session:
            query = select(ProductColorOrm)
            colors = await session.execute(query)
            colors = colors.scalars().all()

            return colors
