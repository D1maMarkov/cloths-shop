from fastapi import APIRouter, Request, Depends
from repositories.favs import FavsRepository
from schemas.products import SBaseProduct
from typing import Annotated


router = APIRouter(
    prefix="/favs",
    tags=["favs"]
)

repository = FavsRepository()

def get_repository():
    return repository

repository_dependency = Annotated[dict, Depends(get_repository)]

@router.post("/add")
async def favs_add(
    request: Request,
    product: SBaseProduct,
    repository: repository_dependency
):
    product = await repository.add_product(request=request, product=product)
    return product

@router.get("/get")
async def favs_get(
    request: Request,
    repository: repository_dependency    
) -> list[SBaseProduct]:
    products = await repository.get_products(request=request)
    return products

@router.get("/remove/{id}")
async def remove(
    request: Request, 
    id: int,
    repository: repository_dependency    
):
    response = await repository.remove(request=request, id=id)
    return response