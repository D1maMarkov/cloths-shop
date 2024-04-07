from application.usecases.product.add_product import AddProduct
from fastapi import Depends
from infrastructure.persistence.repositories.product_repository import ProductRepository
from web_api.depends.product.get_repository import get_repository


def get_add_product_interactor(repository: ProductRepository = Depends(get_repository)) -> AddProduct:
    return AddProduct(repository)
