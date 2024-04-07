from application.contracts.common.base_data_add_request import BaseDataFieldAddRequest
from domain.additional_for_product.repository import (
    AdditionalForProductSRepositoryInterface,
)
from domain.common.base_data_field import BaseDataField


class AddColor:
    def __init__(self, repository: AdditionalForProductSRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self, color: BaseDataFieldAddRequest) -> None:
        color_dict = color.model_dump()
        await self.repository.add_color(color_dict)


class GetColors:
    def __init__(self, repository: AdditionalForProductSRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self) -> list[BaseDataField]:
        color_models = await self.repository.get_colors()

        return [BaseDataField(**color.__dict__) for color in color_models]
