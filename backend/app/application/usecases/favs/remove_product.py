from application.common.favs import FavsInterface


class RemoveFromFavs:
    def __init__(self, favs: FavsInterface) -> None:
        self.favs_session = favs

    async def __call__(self, id: str) -> None:
        self.favs_session.remove(id)
