from domain.product.product import BaseProduct
from infrastructure.persistence.session.favs_adapter import Favs


class AddInFavs:
    def __init__(self, favs: Favs) -> None:
        self.favs_session = favs

    async def __call__(self, product: BaseProduct) -> None:
        product_id = str(product.id)

        self.favs_session.add_product(product_id, product.__dict__)
