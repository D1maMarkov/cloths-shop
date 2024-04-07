from domain.common.base_data_field import BaseDataField
from domain.product.gender_values import Gender
from pydantic import BaseModel


class BaseProduct(BaseModel):
    id: int
    name: str
    description: str
    price: int


class CatalogProduct(BaseProduct):
    image: str
    sizes: list[str] = []


class Product(BaseProduct):
    category_id: int
    brand_id: int
    color_id: int
    code: int
    article: str
    gender: Gender | None = Gender.unisex
    images: list[str] = []
    category: BaseDataField
    brand: BaseDataField
    color: BaseDataField
    sizes: list[str] = []

    class Config:
        from_attributes = True


class ProductImage(BaseModel):
    id: int
    image: str
    product_id: int
