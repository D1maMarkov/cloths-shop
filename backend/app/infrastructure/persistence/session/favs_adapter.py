from infrastructure.persistence.session.sessionObject import SessionObject

secret_key = "favs"


class Favs(SessionObject):
    def __init__(self, request) -> None:
        super().__init__(request, secret_key)
