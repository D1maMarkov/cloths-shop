from infrastructure.persistence.session.sessionObject import SessionObject
from application.common.favs import FavsInterface


secret_key = "favs"


class Favs(SessionObject, FavsInterface):
    def __init__(self, request) -> None:
        super().__init__(request, secret_key)
