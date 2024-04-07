from application.contracts.products.add_product_request import AddProductRequest
from infrastructure.persistence.repositories.product_repository import ProductRepository


class AddProduct:
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    async def __call__(self, data: AddProductRequest) -> None:
        product_dict = data.model_dump()
        return await self.repository.add_product(product_dict)
