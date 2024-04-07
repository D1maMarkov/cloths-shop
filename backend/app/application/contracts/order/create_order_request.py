from pydantic import BaseModel


class CreateOrderRequest(BaseModel):
    name: str
    secondname: str
    adress: str
    phone: str
    payment: str
    delivery: str
