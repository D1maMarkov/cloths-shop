from schemas.products import SBaseProduct
from session.favs import Favs


class FavsRepository:
    @classmethod
    async def add_product(cls, request, product: SBaseProduct):
        favs = Favs(request)
        product_dict = product.model_dump()
        
        favs.add(product=product_dict)

        return {"message": "success"}

    @classmethod
    async def get_products(cls, request) -> list[SBaseProduct]:
        favs = Favs(request)

        serialized_favs = [SBaseProduct(**product) for product in favs]
        
        return serialized_favs
    
    @classmethod
    async def remove(cls, request, id: int):
        favs = Favs(request)
        favs.remove(product_id=id)
        
        return {"message": "success"}