from pydantic import BaseModel


class FilterProductsRequest(BaseModel):
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
