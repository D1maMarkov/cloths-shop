from domain.common.exc import DomainError


class ProductNotFound(DomainError):
    pass


class ProductsImageNotFound(DomainError):
    pass


class ProductAlreadyExist(DomainError):
    pass


class ProductsNotFound(DomainError):
    pass
