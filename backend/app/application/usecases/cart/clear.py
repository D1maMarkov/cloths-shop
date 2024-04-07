from infrastructure.persistence.session.cart_adapter import Cart


class Clear:
    def __init__(self, cart: Cart) -> None:
        self.cart_session = cart

    async def __call__(self) -> None:
        self.cart_session.clear()
