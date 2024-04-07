from domain.additional_for_product.products_size import Size
from domain.common.base_data_field import BaseDataField
from infrastructure.persistence.repositories.additional_for_products_repository import (
    AdditionalForProductSRepository,
)


class AddProductsSize:
    def __init__(self, repository: AdditionalForProductSRepository) -> None:
        self.repository = repository

    async def __call__(self, size: Size) -> None:
        size_dict = size.model_dump()
        await self.repository.add_size(size_dict)


class GetProductsSizes:
    def __init__(self, repository: AdditionalForProductSRepository) -> None:
        self.repository = repository

    async def __call__(self) -> list[BaseDataField]:
        sizes = await self.repository.get_sizes()

        return [BaseDataField(name=size, viewed_name=size) for size in sizes]
