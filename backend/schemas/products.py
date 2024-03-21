from .common import SCategoryAdd, SBaseDataField
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SProductAdd(BaseModel):
    name: str
    category_id: int
    brand_id: int
    price: int
    description: str
    color_id: int
    code: int
    article: str
    gender: Optional[str]# = Gender.unisex.value

class SBaseProduct(SProductAdd):
    id: int
    created: datetime | str
    images: list[str] = []
    category: str
    brand: str
    sizes: list[str] = []
    color: str

    class Config:
        from_attributes = True

class SProduct(SProductAdd):
    id: int
    created: datetime | str
    images: list[str] = []
    category: SCategoryAdd
    brand: SBaseDataField
    sizes: list[str] = []
    color: SBaseDataField
    quantity_sold: int

    class Config:
        from_attributes = True

class SProductImage(BaseModel):
    id: int
    image: str
    product_id: int