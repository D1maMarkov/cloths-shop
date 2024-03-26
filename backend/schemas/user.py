from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    password: str
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str


class SUser(BaseModel):
    username: str
    email: str
    is_active: bool
