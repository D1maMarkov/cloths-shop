from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    password: str
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str


class SUser(BaseModel):
    id: int | None = None
    username: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True
