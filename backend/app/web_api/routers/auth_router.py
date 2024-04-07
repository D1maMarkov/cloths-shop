from typing import Annotated

from application.contracts.user.token_response import TokenResponse
from application.usecases.auth.login import Login
from application.usecases.user.activate_user import ActivateUser
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from infrastructure.auth.jwt_processor import JwtProcessor
from starlette import status
from web_api.depends.auth.auth import (
    get_activate_user_interactor,
    get_jwt_processor,
    get_login_interactor,
)
from web_api.depends.auth.get_current_user import user_dependency

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/confirm-email/{token}")
async def confirm_email(token: str, jwt_processor: JwtProcessor = Depends(get_jwt_processor)) -> dict | bool:
    return await jwt_processor.validate_token(token)


@router.get("/activate-user/{user_id}")
async def activate_user(
    user_id: int, activate_user_interactor: ActivateUser = Depends(get_activate_user_interactor)
) -> TokenResponse:
    return await activate_user_interactor(user_id)


@router.post("/token", response_model=TokenResponse)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], login_interactor: Login = Depends(get_login_interactor)
) -> TokenResponse:
    return await login_interactor(form_data.username, form_data.password)


@router.get("/is-auth", status_code=status.HTTP_200_OK)
async def user(user: user_dependency) -> bool:
    return user is not None
