from typing import Annotated

from fastapi import APIRouter, Depends
from repositories.categories_repository import CategoriesRepository
from schemas.common import SBaseDataField, SCategory
from services.categories_service import CategoriesService

router = APIRouter(prefix="/categories", tags=["categories"])

repository = CategoriesRepository()
service = CategoriesService(repository)


def get_service():
    return service


service_dependency = Annotated[dict, Depends(get_service)]


@router.post("/")
async def add_category(category: Annotated[SCategory, Depends()], service: service_dependency):
    category_id = await service.add_one_category(category)
    return {"ok": True, "category_id": category_id}


@router.get("/")
async def get_categories(service: service_dependency) -> list[SCategory]:
    categories = await service.find_all_categories()
    return categories


@router.get("/accessories")
async def get_accessories_categories(service: service_dependency) -> list[SBaseDataField]:
    categories = await service.find_all_accessories_categories()
    return categories
