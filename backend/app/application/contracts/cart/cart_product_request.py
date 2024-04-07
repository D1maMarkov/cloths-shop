from domain.product.product import BaseProduct


class CartProductRequest(BaseProduct):
    quantity: int
    size: str
