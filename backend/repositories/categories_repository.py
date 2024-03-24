from database import new_session
from models.models import CategoryOrm
from schemas.common import SBaseDataField
from sqlalchemy import select


class CategoriesRepository:
    @classmethod
    async def find_all_categories(cls, basic_category) -> list[SBaseDataField]:
        async with new_session() as session:
            query = select(CategoryOrm).filter(CategoryOrm.basic_category == basic_category)
            result = await session.execute(query)

            category_models = result.scalars().all()

            return category_models

    @classmethod
    async def add_one_category(cls, data) -> int:
        async with new_session() as session:
            category = CategoryOrm(**data)
            session.add(category)
            await session.flush()
            await session.commit()
            return category.id
