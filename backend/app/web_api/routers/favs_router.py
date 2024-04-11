from application.contracts.favs.add_product_request import AddProductInFavsRequest
from application.usecases.favs.add_product import AddInFavs
from application.usecases.favs.get_products import GetFavsProducts
from application.usecases.favs.remove_product import RemoveFromFavs
from domain.product.product import CatalogProduct
from fastapi import APIRouter, Depends
from web_api.depends.favs import (
    get_add_in_favs_interactor,
    get_find_products_in_favs_interactor,
    get_remove_from_favs_interactor,
)

router = APIRouter(prefix="/favs", tags=["favs"])


@router.post("/")
async def favs_add(
    product: AddProductInFavsRequest, add_in_favs_interactor: AddInFavs = Depends(get_add_in_favs_interactor)
) -> None:
    return await add_in_favs_interactor(product)


@router.get("/", response_model=list[CatalogProduct])
async def favs_get(
    get_favs_products: GetFavsProducts = Depends(get_find_products_in_favs_interactor),
) -> list[CatalogProduct]:
    return await get_favs_products()


@router.get("/remove/{id}")
async def remove(
    id: str, remove_from_favs_interactor: RemoveFromFavs = Depends(get_remove_from_favs_interactor)
) -> None:
    return await remove_from_favs_interactor(id)
