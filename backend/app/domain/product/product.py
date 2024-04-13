from dataclasses import dataclass

from domain.common.base_data_field import BaseDataField
from domain.product.gender_values import Gender


@dataclass
class BaseProduct:
    id: int
    name: str
    description: str
    price: int


@dataclass
class CatalogProduct(BaseProduct):
    image: str
    sizes: list[str]


@dataclass
class Product(BaseProduct):
    code: int
    article: str
    images: list[str]
    category: BaseDataField
    brand: BaseDataField
    color: BaseDataField
    sizes: list[str]
    gender: Gender | None = Gender.unisex


@dataclass
class ProductImage:
    image: str
