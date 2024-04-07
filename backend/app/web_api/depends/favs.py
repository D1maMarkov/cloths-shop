from application.usecases.favs.add_product import AddInFavs
from application.usecases.favs.get_products import GetFavsProducts
from application.usecases.favs.remove_product import RemoveFromFavs
from fastapi import Depends, Request
from infrastructure.persistence.session.favs_adapter import Favs


def get_favs(request: Request) -> Favs:
    return Favs(request)


def get_add_in_favs_interactor(favs: Favs = Depends(get_favs)) -> AddInFavs:
    return AddInFavs(favs)


def get_find_products_in_favs_interactor(favs: Favs = Depends(get_favs)) -> GetFavsProducts:
    return GetFavsProducts(favs)


def get_remove_from_favs_interactor(favs: Favs = Depends(get_favs)) -> RemoveFromFavs:
    return RemoveFromFavs(favs)
