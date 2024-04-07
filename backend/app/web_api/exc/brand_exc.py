from fastapi import HTTPException, status


class BrandNotFound(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="brand with this id not found")


class BrandsImageNotFound(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="brand`s image with this id not found")
