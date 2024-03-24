from repositories.additional_for_products_repository import (
    AdditionalForProductSRepository,
)
from schemas.common import SBaseDataField, SBaseDataFieldAdd
from schemas.products import SSize


class AdditionalForProductService:
    def __init__(self, repository: AdditionalForProductSRepository) -> None:
        self.repository = repository

    async def get_colors(self) -> list[SBaseDataField]:
        color_models = await self.repository.get_colors()
        colors = [SBaseDataField(**color.__dict__) for color in color_models]

        return colors

    async def add_color(self, color: SBaseDataFieldAdd):
        color_dict = color.model_dump()
        await self.repository.add_color(color=color_dict)

        return {"message": "success"}

    async def get_sizes(self) -> list[SBaseDataField]:
        sizes = await self.repository.get_sizes()
        sizes = [SBaseDataField(name=size, viewed_name=size) for size in sizes]

        return sizes

    async def add_size(self, size: SSize):
        size_dict = size.model_dump()

        await self.repository.add_size(size_dict)

        return {"message": "success"}
