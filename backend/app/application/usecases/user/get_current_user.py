from infrastructure.auth.jwt_processor import JwtProcessor
from infrastructure.persistence.repositories.user_repository import UserRepository
from web_api.exc.auth_exc import UserNotFound


class GetCurrentUser:
    def __init__(self, repository: UserRepository, jwt_processor: JwtProcessor) -> None:
        self.repository = repository
        self.jwt_processor = jwt_processor

    async def __call__(self, token: str) -> dict:
        payload = await self.jwt_processor.validate_token(token)
        if not payload:
            raise UserNotFound()

        username: str = payload.get("sub")
        user_id: int = payload.get("id")

        if username is None or user_id is None:
            raise UserNotFound()

        return {"username": username, "id": user_id}
