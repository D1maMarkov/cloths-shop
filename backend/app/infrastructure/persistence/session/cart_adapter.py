from infrastructure.persistence.session.sessionObject import SessionObject

secret_key = "cart"


class Cart(SessionObject):
    def __init__(self, request):
        super().__init__(request, secret_key)

    def add_quantity(self, key) -> None:
        self.dict[key]["quantity"] += 1

    def low_quantity(self, key: str) -> None:
        self.dict[key]["quantity"] -= 1

    def get_product(self, key: str) -> dict:
        return self.dict.get(key)

    def clear(self) -> None:
        del self.session[secret_key]
