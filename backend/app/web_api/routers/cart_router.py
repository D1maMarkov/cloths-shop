from application.contracts.cart.cart_product_request import CartProductRequest
from application.usecases.cart.add_product import AddProduct
from application.usecases.cart.clear import Clear
from application.usecases.cart.get_products import GetCart
from application.usecases.cart.low_quantity import LowQuantity
from domain.cart.cart import CartProduct
from fastapi import APIRouter, Depends, status
from web_api.depends.cart import (
    get_add_in_cart_interactor,
    get_clear_cart_intetactor,
    get_find_cart_intetactor,
    get_low_quantity_intetactor,
)

router = APIRouter(prefix="/cart", tags=["cart"])


@router.post("/add", status_code=status.HTTP_201_CREATED)
async def cart_add(
    product: CartProductRequest, add_in_cart_interactor: AddProduct = Depends(get_add_in_cart_interactor)
) -> None:
    return await add_in_cart_interactor(product)


@router.get("/", response_model=list[CartProduct])
async def cart_get(get_cart_interactor: GetCart = Depends(get_find_cart_intetactor)) -> list[CartProduct]:
    return await get_cart_interactor()


@router.post("/low-quantity")
async def low_quantity(
    product: CartProductRequest, low_quantity_interactor: LowQuantity = Depends(get_low_quantity_intetactor)
) -> None:
    return await low_quantity_interactor(product)


@router.get("/clear")
async def clear(cart_clear_interactor: Clear = Depends(get_clear_cart_intetactor)) -> None:
    return await cart_clear_interactor()
