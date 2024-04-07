from application.contracts.user.user_info_response import UserInfoResponse
from infrastructure.persistence.repositories.user_repository import UserRepository


class GetUserInfo:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def __call__(self, user_id: int) -> UserInfoResponse:
        user_model = await self.repository.get_user(user_id)

        return UserInfoResponse(**user_model.__dict__)
