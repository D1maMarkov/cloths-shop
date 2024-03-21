from pydantic import BaseModel
from typing import Optional


class SBrandAdd(BaseModel):
    name: str

class SBrand(SBrandAdd):
    id: int
    viewed_name: str

class SPaginateBrand(SBrandAdd):
    id: int
    image: Optional[str] = None