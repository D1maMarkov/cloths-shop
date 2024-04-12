from application.common.file_service import FileServiceInterface
from domain.product.exc import ProductsImageNotFound
from domain.product.repository import ProductRepositoryInterface
from fastapi import UploadFile
from fastapi.responses import FileResponse
from infrastructure.configs.product_config import ProductSettings


class AddProductsImage:
    def __init__(
        self, repository: ProductRepositoryInterface, file_service: FileServiceInterface, settings: ProductSettings
    ) -> None:
        self.repository = repository
        self.file_service = file_service
        self.settings = settings

    async def __call__(self, product_id: int, file: UploadFile) -> str:
        self.file_service.save_file(self.settings.PRODUCTS_PATH, file)

        return await self.repository.add_image(product_id=product_id, filename=file.filename)


class GetProductsImage:
    def __init__(self, repository: ProductRepositoryInterface, settings: ProductSettings) -> None:
        self.repository = repository
        self.settings = settings

    async def __call__(self, image_id: int) -> FileResponse:
        image = await self.repository.get_image(image_id)
        if image is None:
            raise ProductsImageNotFound("product`s image with this id not found")

        return FileResponse(self.settings.PRODUCTS_PATH + image.image)
