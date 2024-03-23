from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from utils.user_dependency import user_dependency
from schemas.user import Token, CreateUserRequest
from repositories.user import UserRepository
from datetime import datetime, timedelta
from settings import settings
from typing import Annotated
from starlette import status
from jose import jwt


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request: CreateUserRequest):
    response = await UserRepository.create_user(create_user_request)
    return response

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await UserRepository.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="invalid username or password")
    
    token = create_access_token(user.username, user.id, timedelta(minutes=60))
    
    return {'access_token': token, 'token_type': 'bearer'}

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": username, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

@router.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentification failed")
    return {"user": user}

@router.get("/is-auth", status_code=status.HTTP_200_OK)
async def user(user: user_dependency):
    if user is None:
        return False
    return True

@router.get("/get-info", status_code=status.HTTP_200_OK)
async def get_user_info(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentification failed")
    return {"username": user["username"]}