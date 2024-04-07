from typing import Protocol


class FavsInterface(Protocol):
    def add_product(self, key: str, product: dict) -> None:
        raise NotImplementedError

    def remove(self, key: str) -> None:
        raise NotImplementedError
