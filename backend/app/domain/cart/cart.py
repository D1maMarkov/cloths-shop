from domain.product.product import BaseProduct


class CartProduct(BaseProduct):
    image: str
    quantity: int
    size: str
