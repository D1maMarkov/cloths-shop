from schemas.products import SBaseProduct
from session.favs import Favs


class FavsService:
    async def add_product(self, request, product: SBaseProduct):
        favs = Favs(request)
        product_dict = product.model_dump()

        favs.add(product=product_dict)

        return {"message": "success"}

    async def get_products(self, request) -> list[SBaseProduct]:
        favs = Favs(request)

        serialized_favs = [SBaseProduct(**product) for product in favs]

        return serialized_favs

    async def remove(self, request, id: int):
        favs = Favs(request)
        favs.remove(product_id=id)

        return {"message": "success"}
