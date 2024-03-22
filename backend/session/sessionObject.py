class SessionObject:
    def __init__(self, request, secret_key):
        self.session = request.session
        dict = self.session.get(secret_key)

        if not dict:
            dict = self.session[secret_key] = {}

        #dict = self.session[secret_key] = {}

        self.dict = dict

    def __iter__(self):
        dict = self.dict.copy()
      
        for item in dict.values():
            yield item

    def add(self, product):
        product_id = str(product["id"])
        self.dict[product_id] = product

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.dict:
            del self.dict[product_id]