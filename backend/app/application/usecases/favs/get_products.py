from application.common.favs import FavsInterface
from domain.product.product import CatalogProduct


class GetFavsProducts:
    def __init__(self, favs: FavsInterface) -> None:
        self.favs_session = favs

    async def __call__(self) -> list[CatalogProduct]:
        return [CatalogProduct(**product) for product in self.favs_session]
