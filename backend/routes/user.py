from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from repositories.user_repository import UserRepository
from schemas.user import CreateUserRequest, SUser, Token
from services.auth_service import AuthService
from services.user_service import UserService
from settings import Settings, get_settings
from starlette import status
from utils.dependencies import user_dependency

router = APIRouter(prefix="/auth", tags=["auth"])


repository = UserRepository()
user_service = UserService(repository)


def get_user_service():
    return user_service


user_service_dependency = Annotated[dict, Depends(get_user_service)]

auth_service = AuthService(repository)


def get_auth_service():
    return auth_service


auth_service_dependency = Annotated[dict, Depends(get_auth_service)]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(service: user_service_dependency, create_user_request: CreateUserRequest):
    response = await service.create_user(create_user_request)
    return response


@router.get("/confirm-email/{token}")
async def confirm_email(token: str, settings: Settings = Depends(get_settings)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return False


@router.get("/activate-user/{user_id}")
async def activate_user(
    user_service: user_service_dependency, auth_service: auth_service_dependency, user_id: int
) -> str:
    user_model = await user_service.get_user(user_id)
    await user_service.activate_user(user_id)
    token = auth_service.create_access_token(user_model.username, user_model.id, timedelta(minutes=60))
    return token


@router.post("/token", response_model=Token)
async def login_for_access_token(
    service: auth_service_dependency, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid username or password")

    token = service.create_access_token(user.username, user.id, timedelta(minutes=60))

    return {"access_token": token, "token_type": "bearer"}


@router.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentification failed")
    return {"user": user}


@router.get("/is-auth", status_code=status.HTTP_200_OK)
async def user(user: user_dependency):
    if user is None:
        return False
    return True


@router.get("/get-info", status_code=status.HTTP_200_OK)
async def get_user_info(service: user_service_dependency, user: user_dependency) -> SUser:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentification failed")

    user = await service.get_user(user["id"])
    return user
