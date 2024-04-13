from domain.category.basic_category_values import BasicCategory
from domain.category.category import Category
from domain.category.repository import CategoriesRepositoryInterface


class GetAllCategories:
    def __init__(self, repository: CategoriesRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self) -> list[Category]:
        return await self.repository.find_all_categories(BasicCategory.cloths)


class GetAccessoriesCategories:
    def __init__(self, repository: CategoriesRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self) -> list[Category]:
        return await self.repository.find_all_categories(BasicCategory.accessories)
