from application.contracts.user.create_user_request import CreateUserRequest
from application.contracts.user.token_response import TokenResponse
from application.contracts.user.user_info_response import UserInfoResponse
from application.usecases.auth.register import Register
from application.usecases.user.delete_user import DeleteUser
from application.usecases.user.get_info import GetUserInfo
from fastapi import APIRouter, Depends, status
from web_api.depends.auth.get_current_user import user_dependency
from web_api.depends.user import (
    get_delete_user_interactor,
    get_register_interactor,
    get_user_info_interactor,
)

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TokenResponse)
async def create_user(
    create_user_request: CreateUserRequest,
    register_interactor: Register = Depends(get_register_interactor),
) -> TokenResponse:
    return await register_interactor(create_user_request)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    delete_user_interactor: DeleteUser = Depends(get_delete_user_interactor),
) -> None:
    return await delete_user_interactor(user_id)


@router.get("/get-info", status_code=status.HTTP_200_OK, response_model=UserInfoResponse)
async def get_user_info(
    user: user_dependency, get_user_info_interactor: GetUserInfo = Depends(get_user_info_interactor)
) -> UserInfoResponse:
    return await get_user_info_interactor(user["id"])
