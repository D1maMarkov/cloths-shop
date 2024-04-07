from pydantic import BaseModel


class BaseDataFieldAdd(BaseModel):
    name: str
    viewed_name: str


class BaseDataField(BaseDataFieldAdd):
    id: int | None = None

    class Config:
        from_attributes = True
