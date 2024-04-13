from domain.brand.brand import Brand, PaginateBrand
from domain.brand.repository import BrandRepositoryInterface


class GetAllBrands:
    def __init__(self, repository: BrandRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self) -> list[Brand]:
        return await self.repository.find_all_brands()


class GetAllPaginateBrands:
    def __init__(self, repository: BrandRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self) -> list[PaginateBrand]:
        return await self.repository.get_paginate_brands()
