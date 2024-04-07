from application.usecases.auth.login import Login
from application.usecases.user.activate_user import ActivateUser
from application.usecases.user.get_current_user import GetCurrentUser
from fastapi import Depends
from infrastructure.auth.jwt_processor import JwtProcessor
from infrastructure.persistence.repositories.user_repository import UserRepository
from infrastructure.security.password_hasher import PasswordHasher, get_password_hasher
from web_api.depends.auth.get_jwt_processor import get_jwt_processor
from web_api.depends.user import get_repository


def get_login_interactor(
    jwt_processor: JwtProcessor = Depends(get_jwt_processor),
    password_hasher: PasswordHasher = Depends(get_password_hasher),
    repository: UserRepository = Depends(get_repository),
) -> Login:
    return Login(repository, password_hasher, jwt_processor)


def get_activate_user_interactor(
    jwt_processor: JwtProcessor = Depends(get_jwt_processor), repository: UserRepository = Depends(get_repository)
) -> ActivateUser:
    return ActivateUser(repository, jwt_processor)


def get_current_user_interactor(
    jwt_processor: JwtProcessor = Depends(get_jwt_processor), repository: UserRepository = Depends(get_repository)
) -> GetCurrentUser:
    return GetCurrentUser(repository, jwt_processor)
