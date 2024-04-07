from fastapi import Depends
from infrastructure.auth.jwt_processor import JwtProcessor
from infrastructure.auth.jwt_settings import JwtSettings, get_jwt_settings


def get_jwt_processor(jwt_settings: JwtSettings = Depends(get_jwt_settings)) -> JwtProcessor:
    return JwtProcessor(jwt_settings)
