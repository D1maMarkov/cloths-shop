from random import randrange

from application.common.email_notification import EmailNotificationServiceInterface
from application.common.jwt_processor import JwtProcessorInterface
from application.common.password_hasher import PasswordHasherInterface
from application.contracts.user.create_user_request import CreateUserRequest
from application.contracts.user.token_response import TokenResponse
from domain.user.repository import UserRepositoryInterface
from web_api.exc.user_exc import UserWithEmailAlreadyExist, UserWithUsernameAlreadyExist


class Register:
    def __init__(
        self,
        repository: UserRepositoryInterface,
        password_hasher: PasswordHasherInterface,
        jwt_processor: JwtProcessorInterface,
        email_service: EmailNotificationServiceInterface,
    ) -> None:
        self.repository = repository
        self.password_hasher = password_hasher
        self.jwt_processor = jwt_processor
        self.email_service = email_service

    async def __call__(self, create_user_request: CreateUserRequest) -> TokenResponse:
        user_by_username = await self.repository.get_user_by_username(create_user_request.username)
        if user_by_username:
            raise UserWithUsernameAlreadyExist()

        user_by_email = await self.repository.get_user_by_email(create_user_request.email)
        if user_by_email:
            raise UserWithEmailAlreadyExist()

        create_user_request_dict = {
            "username": create_user_request.username,
            "email": create_user_request.email,
            "hashed_password": self.password_hasher.hash_password(create_user_request.password),
        }

        user_id = await self.repository.create_user(create_user_request_dict)

        code = str(randrange(100000, 1000000))
        confirm_email_token = await self.jwt_processor.create_confirm_email_token(user_id, code)

        self.email_service.send_mail(email=create_user_request.email, code=code, token=confirm_email_token)

        return TokenResponse(access_token=confirm_email_token, token_type="bearer")
