from repositories.additional_for_products import AdditionalForProductSRepository
from schemas.common import SBaseDataField, SCategory
from fastapi import APIRouter, Query
from enums import basic_categories


router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.post("/")
async def add_category(
    name: str,
    viewed_name: str,
    basic_category: str = Query(enum=basic_categories)
):
    category = {
        "name": name,
        "viewed_name": viewed_name,
        "basic_category": basic_category
    }
    
    category_id = await AdditionalForProductSRepository.add_one_category(category)
    return {"ok": True, "category_id": category_id}

@router.get("/")
async def get_categories() -> list[SCategory]:
    categories = await AdditionalForProductSRepository.find_all_categories()
    return categories

@router.get("/accessories")
async def get_accessories_categories() -> list[SBaseDataField]:
    categories = await AdditionalForProductSRepository.find_all_accessories_categories()
    return categories