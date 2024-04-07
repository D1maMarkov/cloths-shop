from application.usecases.cart.add_product import AddProduct
from application.usecases.cart.clear import Clear
from application.usecases.cart.get_products import GetCart
from application.usecases.cart.low_quantity import LowQuantity
from fastapi import Depends, Request
from infrastructure.persistence.session.cart_adapter import Cart


def get_cart(request: Request) -> Cart:
    return Cart(request)


def get_add_in_cart_interactor(cart: Cart = Depends(get_cart)) -> AddProduct:
    return AddProduct(cart)


def get_find_cart_intetactor(cart: Cart = Depends(get_cart)) -> GetCart:
    return GetCart(cart)


def get_low_quantity_intetactor(cart: Cart = Depends(get_cart)) -> LowQuantity:
    return LowQuantity(cart)


def get_clear_cart_intetactor(cart: Cart = Depends(get_cart)) -> Clear:
    return Clear(cart)
