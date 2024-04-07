from typing import Protocol


class UserRepositoryInterface(Protocol):
    async def delete_user(self, user_id: int):
        raise NotImplementedError

    async def create_user(self, create_user_request: dict):
        raise NotImplementedError

    async def get_user_by_username(self, username: str):
        raise NotImplementedError

    async def get_user_by_email(self, email: str):
        raise NotImplementedError

    async def activate_user(self, user_id: int):
        raise NotImplementedError

    async def get_user(self, user_id: int):
        raise NotImplementedError

    async def delete_inactive_users(self):
        raise NotImplementedError
