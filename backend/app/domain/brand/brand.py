from pydantic import BaseModel


class Brand(BaseModel):
    id: int
    name: str
    viewed_name: str


class PaginateBrand(BaseModel):
    id: int
    image: str | None = None
