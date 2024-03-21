from schemas.common import SBaseDataFieldAdd, SBaseDataField, SCategory
from database import new_session
from sqlalchemy import select
from models.models import CategoryOrm
from models.products import ProductOrm, ProductSizeOrm, ProductColorOrm


class AdditionalForProductSRepository:    
    @classmethod
    async def find_all_accessories_categories(cls) -> list[SBaseDataField]:
        async with new_session() as session:
            query = select(CategoryOrm).filter(CategoryOrm.basic_category=="accessories")
            result = await session.execute(query)

            category_models = result.scalars().all()
            categories = [SBaseDataField.model_validate(category_model) for category_model in category_models]

            return categories

    @classmethod
    async def add_one_category(cls, data) -> int:
        async with new_session() as session:
            category = CategoryOrm(**data)
            session.add(category)
            await session.flush()
            await session.commit()
            return category.id
    
    @classmethod
    async def find_all_categories(cls) -> list[SCategory]:
        async with new_session() as session:
            query = select(CategoryOrm).filter(CategoryOrm.basic_category=="cloths")
            result = await session.execute(query)

            category_models = result.scalars().all()
            categories = [SCategory.model_validate(category_model) for category_model in category_models]

            return categories
            #return category_models
        
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