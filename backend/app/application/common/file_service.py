from typing import Protocol

from fastapi import UploadFile


class FileServiceInterface(Protocol):
    def save_file(self, path: str, file: UploadFile) -> None:
        raise NotImplementedError
