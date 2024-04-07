from application.usecases.auth.register import Register
from application.usecases.user.delete_user import DeleteUser
from application.usecases.user.get_info import GetUserInfo
from fastapi import Depends
from infrastructure.auth.jwt_processor import JwtProcessor
from infrastructure.email_notification.depends import get_email_service
from infrastructure.email_notification.service import EmailNotificationService
from infrastructure.persistence.repositories.user_repository import UserRepository
from infrastructure.security.password_hasher import PasswordHasher, get_password_hasher
from sqlalchemy.ext.asyncio import AsyncSession
from web_api.depends.auth.get_jwt_processor import get_jwt_processor
from web_api.depends.get_db import get_db


def get_repository(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_register_interactor(
    user_repository: UserRepository = Depends(get_repository),
    jwt_processor: JwtProcessor = Depends(get_jwt_processor),
    email_service: EmailNotificationService = Depends(get_email_service),
    password_hasher: PasswordHasher = Depends(get_password_hasher),
) -> Register:
    return Register(user_repository, password_hasher, jwt_processor, email_service)


def get_user_info_interactor(
    user_repository: UserRepository = Depends(get_repository),
) -> GetUserInfo:
    return GetUserInfo(user_repository)


def get_delete_user_interactor(user_repository: UserRepository = Depends(get_repository)) -> DeleteUser:
    return DeleteUser(user_repository)
