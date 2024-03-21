from pydantic import BaseModel
from datetime import datetime


class CreateOrderForm(BaseModel):
    name: str
    secondname: str
    adress: str
    phone: str
    payment: str
    delivery: str

class SCartProduct(BaseModel):
    id: int
    image: str
    name: str
    description: str
    price: int
    quantity: int
    size: str

class SOrderProduct(SCartProduct):
    order_id: int

class SOrder(CreateOrderForm):
    user_id: int
    created: datetime | str
    order_products: list[SCartProduct] = []