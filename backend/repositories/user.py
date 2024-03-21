from schemas.user import CreateUserRequest
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from fastapi import HTTPException
from database import new_session
from sqlalchemy import select
from starlette import status
from models.models import User


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class UserRepository:
    @classmethod
    async def create_user(cls, create_user_request: CreateUserRequest):
        async with new_session() as session:
            try:
                create_user_model = User(
                    username=create_user_request.username,
                    hashed_password=bcrypt_context.hash(create_user_request.password)
                )
                
                session.add(create_user_model)
                await session.commit()
                return {"message": "success"}
            except IntegrityError:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="There is already a user with that username")

    @classmethod
    async def authenticate_user(cls, username: str, password: str):
        async with new_session() as session:
            query = select(User).filter(User.username==username)
            user = await session.execute(query)
            user = user.scalars().first()

            if not user:
                return False
            if not bcrypt_context.verify(password, user.hashed_password):
                return False
            return user