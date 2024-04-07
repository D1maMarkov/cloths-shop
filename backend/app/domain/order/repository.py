from typing import Protocol


class OrderRepositoryInterface(Protocol):
    async def create_order(self, order_form: dict) -> int:
        raise NotImplementedError

    async def create_order_product(self, order_product_dict: dict) -> None:
        raise NotImplementedError

    async def update_product_quantity_sold(self, product_id: int, quantity: int) -> None:
        raise NotImplementedError

    async def get_orders(self, user_id: int):
        raise NotImplementedError
