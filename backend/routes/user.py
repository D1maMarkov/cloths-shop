from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from repositories.user_repository import UserRepository
from schemas.user import CreateUserRequest, SUser, Token
from services.user_service import UserService
from settings import settings
from starlette import status
from utils.user_dependency import user_dependency

router = APIRouter(prefix="/auth", tags=["auth"])


repository = UserRepository()
service = UserService(repository)


def get_service():
    return service


service_dependency = Annotated[dict, Depends(get_service)]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(service: service_dependency, create_user_request: CreateUserRequest):
    response = await service.create_user(create_user_request)
    return response


@router.get("/confirm-email/{token}")
async def confirm_email(service: service_dependency, token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return False


@router.get("/activate-user/{id}")
async def activate_user(service: service_dependency, id):
    response = await service.activate_user(id)
    return response


@router.post("/token", response_model=Token)
async def login_for_access_token(
    service: service_dependency, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await UserRepository.authenticate_user(form_data.username, form_data.password)
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
async def get_user_info(service: service_dependency, user: user_dependency) -> SUser:
    if user is None:
        raise HTTPException(status_code=401, detail="Authentification failed")

    user = await service.get_user_info(user["id"])
    return user
