from typing import Protocol

from application.contracts.products.filter_products_request import FilterProductsRequest


class ProductRepositoryInterface(Protocol):
    async def get_prices(self) -> list[int]:
        raise NotImplementedError

    async def get_all_images(self):
        raise NotImplementedError

    async def add_image(self, product_id: int, filename: str):
        raise NotImplementedError

    async def get_image(self, id: int):
        raise NotImplementedError

    async def add_product(self, data: dict) -> None:
        raise NotImplementedError

    async def get_product(self, id: int):
        raise NotImplementedError

    async def get_filtered_products(self, data: FilterProductsRequest):
        raise NotImplementedError

    async def get_all_products(self):
        raise NotImplementedError

    async def get_populars(self):
        raise NotImplementedError

    async def get_new_arrivals(self):
        raise NotImplementedError

    async def get_colors(self, name: str):
        raise NotImplementedError
