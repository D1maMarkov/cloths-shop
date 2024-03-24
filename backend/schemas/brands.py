from pydantic import BaseModel, validator
from settings import settings


class SBrandAdd(BaseModel):
    name: str


class SBrand(SBrandAdd):
    id: int
    viewed_name: str


class SPaginateBrand(SBrandAdd):
    id: int
    image: str | None = None

    @validator("image", pre=True)
    def get_image(cls, v, values):
        if len(v) == 0:
            return ""

        return f"{settings.HOST}/brands/image/{v[0].id}"
