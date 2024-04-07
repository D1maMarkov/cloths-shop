from application.common.cart import CartInterface


class Clear:
    def __init__(self, cart: CartInterface) -> None:
        self.cart_session = cart

    async def __call__(self) -> None:
        self.cart_session.clear()
