from domain.order.order import Order
from infrastructure.persistence.repositories.mappers.order_mappers import (
    order_from_orm_to_entity,
)
from infrastructure.persistence.repositories.order_repository import OrderRepository


class GetOrders:
    def __init__(self, repository: OrderRepository) -> None:
        self.repository = repository

    async def __call__(self, user_id: int) -> list[Order]:
        order_models = await self.repository.get_orders(user_id)

        return [order_from_orm_to_entity(order_model) for order_model in order_models]
