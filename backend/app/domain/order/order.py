from datetime import datetime

from domain.product.product import BaseProduct
from pydantic import BaseModel


class OrderProduct(BaseProduct):
    quantity: int
    size: str
    image: str


class Order(BaseModel):
    name: str
    secondname: str
    adress: str
    phone: str
    payment: str
    delivery: str
    user_id: int
    created: datetime | str
    order_products: list[OrderProduct] = []
