from functools import lru_cache

from application.common.password_hasher import PasswordHasherInterface
from passlib.context import CryptContext


class PasswordHasher(PasswordHasherInterface):
    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify(self, password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(password, hashed_password)


@lru_cache
def get_password_hasher() -> PasswordHasher:
    return PasswordHasher()
