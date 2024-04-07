from application.common.jwt_processor import JwtProcessorInterface
from application.common.password_hasher import PasswordHasherInterface
from application.contracts.user.token_response import TokenResponse
from domain.user.repository import UserRepositoryInterface
from web_api.exc.auth_exc import UserNotFound


class Login:
    def __init__(
        self,
        repository: UserRepositoryInterface,
        password_hasher: PasswordHasherInterface,
        jwt_processor: JwtProcessorInterface,
    ) -> None:
        self.repository = repository
        self.password_hasher = password_hasher
        self.jwt_processor = jwt_processor

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
