from domain.order.order import Order
from domain.order.repository import OrderRepositoryInterface
from infrastructure.persistence.repositories.mappers.order_mappers import (
    order_from_orm_to_entity,
)


class GetOrders:
    def __init__(self, repository: OrderRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self, user_id: int) -> list[Order]:
        order_models = await self.repository.get_orders(user_id)

        return [order_from_orm_to_entity(order_model) for order_model in order_models]
