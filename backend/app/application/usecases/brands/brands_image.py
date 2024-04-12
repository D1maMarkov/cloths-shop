from application.common.file_service import FileServiceInterface
from domain.brand.exc import BrandsImageNotFound
from domain.brand.repository import BrandRepositoryInterface
from fastapi import UploadFile
from fastapi.responses import FileResponse
from infrastructure.configs.brand_config import BrandSettings


class AddBrandsImage:
    def __init__(
        self, repository: BrandRepositoryInterface, file_service: FileServiceInterface, settings: BrandSettings
    ) -> None:
        self.repository = repository
        self.file_service = file_service
        self.settings = settings

    async def __call__(self, brand_id: int, file: UploadFile) -> None:
        self.file_service.save_file(self.settings.BRANDS_PATH, file)

        return await self.repository.add_image(brand_id=brand_id, filename=file.filename)


class GetBrandsImage:
    def __init__(self, repository: BrandRepositoryInterface, settings: BrandSettings) -> None:
        self.repository = repository
        self.settings = settings

    async def __call__(self, image_id: int):
        image = await self.repository.get_image(image_id)
        if image is None:
            raise BrandsImageNotFound("brand`s image with this id not found")

        return FileResponse(self.settings.BRANDS_PATH + image.image)
