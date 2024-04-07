from datetime import datetime, timedelta

from application.common.jwt_processor import JwtProcessorInterface
from jose import JWTError, jwt

from .jwt_settings import JwtSettings


class JwtProcessor(JwtProcessorInterface):
    def __init__(self, jwt_settings: JwtSettings) -> None:
        self.jwt_settings = jwt_settings

    def create_access_token(self, username: str, user_id: int) -> dict:
        encode = {"sub": username, "id": user_id}
        expires = datetime.utcnow() + timedelta(hours=self.jwt_settings.expires_in)
        encode.update({"exp": expires})
        return jwt.encode(encode, self.jwt_settings.secret_key, algorithm=self.jwt_settings.algorithm)

    async def validate_token(self, token: str) -> dict | bool:
        try:
            payload = jwt.decode(token, self.jwt_settings.secret_key, algorithms=[self.jwt_settings.algorithm])
            return payload
        except JWTError:
            return False

    async def create_confirm_email_token(self, user_id: int, code: str) -> str:
        payload = {
            "user_id": user_id,
            "code": code,
            "exp": datetime.utcnow() + timedelta(hours=self.jwt_settings.expires_in),
        }

        return jwt.encode(payload, self.jwt_settings.secret_key, algorithm=self.jwt_settings.algorithm)
