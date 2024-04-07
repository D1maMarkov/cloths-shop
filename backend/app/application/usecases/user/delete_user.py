from infrastructure.persistence.repositories.user_repository import UserRepository


class DeleteUser:
    def __init__(
        self,
        repository: UserRepository,
    ) -> None:
        self.repository = repository

    async def __call__(self, user_id: int) -> None:
        await self.repository.delete_user(user_id)
