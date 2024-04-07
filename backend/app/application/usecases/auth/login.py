from application.contracts.user.token_response import TokenResponse
from infrastructure.auth.jwt_processor import JwtProcessor
from infrastructure.email_notification.service import EmailNotificationService
from infrastructure.persistence.repositories.user_repository import UserRepository
from infrastructure.security.password_hasher import PasswordHasher
from web_api.exc.auth_exc import UserNotFound


class Login:
    def __init__(
        self,
        repository: UserRepository,
        password_hasher: PasswordHasher,
        jwt_processor: JwtProcessor,
        email_service: EmailNotificationService,
    ) -> None:
        self.repository = repository
        self.password_hasher = password_hasher
        self.jwt_processor = jwt_processor
        self.email_service = email_service

    async def __call__(self, username: str, password: str) -> TokenResponse:
        user = await self.repository.get_user_by_username(username)

        if not user:
            raise UserNotFound()
        if not self.password_hasher.verify(password, user.hashed_password):
            raise UserNotFound()
        if not user.is_active:
            raise UserNotFound()

        token = self.jwt_processor.create_access_token(user.username, user.id)

        return TokenResponse(access_token=token, token_type="bearer")
