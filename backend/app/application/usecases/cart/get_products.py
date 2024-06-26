from application.common.cart import CartInterface
from domain.cart.cart import CartProduct


class GetCart:
    def __init__(self, cart: CartInterface) -> None:
        self.cart_session = cart

    async def __call__(self) -> list[CartProduct]:
        return [CartProduct(**product) for product in self.cart_session]
