import os
from functools import lru_cache

from application.common.file_service import FileServiceInterface
from fastapi import UploadFile


class FileService(FileServiceInterface):
    def save_file(self, path: str, file: UploadFile) -> None:
        contents = file.file.read()
        if not os.path.exists(path):
            os.makedirs(path)

        with open(path + file.filename, "wb") as f:
            f.write(contents)

        file.file.close()


@lru_cache
def get_file_service() -> FileService:
    return FileService()
