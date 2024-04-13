from application.contracts.user.user_info_response import UserInfoResponse
from infrastructure.persistence.models.user import UserOrm


def from_orm_to_user(user: UserOrm) -> UserInfoResponse:
    return UserInfoResponse(id=user.id, username=user.username, email=user.email, is_active=user.is_active)
