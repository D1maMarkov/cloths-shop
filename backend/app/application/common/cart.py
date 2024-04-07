from typing import Protocol
from domain.cart.cart import CartProduct

class CartInterface(Protocol):
    def add_product(self, key: str, product: dict) -> None:
        raise NotImplementedError

    def remove(self, key: str) -> None:
        raise NotImplementedError

    def add_quantity(self, key) -> None:
        raise NotImplementedError

    def low_quantity(self, key: str) -> None:
        raise NotImplementedError

    def get_product(self, key: str) -> CartProduct:
        raise NotImplementedError

    def clear(self) -> None:
        raise NotImplementedError
