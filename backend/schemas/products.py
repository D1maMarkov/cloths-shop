from .common import SCategoryAdd, SBaseDataField
from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime
from schemas.brands import SBrand
from settings import Settings


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
    category: SBaseDataField
    brand: SBaseDataField
    sizes: list[str] = []
    color: SBaseDataField
    quantity_sold: int

class SProduct(SProductAdd):
    id: int
    created: datetime | str
    images: list[str] = []
    category: SBaseDataField
    brand: SBaseDataField
    sizes: list[str] = []
    color: SBaseDataField
    quantity_sold: int

    @validator("sizes", pre=True)
    def get_sizes(cls, v, values):
        sizes = [size.size for size in v]

        if len(sizes) == 0:
            return ["ONE SIZE"]
        return sizes

    @validator("brand", pre=True)
    def get_brand(cls, v, values):
        return SBaseDataField(**v.__dict__, viewed_name=v.name)

    @validator("images", pre=True)
    def get_images(cls, v, values):
        images = [f'{Settings.HOST}/products/image/{image.id}' for image in v]

        return images

    @validator("category", pre=True)
    def get_category(cls, v, values):
        return SBaseDataField(**v.__dict__)

    @validator("color", pre=True)
    def get_color(cls, v, values):
        return SBaseDataField(**v.__dict__)

    class Config:
        from_attributes = True

class SProductImage(BaseModel):
    id: int
    image: str
    product_id: int