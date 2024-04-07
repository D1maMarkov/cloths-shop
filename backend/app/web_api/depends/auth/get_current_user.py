from typing import Annotated

from application.usecases.user.get_current_user import GetCurrentUser
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from web_api.depends.auth.auth import get_current_user_interactor

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_bearer)],
    current_user_interactor: GetCurrentUser = Depends(get_current_user_interactor),
) -> dict | None:
    return await current_user_interactor(token)


user_dependency = Annotated[dict, Depends(get_current_user)]
