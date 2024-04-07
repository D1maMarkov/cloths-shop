from application.contracts.brands.add_brand_request import AddBrandRequest
from domain.brand.repository import BrandRepositoryInterface


class AddBrand:
    def __init__(self, repository: BrandRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self, data: AddBrandRequest) -> None:
        brand_dict = data.model_dump()

        return await self.repository.add_brand(brand_dict)
