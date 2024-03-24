from schemas.cart import SCartProduct
from session.cart import Cart


class CartService:
    async def add_product(self, request, product: SCartProduct):
        cart = Cart(request)
        product_dict = product.model_dump()

        cart.add(product=product_dict)

        return {"message": "success"}

    async def get_products(self, request) -> list[SCartProduct]:
        cart = Cart(request)

        serialized_cart = [SCartProduct(**product) for product in cart]

        return serialized_cart

    async def low_quantity(self, request, product: SCartProduct):
        cart = Cart(request)
        product_dict = product.model_dump()

        cart.low_quantity(product=product_dict)

        return {"message": "success"}

    async def clear(self, request):
        cart = Cart(request)
        cart.clear()

        return {"message": "success"}
