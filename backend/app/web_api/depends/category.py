from application.usecases.category.add_category import AddCategory
from application.usecases.category.get_categories import (
    GetAccessoriesCategories,
    GetAllCategories,
)
from fastapi import Depends
from infrastructure.persistence.repositories.category_repository import (
    CategoriesRepository,
)
from sqlalchemy.ext.asyncio import AsyncSession
from web_api.depends.get_db import get_db


def get_repository(db: AsyncSession = Depends(get_db)) -> CategoriesRepository:
    return CategoriesRepository(db)


def get_add_category_interactor(repository: CategoriesRepository = Depends(get_repository)) -> AddCategory:
    return AddCategory(repository)


def get_find_all_categories_interactor(repository: CategoriesRepository = Depends(get_repository)) -> GetAllCategories:
    return GetAllCategories(repository)


def get_find_accessories_categories_interactor(
    repository: CategoriesRepository = Depends(get_repository),
) -> GetAccessoriesCategories:
    return GetAccessoriesCategories(repository)
