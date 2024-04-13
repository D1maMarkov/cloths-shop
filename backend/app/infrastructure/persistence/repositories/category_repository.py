from domain.category.category import Category
from domain.category.repository import CategoriesRepositoryInterface
from infrastructure.persistence.models.category_models import CategoryOrm
from infrastructure.persistence.repositories.mappers.category_mapper import (
    from_orm_to_category,
)
from infrastructure.persistence.repositories.repository import BaseRepository
from sqlalchemy import select


class CategoriesRepository(CategoriesRepositoryInterface, BaseRepository):
    async def find_all_categories(self, basic_category: str) -> Category:
        query = select(CategoryOrm).filter(CategoryOrm.basic_category == basic_category)
        result = await self.db.execute(query)

        category_models = result.scalars().all()

        return [from_orm_to_category(category_model) for category_model in category_models]

    async def add_category(self, data: dict) -> None:
        category = CategoryOrm(**data)
        self.db.add(category)
        await self.db.commit()
