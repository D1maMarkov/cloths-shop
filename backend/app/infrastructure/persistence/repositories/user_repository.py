from domain.user.exc import UserByIdNotFound
from domain.user.repository import UserRepositoryInterface
from infrastructure.persistence.models.user import UserOrm
from infrastructure.persistence.repositories.repository import BaseRepository
from sqlalchemy import select


class UserRepository(UserRepositoryInterface, BaseRepository):
    async def delete_user(self, user_id: int):
        user = await self.db.get(UserOrm, user_id)
        if user is None:
            raise UserByIdNotFound("user with this id does not exist")

        await self.db.delete(user)
        await self.db.commit()

    async def create_user(self, create_user_request: dict):
        create_user_model = UserOrm(**create_user_request)

        self.db.add(create_user_model)
        await self.db.flush()
        await self.db.commit()
        return create_user_model.id

    async def get_user_by_username(self, username: str):
        query = select(UserOrm).filter(UserOrm.username == username)
        result = await self.db.execute(query)
        user = result.scalars().first()

        return user

    async def get_user_by_email(self, email: str):
        query = select(UserOrm).filter(UserOrm.email == email)
        result = await self.db.execute(query)
        user = result.scalars().first()

        return user

    async def activate_user(self, user_id: int):
        user = await self.db.get(UserOrm, user_id)
        user.is_active = True

        await self.db.commit()
        await self.db.refresh(user)

    async def get_user(self, user_id: int):
        return await self.db.get(UserOrm, user_id)

    async def delete_inactive_users(self):
        inactive_users = select(UserOrm).filter(UserOrm.is_active == False)
        for user in inactive_users:
            await self.db.delete(user)

        await self.db.commit()
