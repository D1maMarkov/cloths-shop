from domain.category.basic_category_values import BasicCategory
from domain.category.category import Category
from infrastructure.persistence.repositories.category_repository import (
    CategoriesRepository,
)


class GetAllCategories:
    def __init__(self, repository: CategoriesRepository) -> None:
        self.repository = repository

    async def __call__(self) -> list[Category]:
        category_models = await self.repository.find_all_categories(BasicCategory.cloths)

        return [Category.model_validate(category_model) for category_model in category_models]


class GetAccessoriesCategories:
    def __init__(self, repository: CategoriesRepository) -> None:
        self.repository = repository

    async def __call__(self) -> list[Category]:
        category_models = await self.repository.find_all_categories(BasicCategory.accessories)

        return [Category.model_validate(category_model) for category_model in category_models]