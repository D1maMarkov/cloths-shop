from typing import Annotated

from fastapi import APIRouter, Depends, Request
from schemas.products import SBaseProduct
from services.favs_service import FavsService

router = APIRouter(prefix="/favs", tags=["favs"])

service = FavsService()


def get_service():
    return service


service_dependency = Annotated[dict, Depends(get_service)]


@router.post("/add")
async def favs_add(request: Request, product: SBaseProduct, service: service_dependency):
    product = await service.add_product(request=request, product=product)
    return product


@router.get("/get")
async def favs_get(request: Request, service: service_dependency) -> list[SBaseProduct]:
    products = await service.get_products(request=request)
    return products


@router.get("/remove/{id}")
async def remove(request: Request, id: int, service: service_dependency):
    response = await service.remove(request=request, id=id)
    return response
