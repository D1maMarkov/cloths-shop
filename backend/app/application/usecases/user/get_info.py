from application.contracts.user.user_info_response import UserInfoResponse
from infrastructure.persistence.repositories.mappers.user_mapper import from_orm_to_user
from infrastructure.persistence.repositories.user_repository import UserRepository


class GetUserInfo:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def __call__(self, user_id: int) -> UserInfoResponse:
        user_model = await self.repository.get_user(user_id)
        return from_orm_to_user(user_model)
