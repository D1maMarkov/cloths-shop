from application.contracts.products.add_product_request import AddProductRequest
from domain.product.repository import ProductRepositoryInterface


class AddProduct:
    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self, data: AddProductRequest) -> None:
        product_dict = data.model_dump()
        return await self.repository.add_product(product_dict)
