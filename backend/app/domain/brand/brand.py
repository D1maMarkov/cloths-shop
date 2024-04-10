from pydantic import BaseModel


class Brand(BaseModel):
    name: str
    viewed_name: str


class PaginateBrand(BaseModel):
    image: str | None = None
