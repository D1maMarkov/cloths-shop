from application.usecases.order.create_order import CreateOrder
from fastapi import Depends
from infrastructure.persistence.repositories.order_repository import OrderRepository
from infrastructure.persistence.repositories.user_repository import UserRepository
from infrastructure.persistence.session.cart_adapter import Cart
from web_api.depends.cart import get_cart
from web_api.depends.order.get_repository import get_repository
from web_api.depends.user import get_repository as get_user_repository


async def get_create_interactor(
    cart: Cart = Depends(get_cart),
    user_repository: UserRepository = Depends(get_user_repository),
    order_repository: OrderRepository = Depends(get_repository),
) -> CreateOrder:
    return CreateOrder(order_repository, cart, user_repository)
