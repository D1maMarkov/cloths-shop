from typing import Annotated

from application.contracts.categories.add_category_request import AddCategoryRequest
from application.usecases.category.add_category import AddCategory
from application.usecases.category.get_categories import (
    GetAccessoriesCategories,
    GetAllCategories,
)
from domain.category.category import Category
from fastapi import APIRouter, Depends, status
from web_api.depends.category import (
    get_add_category_interactor,
    get_find_accessories_categories_interactor,
    get_find_all_categories_interactor,
)

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_category(
    category: Annotated[AddCategoryRequest, Depends()],
    add_category_interactor: AddCategory = Depends(get_add_category_interactor),
) -> None:
    return await add_category_interactor(category)


@router.get("/", response_model=list[Category])
async def get_categories(
    get_categories_interactor: GetAllCategories = Depends(get_find_all_categories_interactor),
) -> list[Category]:
    return await get_categories_interactor()


@router.get("/accessories", response_model=list[Category])
async def get_accessories_categories(
    get_accessories_categories_interactor: GetAccessoriesCategories = Depends(
        get_find_accessories_categories_interactor
    ),
) -> list[Category]:
    return await get_accessories_categories_interactor()
