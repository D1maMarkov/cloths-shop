from domain.product.product import CatalogProduct
from application.common.favs import FavsInterface


class GetFavsProducts:
    def __init__(self, favs: FavsInterface) -> None:
        self.favs_session = favs

    async def __call__(self) -> list[CatalogProduct]:
        return [CatalogProduct(**product) for product in self.favs_session]
