from application.contracts.order.create_order_request import CreateOrderRequest
from infrastructure.persistence.repositories.order_repository import OrderRepository
from infrastructure.persistence.repositories.user_repository import UserRepository
from infrastructure.persistence.session.cart_adapter import Cart


class CreateOrder:
    def __init__(self, repository: OrderRepository, cart: Cart, user_repository: UserRepository) -> None:
        self.repository = repository
        self.cart_session = cart
        self.user_repository = user_repository

    async def __call__(self, request: CreateOrderRequest, user) -> None:
        order_id = await self.repository.create_order({**request.model_dump(), "user_id": user.id, "user": user})

        for product in self.cart_session:
            await self.repository.create_order_product(
                {
                    "product_model_id": product["id"],
                    "order_id": order_id,
                    "quantity": product["quantity"],
                    "size": product["size"],
                }
            )

            await self.repository.update_product_quantity_sold(product_id=product["id"], quantity=product["quantity"])
