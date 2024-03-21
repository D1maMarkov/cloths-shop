from repositories.favs import FavsRepository
from schemas.cart import SCartProduct
from schemas.products import SProduct
from fastapi import APIRouter
from fastapi import Request


router = APIRouter(
    prefix="/favs",
    tags=["favs"]
)

@router.post("/add")
async def favs_add(request: Request, product: SProduct):
    product = await FavsRepository.add_product(request=request, product=product)
    return product

@router.get("/get")
async def favs_get(request: Request):
    products = await FavsRepository.get_products(request=request)
    return products

@router.get("/remove/{id}")
async def remove(request: Request, id: int):
    response = await FavsRepository.remove(request=request, id=id)
    return response