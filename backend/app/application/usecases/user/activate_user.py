from application.contracts.user.token_response import TokenResponse
from infrastructure.auth.jwt_processor import JwtProcessor
from infrastructure.persistence.repositories.user_repository import UserRepository


class ActivateUser:
    def __init__(
        self,
        repository: UserRepository,
        jwt_processor: JwtProcessor,
    ) -> None:
        self.repository = repository
        self.jwt_processor = jwt_processor

    async def __call__(self, user_id: int) -> TokenResponse:
        await self.repository.activate_user(user_id)
        user_model = await self.repository.get_user(user_id)

        token = self.jwt_processor.create_access_token(user_model.username, user_model.id)

        return TokenResponse(access_token=token, token_type="bearer")
