from domain.product.gender_values import Gender
from pydantic import BaseModel


class AddProductRequest(BaseModel):
    name: str
    category_id: int
    brand_id: int
    price: int
    description: str
    color_id: int
    code: int
    article: str
    gender: Gender | None = Gender.unisex
