from dataclasses import dataclass

from domain.product.product import BaseProduct


@dataclass
class CartProduct(BaseProduct):
    image: str
    quantity: int
    size: str
