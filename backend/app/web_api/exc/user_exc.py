from fastapi import HTTPException, status


class UserWithUsernameAlreadyExist(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail="user with this username already exist")


class UserWithEmailAlreadyExist(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail="user with this email already exist")


class UserNotFound(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="user with this id does not exist")
