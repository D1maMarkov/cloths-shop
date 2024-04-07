from application.contracts.categories.add_category_request import AddCategoryRequest
from domain.category.repository import CategoriesRepositoryInterface


class AddCategory:
    def __init__(self, repository: CategoriesRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self, data: AddCategoryRequest) -> None:
        category_dict = data.model_dump()

        return await self.repository.add_category(category_dict)
