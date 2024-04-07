from domain.order.order import Order, OrderProduct
from infrastructure.persistence.models.order import OrderOrm, OrderProductOrm
from infrastructure.persistence.repositories.mappers.product_mappers import (
    from_orm_to_image,
)


def order_products_from_orm_to_entity(order: OrderOrm) -> list[OrderProduct]:
    return [order_product_from_orm_to_entity(order_product) for order_product in order.order_products]


def order_from_orm_to_entity(order: OrderOrm) -> Order:
    products = order_products_from_orm_to_entity(order)

    order_dict = order.__dict__
    del order_dict["order_products"]

    return Order(**order_dict, order_products=products)


def order_product_from_orm_to_entity(order_product: OrderProductOrm) -> OrderProduct:
    product_model = order_product.product

    product = product_model.__dict__

    product["size"] = order_product.size
    product["quantity"] = order_product.quantity

    return OrderProduct(**product, image=from_orm_to_image(product_model.images[0]))
