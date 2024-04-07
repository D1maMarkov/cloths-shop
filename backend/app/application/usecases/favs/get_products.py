from domain.product.product import CatalogProduct
from infrastructure.persistence.session.favs_adapter import Favs


class GetFavsProducts:
    def __init__(self, favs: Favs) -> None:
        self.favs_session = favs

    async def __call__(self) -> list[CatalogProduct]:
        return [CatalogProduct(**product) for product in self.favs_session]
