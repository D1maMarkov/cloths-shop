from fastapi import UploadFile
from fastapi.responses import FileResponse
from infrastructure.configs.product_config import ProductSettings
from infrastructure.file_service.file_service import FileService
from infrastructure.persistence.repositories.product_repository import ProductRepository
from web_api.exc.product_exc import ProductsImageNotFound


class AddProductsImage:
    def __init__(self, repository: ProductRepository, file_service: FileService, settings: ProductSettings) -> None:
        self.repository = repository
        self.file_service = file_service
        self.settings = settings

    async def __call__(self, product_id: int, file: UploadFile) -> str:
        self.file_service.save_file(self.settings.PRODUCTS_PATH, file)

        return await self.repository.add_image(product_id=product_id, filename=file.filename)


class GetProductsImage:
    def __init__(self, repository: ProductRepository, settings: ProductSettings) -> None:
        self.repository = repository
        self.settings = settings

    async def __call__(self, image_id: int) -> FileResponse:
        image = await self.repository.get_image(image_id)
        if image is None:
            raise ProductsImageNotFound()

        return FileResponse(self.settings.PRODUCTS_PATH + image.image)
