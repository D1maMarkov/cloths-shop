from datetime import datetime, timedelta

from jose import jwt
from repositories.user_repository import UserRepository
from settings import get_settings


class AuthService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create_access_token(self, username: str, user_id: int, expires_delta: timedelta):
        encode = {"sub": username, "id": user_id}
        expires = datetime.utcnow() + expires_delta
        encode.update({"exp": expires})
        return jwt.encode(encode, get_settings().SECRET_KEY, algorithm=get_settings().ALGORITHM)

    async def authenticate_user(self, username, password):
        user = await self.repository.authenticate_user(username, password)
        return user
