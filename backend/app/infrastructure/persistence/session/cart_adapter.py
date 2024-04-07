from infrastructure.persistence.session.sessionObject import SessionObject
from domain.cart.cart import CartProduct
from application.common.cart import CartInterface


secret_key = "cart"


class Cart(SessionObject, CartInterface):
    def __init__(self, request):
        super().__init__(request, secret_key)

    def add_quantity(self, key) -> None:
        self.dict[key]["quantity"] += 1

    def low_quantity(self, key: str) -> None:
        self.dict[key]["quantity"] -= 1

    def get_product(self, key: str) -> CartProduct:
        return CartProduct(**self.dict.get(key))

    def clear(self) -> None:
        del self.session[secret_key]
