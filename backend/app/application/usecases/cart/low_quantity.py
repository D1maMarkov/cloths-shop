from application.common.cart import CartInterface
from domain.cart.cart import CartProduct


class LowQuantity:
    def __init__(self, cart: CartInterface) -> None:
        self.cart_session = cart

    async def __call__(self, product: CartProduct) -> None:
        key = ",".join([str(product.id), product.size])

        cart_product = self.cart_session.get_product(key)

        if cart_product.quantity > 1:
            self.cart_session.low_quantity(key)
        else:
            self.cart_session.remove(key)
