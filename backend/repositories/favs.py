from schemas.products import SProduct
from session.favs import Favs


class FavsRepository:
    @classmethod
    async def add_product(cls, request, product: SProduct):
        favs = Favs(request)
        product_dict = product.model_dump()
        
        await favs.add(product=product_dict)

        return {"message": "success"}

    @classmethod
    async def get_products(cls, request) -> list[SProduct]:
        favs = Favs(request)
        
        serialized_favs = [SProduct(**product) for product in favs]

        return serialized_favs
    
    @classmethod
    async def remove(cls, request, id: int):
        favs = Favs(request)
        favs.remove(product_id=id)
        
        return {"message": "success"}