from datetime import datetime, timedelta
from random import randrange

from jose import jwt
from repositories.user_repository import UserRepository
from schemas.user import CreateUserRequest, SUser
from settings import settings
from tasks.tasks import send_mail


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def create_user(self, create_user_request: CreateUserRequest):
        user_id = await self.repository.create_user(create_user_request)
        code = "".join([str(randrange(10)) for _ in range(6)])

        payload = {"user_id": user_id, "code": code, "exp": datetime.utcnow() + timedelta(hours=1)}

        confirm_email_token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

        send_mail.delay(create_user_request.email, code, confirm_email_token)

        return confirm_email_token

    def create_access_token(self, username: str, user_id: int, expires_delta: timedelta):
        encode = {"sub": username, "id": user_id}
        expires = datetime.utcnow() + expires_delta
        encode.update({"exp": expires})
        return jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    async def activate_user(self, user_id: int) -> str:
        user_model = await self.repository.get_user(user_id)
        await self.repository.activate_user(user_id)
        token = self.create_access_token(user_model.username, user_model.id, timedelta(minutes=60))
        return token

    async def get_user_info(self, user_id: int) -> SUser:
        user_model = await self.repository.get_user(user_id)

        user = SUser(**user_model.__dict__)
        return user

    async def authenticate_user(self, username, password):
        user = await self.repository.authenticate_user(username, password)
        return user
