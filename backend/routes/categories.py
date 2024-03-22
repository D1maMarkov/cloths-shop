from repositories.categories import CategoriesRepository
from schemas.common import SBaseDataField, SCategory
from fastapi import APIRouter, Query, Depends
from enums import basic_categories
from typing import Annotated


router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

repository = CategoriesRepository()

def get_repository():
    return repository

repository_dependency = Annotated[dict, Depends(get_repository)]

@router.post("/")
async def add_category(
    name: str,
    viewed_name: str,
    repository: repository_dependency,
    basic_category: str = Query(enum=basic_categories)
):
    category = {
        "name": name,
        "viewed_name": viewed_name,
        "basic_category": basic_category
    }
    
    category_id = await repository.add_one_category(category)
    return {"ok": True, "category_id": category_id}

@router.get("/")
async def get_categories(repository: repository_dependency) -> list[SCategory]:
    categories = await repository.find_all_categories()
    return categories

@router.get("/accessories")
async def get_accessories_categories(repository: repository_dependency) -> list[SBaseDataField]:
    categories = await repository.find_all_accessories_categories()
    return categories