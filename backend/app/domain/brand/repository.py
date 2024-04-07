from typing import Protocol


class BrandRepositoryInterface(Protocol):
    async def add_brand(self, data: dict) -> None:
        raise NotImplementedError

    async def add_image(self, brand_id: int, filename: str) -> None:
        raise NotImplementedError

    async def get_image(self, image_id: int):
        raise NotImplementedError

    async def find_all_brands(self):
        raise NotImplementedError

    async def get_paginate_brands(self):
        raise NotImplementedError
