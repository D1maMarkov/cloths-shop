from infrastructure.persistence.models.user import User
from infrastructure.persistence.repositories.repository import BaseRepository
from sqlalchemy import select
from web_api.exc.user_exc import UserNotFound


class UserRepository(BaseRepository):
    async def delete_user(self, user_id: int):
        user = await self.db.get(User, user_id)
        if user is None:
            raise UserNotFound()

        await self.db.delete(user)
        await self.db.commit()

    async def create_user(self, create_user_request: dict):
        create_user_model = User(**create_user_request)

        self.db.add(create_user_model)
        await self.db.flush()
        await self.db.commit()
        return create_user_model.id

    async def get_user_by_username(self, username: str):
        query = select(User).filter(User.username == username)
        result = await self.db.execute(query)
        user = result.scalars().first()

        return user

    async def get_user_by_email(self, email: str):
        query = select(User).filter(User.email == email)
        result = await self.db.execute(query)
        user = result.scalars().first()

        return user

    async def activate_user(self, user_id: int):
        user = await self.db.get(User, user_id)
        user.is_active = True

        await self.db.commit()
        await self.db.refresh(user)

    async def get_user(self, user_id: int):
        return await self.db.get(User, user_id)

    async def delete_inactive_users(self):
        inactive_users = select(User).filter(User.is_active == False)
        for user in inactive_users:
            await self.db.delete(user)

        await self.db.commit()
