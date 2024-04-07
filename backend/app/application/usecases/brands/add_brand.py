from application.contracts.brands.add_brand_request import AddBrandRequest
from infrastructure.persistence.repositories.brand_repository import BrandRepository


class AddBrand:
    def __init__(self, repository: BrandRepository) -> None:
        self.repository = repository

    async def __call__(self, data: AddBrandRequest) -> None:
        brand_dict = data.model_dump()

        return await self.repository.add_brand(brand_dict)
