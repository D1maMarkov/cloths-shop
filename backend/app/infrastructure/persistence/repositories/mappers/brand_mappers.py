from domain.brand.brand import Brand, PaginateBrand
from infrastructure.persistence.models.brand_models import BrandImageOrm, BrandOrm
from web_api.config import get_settings


def from_orm_to_image(images: BrandImageOrm | None | list = None) -> str | None:
    if images is None or images == []:
        return None

    return f"{get_settings().HOST}/brands/image/{images[0].id}"


def from_orm_to_paginate_brand(brand: BrandOrm) -> PaginateBrand:
    return PaginateBrand(id=brand.id, image=from_orm_to_image(brand.image))


def from_orm_to_brand(brand: BrandOrm) -> Brand:
    return Brand(id=brand.id, name=brand.name, viewed_name=brand.name)
