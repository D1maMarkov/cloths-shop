from application.usecases.product.products_image import (
    AddProductsImage,
    GetProductsImage,
)
from fastapi import Depends
from infrastructure.configs.product_config import ProductSettings, get_settings
from infrastructure.file_service.file_service import FileService, get_file_service
from infrastructure.persistence.repositories.product_repository import ProductRepository
from web_api.depends.product.get_repository import get_repository


def get_add_products_image_interactor(
    repository: ProductRepository = Depends(get_repository),
    products_settings: ProductSettings = Depends(get_settings),
    file_service: FileService = Depends(get_file_service),
) -> AddProductsImage:
    return AddProductsImage(repository, file_service, products_settings)


def get_show_products_image_interactor(
    repository: ProductRepository = Depends(get_repository), products_settings: ProductSettings = Depends(get_settings)
) -> GetProductsImage:
    return GetProductsImage(repository, products_settings)
