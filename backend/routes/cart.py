from schemas.cart import SCartProduct, CreateOrderForm
from utils.user_dependency import user_dependency
from fastapi import APIRouter, Request, Depends
from repositories.order import OrderRepository
from repositories.cart import CartRepository
from typing import Annotated


router = APIRouter(
    prefix="/cart",
    tags=["cart"]
)

cart_repository = CartRepository()

def get_cart_repository():
    return cart_repository

cart_repository_dependency = Annotated[dict, Depends(get_cart_repository)]

order_repository = OrderRepository()

def get_order_repository():
    return order_repository

order_repository_dependency = Annotated[dict, Depends(get_order_repository)]

@router.post("/add")
async def cart_add(
    request: Request, 
    product: SCartProduct,
    repository: cart_repository_dependency
):
    product = await repository.add_product(request=request, product=product)
    return product

@router.get("/get")
async def cart_get(
    request: Request,
    repository: cart_repository_dependency    
) -> list[SCartProduct]:
    products = await repository.get_products(request=request)
    return products

@router.post("/low-quantity")
async def low_quantity(
    request: Request, 
    product: SCartProduct,
    repository: cart_repository_dependency
):
    response = await repository.low_quantity(request=request, product=product)
    return response

@router.post("/remove")
async def remove(
    request: Request, 
    product: SCartProduct,
    repository: cart_repository_dependency
):
    response = await repository.remove(request=request, product=product)
    return response

@router.get("/clear")
async def clear(
    request: Request,
    repository: cart_repository_dependency    
):
    response = await repository.clear(request=request)
    return response

@router.post("/create-order")
async def create_order(
    user: user_dependency, 
    request: Request, 
    order_form: CreateOrderForm,
    repository: order_repository_dependency
):
    response = await repository.create_order(
        request=request,
        user=user,
        order_form=order_form
    )
    
    return response

@router.get("/get-orders")
async def get_orders(
    user: user_dependency,
    repository: order_repository_dependency    
):
    response = await repository.get_orders(user=user)
    return response