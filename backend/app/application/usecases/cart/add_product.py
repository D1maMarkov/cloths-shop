from domain.cart.cart import CartProduct
from application.common.cart import CartInterface


class AddProduct:
    def __init__(self, cart: CartInterface) -> None:
        self.cart_session = cart

    async def __call__(self, product: CartProduct) -> None:
        key = ",".join([str(product.id), product.size])

        if key not in self.cart_session:
            self.cart_session.add_product(key, product.__dict__)
        else:
            self.cart_session.add_quantity(key)
