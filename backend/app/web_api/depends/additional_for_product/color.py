from application.usecases.additional_for_product.color import AddColor, GetColors
from fastapi import Depends
from infrastructure.persistence.repositories.additional_for_products_repository import (
    AdditionalForProductSRepository,
)
from web_api.depends.additional_for_product.get_repository import get_repository


async def get_add_color_interactor(repository: AdditionalForProductSRepository = Depends(get_repository)) -> AddColor:
    return AddColor(repository)


async def get_find_colors_interactor(
    repository: AdditionalForProductSRepository = Depends(get_repository),
) -> GetColors:
    return GetColors(repository)
