from application.usecases.product.get_prices import GetProductsPrices
from fastapi import Depends
from infrastructure.persistence.repositories.product_repository import ProductRepository
from web_api.depends.product.get_repository import get_repository


def get_price_range_interactor(repository: ProductRepository = Depends(get_repository)) -> GetProductsPrices:
    return GetProductsPrices(repository)
