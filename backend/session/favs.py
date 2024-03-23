from .sessionObject import SessionObject

secret_key='favs'

class Favs(SessionObject):
    def __init__(self, request):
        super().__init__(request, secret_key)

    def add(self, product):
        product_id = str(product["id"])
        self.dict[product_id] = product