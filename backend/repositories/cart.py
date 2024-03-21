from schemas.cart import SCartProduct
from session.cart import Cart


class CartRepository:
    @classmethod
    async def add_product(cls, request, product: SCartProduct):
        cart = Cart(request)
        product_dict = product.model_dump()
        
        cart.add(product=product_dict)

        return {"message": "success"}

    @classmethod
    async def get_products(cls, request) -> list[SCartProduct]:
        cart = Cart(request)

        serialized_cart = [SCartProduct(**product) for product in cart]

        return serialized_cart
    
    @classmethod
    async def low_quantity(cls, request, product: SCartProduct):
        cart = Cart(request)
        product_dict = product.model_dump()
        
        cart.low_quantity(product=product_dict)
        
        return {"message": "success"}
    
    @classmethod
    async def remove(cls, request, product: SCartProduct):
        cart = Cart(request)
        product_dict = product.model_dump()
        
        cart.remove(product=product_dict)
        
        return {"message": "success"}

    @classmethod
    async def clear(cls, request):
        cart = Cart(request)
        cart.clear()
        
        return {"message": "success"}