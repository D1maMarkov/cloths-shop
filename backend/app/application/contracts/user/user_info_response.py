from domain.user.user import User


class UserInfoResponse(User):
    class Config:
        from_attributes = True
