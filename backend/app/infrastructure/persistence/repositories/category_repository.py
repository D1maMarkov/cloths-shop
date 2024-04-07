from domain.category.repository import CategoriesRepositoryInterface
from infrastructure.persistence.models.category_models import CategoryOrm
from infrastructure.persistence.repositories.repository import BaseRepository
from sqlalchemy import select


class CategoriesRepository(CategoriesRepositoryInterface, BaseRepository):
    async def find_all_categories(self, basic_category: str):
        query = select(CategoryOrm).filter(CategoryOrm.basic_category == basic_category)
        result = await self.db.execute(query)

        category_models = result.scalars().all()

        return category_models

    async def add_category(self, data: dict) -> None:
        category = CategoryOrm(**data)
        self.db.add(category)
        await self.db.commit()
