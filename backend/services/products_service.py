import os

from fastapi import UploadFile
from fastapi.responses import FileResponse
from repositories.products_repository import ProductRepository
from schemas.common import SFiltered
from schemas.products import SProduct, SProductAdd
from settings import get_settings


class ProductService:
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    async def add_one_product(self, data: SProductAdd) -> list[int]:
        product_dict = data.model_dump()
        ids = await self.repository.add_one_product(product_dict)

        return ids

    async def get_filtered_products(self, data: SFiltered) -> list[SProduct]:
        product_models = await self.repository.get_filtered_products(data=data)

        products = [SProduct(**product.__dict__) for product in product_models]

        return products

    async def get_price_range(self) -> list[int]:
        prices = await self.repository.get_prices()

        return [min(prices), max(prices)]

    async def add_image(self, product_id: int, file: UploadFile):
        contents = file.file.read()

        if not os.path.exists(get_settings().PRODUCTS_PATH):
            os.makedirs(get_settings().PRODUCTS_PATH)

        with open(get_settings().PRODUCTS_PATH + file.filename, "wb") as f:
            f.write(contents)

        file.file.close()

        message = await self.repository.add_image(product_id=product_id, filename=file.filename)

        return message

    async def get_image(self, image_id: int):
        image = await self.repository.get_image(id=image_id)

        return FileResponse(get_settings().PRODUCTS_PATH + image.image)

    async def get_searched_products(self, search: str) -> list[SProduct]:
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

        products = [SProduct(**product.__dict__) for product in products]

        return products

    async def get_colors(self, name) -> list[SProduct]:
        product_models = await self.repository.get_colors(name=name)
        products = [SProduct(**product.__dict__) for product in product_models]

        return products

    async def get_new_arrivals(self) -> list[SProduct]:
        product_models = await self.repository.get_new_arrivals()
        products = [SProduct(**product.__dict__) for product in product_models]

        return products

    async def get_populars(self) -> list[SProduct]:
        product_models = await self.repository.get_populars()
        products = [SProduct(**product.__dict__) for product in product_models]

        return products

    async def get_product(self, id) -> SProduct:
        product_model = await self.repository.get_product(id=id)
        product = SProduct(**product_model.__dict__)

        return product
