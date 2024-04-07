from fastapi import Request


class SessionObject:
    def __init__(self, request: Request, secret_key: str) -> None:
        self.session = request.session
        dict = self.session.get(secret_key)

        if not dict:
            dict = self.session[secret_key] = {}

        # dict = self.session[secret_key] = {}

        self.dict = dict

    def __contains__(self, key: str) -> bool:
        return key in self.dict

    def __iter__(self):
        dict = self.dict.copy()

        yield from dict.values()

    def add_product(self, key: str, product: dict) -> None:
        self.dict[key] = product

    def remove(self, key: str) -> None:
        print(self.dict)
        print(key)
        if key in self.dict:
            del self.dict[key]
