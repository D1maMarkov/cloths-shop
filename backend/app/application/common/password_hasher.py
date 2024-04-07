from typing import Protocol


class PasswordHasherInterface(Protocol):
    def hash_password(self, password: str) -> str:
        raise NotImplementedError

    def verify(self, password: str, hashed_password: str) -> bool:
        raise NotImplementedError
