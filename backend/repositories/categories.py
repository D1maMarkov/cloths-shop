from schemas.common import SBaseDataField, SCategory
from models.models import CategoryOrm
from database import new_session
from sqlalchemy import select


class CategoriesRepository:    
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