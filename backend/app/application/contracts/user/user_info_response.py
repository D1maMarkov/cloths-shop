from pydantic import BaseModel


class UserInfoResponse(BaseModel):
    id: int | None = None
    username: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True
