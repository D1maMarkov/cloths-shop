from .sessionObject import SessionObject

secret_key = "cart"


class Cart(SessionObject):
    def __init__(self, request):
        super().__init__(request, secret_key)

    def add(self, product):
        key = ",".join([str(product["id"]), product["size"]])
        if key not in self.dict:
            self.dict[key] = product
        else:
            self.dict[key]["quantity"] += 1

    def low_quantity(self, product):
        key = ",".join([str(product["id"]), product["size"]])
        self.dict[key]["quantity"] -= 1

        if self.dict[key]["quantity"] <= 0:
            self.remove(key)

    def remove(self, key):
        if key in self.dict:
            del self.dict[key]

    def clear(self):
        del self.session[secret_key]
