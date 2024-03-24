from enums import BasicCategory
from repositories.categories_repository import CategoriesRepository
from schemas.common import SCategory


class CategoriesService:
    def __init__(self, repository: CategoriesRepository) -> None:
        self.repository = repository

    async def find_all_accessories_categories(self) -> list[SCategory]:
        category_models = await self.repository.find_all_categories(BasicCategory.accessories)
        categories = [SCategory.model_validate(category_model) for category_model in category_models]

        return categories

    async def add_one_category(self, data) -> int:
        category_id = await self.repository.add_one_category(data)

        return category_id

    async def find_all_categories(self) -> list[SCategory]:
        category_models = await self.repository.find_all_categories(BasicCategory.cloths)
        categories = [SCategory.model_validate(category_model) for category_model in category_models]

        return categories
