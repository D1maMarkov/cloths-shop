from infrastructure.persistence.session.favs_adapter import Favs


class RemoveFromFavs:
    def __init__(self, favs: Favs) -> None:
        self.favs_session = favs

    async def __call__(self, id: str) -> None:
        self.favs_session.remove(id)
