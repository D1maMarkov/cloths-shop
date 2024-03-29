from datetime import datetime, timedelta
from random import randrange

from jose import jwt
from repositories.user_repository import UserRepository
from schemas.user import CreateUserRequest, SUser
from settings import get_settings
from tasks.tasks import send_mail


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def create_user(self, create_user_request: CreateUserRequest):
        user_id = await self.repository.create_user(create_user_request)
        code = str(randrange(100000, 1000000))

        payload = {"user_id": user_id, "code": code, "exp": datetime.utcnow() + timedelta(hours=1)}

        confirm_email_token = jwt.encode(payload, get_settings().SECRET_KEY, algorithm=get_settings().ALGORITHM)

        send_mail.delay(create_user_request.email, code, confirm_email_token)

        return confirm_email_token

    async def get_user(self, user_id: int) -> SUser:
        user_model = await self.repository.get_user(user_id)

        user = SUser(**user_model.__dict__)
        return user

    async def activate_user(self, user_id: int) -> None:
        await self.repository.activate_user(user_id)
