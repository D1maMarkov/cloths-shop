from dataclasses import dataclass
from datetime import datetime

from domain.product.product import BaseProduct


@dataclass
class OrderProduct(BaseProduct):
    quantity: int
    size: str
    image: str


@dataclass
class Order:
    name: str
    secondname: str
    adress: str
    phone: str
    payment: str
    delivery: str
    user_id: int
    created: datetime | str
    order_products: list[OrderProduct]
