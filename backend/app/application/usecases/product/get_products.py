from application.contracts.products.filter_products_request import FilterProductsRequest
from domain.product.product import CatalogProduct, Product
from domain.product.repository import ProductRepositoryInterface
from infrastructure.persistence.repositories.mappers.product_mappers import (
    from_orm_to_catalog_product,
)


class GetFilteredProducts:
    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self, data: FilterProductsRequest) -> list[CatalogProduct]:
        return await self.repository.get_filtered_products(data)


class GetSearchedProducts:
    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self, search: str) -> list[CatalogProduct]:
        product_models = await self.repository.get_all_products()

        search = search.lower()
        products = []
        for product in product_models:
            if (
                search in product.category.name.lower()
                or search in product.category.viewed_name.lower()
                or search in product.name.lower()
                or search in product.description.lower()
                or search in product.brand.name.lower()
            ):
                products.append(product)

        return [from_orm_to_catalog_product(product) for product in products]


class GetProductById:
    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self, id: int) -> Product:
        return await self.repository.get_product(id)


class GetProductsColors:
    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self, name: str) -> list[CatalogProduct]:
        return await self.repository.get_colors(name)


class GetNewArrivals:
    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self) -> list[Product]:
        return await self.repository.get_new_arrivals()


class GetPopulars:
    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self) -> list[CatalogProduct]:
        return await self.repository.get_populars()
