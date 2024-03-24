from typing import Annotated

from fastapi import APIRouter, Depends, Request
from repositories.order_repository import OrderRepository
from repositories.products_repository import ProductRepository
from schemas.cart import CreateOrderForm, SCartProduct
from services.cart_service import CartService
from services.order_service import OrderService
from utils.user_dependency import user_dependency

router = APIRouter(prefix="/cart", tags=["cart"])

cart_service = CartService()


def get_cart_service():
    return cart_service


cart_service_dependency = Annotated[dict, Depends(get_cart_service)]

order_repository = OrderRepository()
product_repository = ProductRepository()
order_service = OrderService(order_repository, product_repository)


def get_order_service():
    return order_service


order_service_dependency = Annotated[dict, Depends(get_order_service)]


@router.post("/add")
async def cart_add(request: Request, product: SCartProduct, service: cart_service_dependency):
    product = await service.add_product(request=request, product=product)
    return product


@router.get("/get")
async def cart_get(request: Request, service: cart_service_dependency) -> list[SCartProduct]:
    products = await service.get_products(request=request)
    return products


@router.post("/low-quantity")
async def low_quantity(request: Request, product: SCartProduct, service: cart_service_dependency):
    response = await service.low_quantity(request=request, product=product)
    return response


@router.get("/clear")
async def clear(request: Request, service: cart_service_dependency):
    response = await service.clear(request=request)
    return response


@router.post("/create-order")
async def create_order(
    user: user_dependency, request: Request, order_form: CreateOrderForm, service: order_service_dependency
):
    response = await service.create_order(request=request, user=user, order_form=order_form)

    return response


@router.get("/get-orders")
async def get_orders(user: user_dependency, service: order_service_dependency):
    response = await service.get_orders(user=user)
    return response
