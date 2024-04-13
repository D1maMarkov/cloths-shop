from application.contracts.additional_for_product.add_size_request import AddSizeRequest
from domain.additional_for_product.repository import (
    AdditionalForProductSRepositoryInterface,
)


class AddProductsSize:
    def __init__(self, repository: AdditionalForProductSRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self, size: AddSizeRequest) -> None:
        size_dict = size.model_dump()
        await self.repository.add_size(size_dict)


class GetProductsSizes:
    def __init__(self, repository: AdditionalForProductSRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self) -> list[str]:
        return await self.repository.get_sizes()
