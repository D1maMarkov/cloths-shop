from domain.common.exc import DomainError


class UserNotFound(DomainError):
    pass


class UserByIdNotFound(DomainError):
    pass


class UserWithEmailAlreadyExist(DomainError):
    pass


class UserWithUsernameAlreadyExist(DomainError):
    pass
