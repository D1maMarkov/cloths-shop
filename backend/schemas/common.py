from pydantic import BaseModel
from typing import Optional


class SBaseDataFieldAdd(BaseModel):
    name: str
    viewed_name: str

class SBaseDataField(SBaseDataFieldAdd):
    id: Optional[int] = None

    class Config:
        from_attributes = True

class SCategoryAdd(SBaseDataFieldAdd):
    basic_category: str
    
class SCategory(SBaseDataField):
    basic_category: str

class SFiltered(BaseModel):
    gender: str
    category: str
    brand: str
    size: str
    color: str
    price: int
    quantity: int
    pageIndex: int
    orderBy: str
    basicCategory: str

class SSearch(BaseModel):
    search: str