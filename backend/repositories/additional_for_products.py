from models.products import ProductOrm, ProductSizeOrm, ProductColorOrm
from schemas.common import SBaseDataFieldAdd, SBaseDataField
from database import new_session
from sqlalchemy import select


class AdditionalForProductSRepository:    
    @classmethod
    async def add_size(cls, product_id: int, size: str):
        async with new_session() as session:
            product = await session.get(ProductOrm, product_id)

            product_size = ProductSizeOrm(
                product_id=product_id, 
                size=size,
                product=product
            )
            
            session.add(product_size)
            await session.commit()
            return {"message": "success"}

    @classmethod
    async def get_sizes(cls) -> list[SBaseDataField]:
        async with new_session() as session:
            query = select(ProductSizeOrm)
            sizes = await session.execute(query)
            sizes = sizes.scalars().all()
            sizes = sorted(set([size.size for size in sizes]))

            serialized_sizes = []
            for size in sizes:
                size_dict = {
                    "viewed_name": size,
                    "name": size
                }

                serialized_sizes.append(size_dict)

            return serialized_sizes
        
    @classmethod
    async def add_color(cls, color: SBaseDataFieldAdd):
        async with new_session() as session:
            color_dict = color.model_dump()
            product_color = ProductColorOrm(**color_dict)
            
            session.add(product_color)
            await session.commit()
            return {"message": "success"}

    @classmethod
    async def get_colors(cls) -> list[SBaseDataField]:
        async with new_session() as session:
            query = select(ProductColorOrm)
            colors = await session.execute(query)
            colors = colors.scalars().all()

            serialized_colors = []
            for color in colors:
                color_dict = {
                    "viewed_name": color.viewed_name,
                    "name": color.name
                }

                serialized_colors.append(color_dict)

            return serialized_colors