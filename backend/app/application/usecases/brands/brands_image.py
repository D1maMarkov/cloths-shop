from fastapi import UploadFile
from fastapi.responses import FileResponse
from infrastructure.configs.brand_config import BrandSettings
from infrastructure.file_service.file_service import FileService
from infrastructure.persistence.repositories.brand_repository import BrandRepository
from web_api.exc.brand_exc import BrandsImageNotFound


class AddBrandsImage:
    def __init__(self, repository: BrandRepository, file_service: FileService, settings: BrandSettings) -> None:
        self.repository = repository
        self.file_service = file_service
        self.settings = settings

    async def __call__(self, brand_id: int, file: UploadFile) -> None:
        self.file_service.save_file(self.settings.BRANDS_PATH, file)

        return await self.repository.add_image(brand_id=brand_id, filename=file.filename)


class GetBrandsImage:
    def __init__(self, repository: BrandRepository, settings: BrandSettings) -> None:
        self.repository = repository
        self.settings = settings

    async def __call__(self, image_id: int):
        image = await self.repository.get_image(image_id)
        if image is None:
            raise BrandsImageNotFound()

        return FileResponse(self.settings.BRANDS_PATH + image.image)
