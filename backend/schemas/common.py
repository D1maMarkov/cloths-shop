from enums import BasicCategory
from pydantic import BaseModel, validator
from utils.get_list_from_json import get_list_from_json


class SBaseDataFieldAdd(BaseModel):
    name: str
    viewed_name: str


class SBaseDataField(SBaseDataFieldAdd):
    id: int | None = None

    class Config:
        from_attributes = True


class SCategoryAdd(SBaseDataFieldAdd):
    basic_category: str


class SCategory(SBaseDataField):
    basic_category: BasicCategory


class SFiltered(BaseModel):
    gender: list[str] = []
    category: list[str] = []
    brand: list[str] = []
    size: list[str] = []
    color: list[str] = []
    price: int
    quantity: int
    pageIndex: int
    orderBy: str
    basicCategory: str

    @validator("gender", pre=True)
    def get_genders(cls, v, values):
        return get_list_from_json(v)

    @validator("category", pre=True)
    def get_categories(cls, v, values):
        return get_list_from_json(v)

    @validator("brand", pre=True)
    def get_brands(cls, v, values):
        return get_list_from_json(v)

    @validator("size", pre=True)
    def get_sizes(cls, v, values):
        return get_list_from_json(v)

    @validator("color", pre=True)
    def get_colors(cls, v, values):
        return get_list_from_json(v)


class SSearch(BaseModel):
    search: str
