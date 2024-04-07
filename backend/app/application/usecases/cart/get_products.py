from domain.cart.cart import CartProduct
from infrastructure.persistence.session.cart_adapter import Cart


class GetCart:
    def __init__(self, cart: Cart) -> None:
        self.cart_session = cart

    async def __call__(self) -> list[CartProduct]:
        return [CartProduct(**product) for product in self.cart_session]
