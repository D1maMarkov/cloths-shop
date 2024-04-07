from typing import Protocol


class CategoriesRepositoryInterface(Protocol):
    async def find_all_categories(self, basic_category: str):
        raise NotImplementedError

    async def add_category(self, data: dict) -> None:
        raise NotImplementedError
