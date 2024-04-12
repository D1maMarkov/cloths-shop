from application.common.jwt_processor import JwtProcessorInterface
from domain.user.exc import UserNotFound
from infrastructure.persistence.repositories.user_repository import UserRepository


class GetCurrentUser:
    def __init__(self, repository: UserRepository, jwt_processor: JwtProcessorInterface) -> None:
        self.repository = repository
        self.jwt_processor = jwt_processor

    async def __call__(self, token: str) -> dict:
        payload = await self.jwt_processor.validate_token(token)
        if not payload:
            raise UserNotFound("Could not validate user")

        username: str = payload.get("sub")
        user_id: int = payload.get("id")

        if username is None or user_id is None:
            raise UserNotFound("Could not validate user")

        return {"username": username, "id": user_id}
