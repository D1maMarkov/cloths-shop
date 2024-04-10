from typing import Annotated

from application.contracts.additional_for_product.add_size_request import AddSizeRequest
from application.contracts.common.base_data_add_request import BaseDataFieldAddRequest
from application.usecases.additional_for_product.color import AddColor, GetColors
from application.usecases.additional_for_product.size import (
    AddProductsSize,
    GetProductsSizes,
)
from domain.common.base_data_field import BaseDataField
from fastapi import APIRouter, Depends, status
from web_api.depends.additional_for_product.color import (
    get_add_color_interactor,
    get_find_colors_interactor,
)
from web_api.depends.additional_for_product.size import (
    get_add_size_interactor,
    get_find_sizes_interactor,
)

router = APIRouter(prefix="/additional-for-products", tags=["additional for products"])


@router.post("/size", status_code=status.HTTP_201_CREATED)
async def add_size(
    size: Annotated[AddSizeRequest, Depends()], add_size_interactor: AddProductsSize = Depends(get_add_size_interactor)
) -> None:
    return await add_size_interactor(size)


@router.get("/sizes", response_model=list[BaseDataField])
async def get_sizes(get_sizes_interactor: GetProductsSizes = Depends(get_find_sizes_interactor)) -> list[BaseDataField]:
    return await get_sizes_interactor()


@router.post("/color", status_code=status.HTTP_201_CREATED)
async def add_color(
    color: Annotated[BaseDataFieldAddRequest, Depends()],
    add_color_interactor: AddColor = Depends(get_add_color_interactor),
) -> None:
    return await add_color_interactor(color)


@router.get("/colors", response_model=list[BaseDataField])
async def get_colors(get_colors_interactor: GetColors = Depends(get_find_colors_interactor)) -> list[BaseDataField]:
    return await get_colors_interactor()
