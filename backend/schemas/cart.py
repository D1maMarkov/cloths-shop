from pydantic import BaseModel, validator
from datetime import datetime
from settings import settings


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
    @validator("image", pre=True)
    def get_image(cls, v, values):
        return f"{settings.HOST}/products/image/{v.id}"

class SOrder(CreateOrderForm):
    user_id: int
    created: datetime | str
    order_products: list[SCartProduct] = []