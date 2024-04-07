from application.usecases.product.get_products import (
    GetFilteredProducts,
    GetNewArrivals,
    GetPopulars,
    GetProductById,
    GetProductsColors,
    GetSearchedProducts,
)
from fastapi import Depends
from infrastructure.persistence.repositories.product_repository import ProductRepository
from web_api.depends.product.get_repository import get_repository


def get_filtered_interactor(repository: ProductRepository = Depends(get_repository)) -> GetFilteredProducts:
    return GetFilteredProducts(repository)


def get_searched_interactor(repository: ProductRepository = Depends(get_repository)) -> GetSearchedProducts:
    return GetSearchedProducts(repository)


def get_find_product_interactor(repository: ProductRepository = Depends(get_repository)) -> GetProductById:
    return GetProductById(repository)


def get_populars_interactor(repository: ProductRepository = Depends(get_repository)) -> GetPopulars:
    return GetPopulars(repository)


def get_new_arrivals_interactor(repository: ProductRepository = Depends(get_repository)) -> GetNewArrivals:
    return GetNewArrivals(repository)


def get_find_products_colors_interactor(repository: ProductRepository = Depends(get_repository)) -> GetProductsColors:
    return GetProductsColors(repository)
