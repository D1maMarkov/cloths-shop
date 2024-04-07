from typing import Protocol

from domain.common.base_data_field import BaseDataField


class AdditionalForProductSRepositoryInterface(Protocol):
    async def add_size(self, size: dict) -> None:
        raise NotImplementedError

    async def get_sizes(self) -> list[str]:
        raise NotImplementedError

    async def add_color(self, color: dict) -> None:
        raise NotImplementedError

    async def get_colors(self) -> list[BaseDataField]:
        raise NotImplementedError
