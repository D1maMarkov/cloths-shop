from domain.brand.brand import Brand, PaginateBrand
from domain.brand.repository import BrandRepositoryInterface


class GetAllBrands:
    def __init__(self, repository: BrandRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self) -> list[Brand]:
        brand_models = await self.repository.find_all_brands()

        return [Brand(**brand.__dict__, viewed_name=brand.name) for brand in brand_models]


class GetAllPaginateBrands:
    def __init__(self, repository: BrandRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self) -> list[PaginateBrand]:
        return await self.repository.get_paginate_brands()
