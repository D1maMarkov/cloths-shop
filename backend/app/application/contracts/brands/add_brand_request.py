from pydantic import BaseModel


class AddBrandRequest(BaseModel):
    name: str
