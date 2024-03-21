from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from settings import Settings
from typing import Annotated
from starlette import status

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, Settings.SECRET_KEY, algorithms=[Settings.ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate user.")

        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate user.")

user_dependency = Annotated[dict, Depends(get_current_user)]