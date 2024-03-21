from schemas.cart import SCartProduct, CreateOrderForm
from utils.user_dependency import user_dependency
from repositories.order import OrderRepository
from repositories.cart import CartRepository
from fastapi import APIRouter
from fastapi import Request


router = APIRouter(
    prefix="/cart",
    tags=["cart"]
)

@router.post("/add")
async def cart_add(request: Request, product: SCartProduct):
    product = await CartRepository.add_product(request=request, product=product)
    return product

@router.get("/get")
async def cart_get(request: Request) -> list[SCartProduct]:
    products = await CartRepository.get_products(request=request)
    return products

@router.post("/low-quantity")
async def low_quantity(request: Request, product: SCartProduct):
    response = await CartRepository.low_quantity(request=request, product=product)
    return response

@router.post("/remove")
async def remove(request: Request, product: SCartProduct):
    response = await CartRepository.remove(request=request, product=product)
    return response

@router.get("/clear")
async def clear(request: Request):
    response = await CartRepository.clear(request=request)
    return response

@router.post("/create-order")
async def create_order(user: user_dependency, request: Request, order_form: CreateOrderForm):
    response = await OrderRepository.create_order(
        request=request, 
        user=user, 
        order_form=order_form
    )
    return response

@router.get("/get-orders")
async def get_orders(user: user_dependency):
    response = await OrderRepository.get_orders(user=user)
    return response

@router.get("/get-products")
async def get_ordersgrgrg():
    response = await OrderRepository.get_products()
    return response