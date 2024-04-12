from application.contracts.products.price_range_response import PriceRangeResponse
from domain.product.exc import ProductsNotFound
from domain.product.repository import ProductRepositoryInterface


class GetProductsPrices:
    def __init__(self, repository: ProductRepositoryInterface) -> None:
        self.repository = repository

    async def __call__(self) -> PriceRangeResponse:
        prices = await self.repository.get_prices()

        if len(prices) == 0:
            raise ProductsNotFound("no products found")

        return PriceRangeResponse(min_price=min(prices), max_price=max(prices))
