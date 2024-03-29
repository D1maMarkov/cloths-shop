from database import new_session
from fastapi import HTTPException
from models.models import User
from passlib.context import CryptContext
from schemas.user import CreateUserRequest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from starlette import status

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserRepository:
    @classmethod
    async def create_user(cls, create_user_request: CreateUserRequest):
        async with new_session() as session:
            try:
                create_user_model = User(
                    username=create_user_request.username,
                    hashed_password=bcrypt_context.hash(create_user_request.password),
                    email=create_user_request.email,
                )

                session.add(create_user_model)
                await session.flush()
                await session.commit()
                return create_user_model.id

            except IntegrityError as e:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT, detail="There is already a user with that email"
                )

    @classmethod
    async def authenticate_user(cls, username: str, password: str):
        async with new_session() as session:
            query = select(User).filter(User.username == username)
            user = await session.execute(query)
            user = user.scalars().first()

            if not user:
                return False
            if not bcrypt_context.verify(password, user.hashed_password):
                return False
            if not user.is_active:
                return False

            return user

    @classmethod
    async def activate_user(cls, user_id):
        async with new_session() as session:
            user_model = await session.get(User, user_id)
            user_model.is_active = True

            await session.commit()
            await session.refresh(user_model)

    @classmethod
    async def get_user(cls, user_id: int):
        async with new_session() as session:
            user = await session.get(User, user_id)
            return user

    @classmethod
    async def delete_inactive_users(cls):
        async with new_session() as session:
            inactive_users = select(User).filter(User.is_active == False)
            await session.delete(inactive_users)
            await session.commit()
