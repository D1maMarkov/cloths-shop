from application.usecases.order.get_orders import GetOrders
from fastapi import Depends
from infrastructure.persistence.repositories.order_repository import OrderRepository
from web_api.depends.order.get_repository import get_repository


async def get_find_interactor(order_repository: OrderRepository = Depends(get_repository)) -> GetOrders:
    return GetOrders(order_repository)
