from typing import Protocol


class JwtProcessorInterface(Protocol):
    def create_access_token(self, username: str, user_id: int) -> dict:
        raise NotImplementedError

    async def validate_token(self, token: str) -> dict | bool:
        raise NotImplementedError

    async def create_confirm_email_token(self, user_id: int, code: str) -> str:
        raise NotImplementedError
