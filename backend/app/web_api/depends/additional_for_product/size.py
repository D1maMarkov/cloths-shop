from application.usecases.additional_for_product.size import (
    AddProductsSize,
    GetProductsSizes,
)
from fastapi import Depends
from infrastructure.persistence.repositories.additional_for_products_repository import (
    AdditionalForProductSRepository,
)
from web_api.depends.additional_for_product.get_repository import get_repository


async def get_add_size_interactor(
    repository: AdditionalForProductSRepository = Depends(get_repository),
) -> AddProductsSize:
    return AddProductsSize(repository)


async def get_find_sizes_interactor(
    repository: AdditionalForProductSRepository = Depends(get_repository),
) -> GetProductsSizes:
    return GetProductsSizes(repository)
