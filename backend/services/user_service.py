import smtplib
from datetime import datetime, timedelta
from email.message import EmailMessage
from random import randrange

from jose import jwt
from repositories.user_repository import UserRepository
from schemas.user import CreateUserRequest, SUser
from settings import settings


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def create_user(self, create_user_request: CreateUserRequest):
        user_id = await self.repository.create_user(create_user_request)
        code = "".join([str(randrange(10)) for _ in range(6)])

        payload = {"user_id": user_id, "code": code, "exp": datetime.utcnow() + timedelta(hours=1)}

        confirm_email_token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

        await self.send_mail(create_user_request.email, code, confirm_email_token)

        return confirm_email_token

    async def send_mail(self, email, code, token):
        msg = EmailMessage()
        msg["Subject"] = "verification code for confirm your email"
        msg["From"] = settings.BACKEND_EMAIL
        msg["To"] = email  # type Email

        msg.set_content(
            f"""\
            ссылка для подтверждения почты: http:127.0.0.1:4000/confirm-email/{token} \n

        код для подтверждения почты: {code}
        """,
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(settings.BACKEND_EMAIL, settings.BACKEND_EMAIL_PASSWORD)
            smtp.send_message(msg)

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
