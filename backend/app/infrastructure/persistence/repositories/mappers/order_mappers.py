from domain.order.order import Order, OrderProduct
from infrastructure.persistence.models.order import OrderOrm, OrderProductOrm
from infrastructure.persistence.repositories.mappers.product_mappers import (
    from_orm_to_image,
)


def order_products_from_orm_to_entity(order: OrderOrm) -> list[OrderProduct]:
    return [order_product_from_orm_to_entity(order_product) for order_product in order.order_products]


def order_from_orm_to_entity(order: OrderOrm) -> Order:
    return Order(
        name=order.name,
        secondname=order.secondname,
        adress=order.adress,
        phone=order.phone,
        payment=order.payment,
        delivery=order.delivery,
        user_id=order.user_id,
        created=order.created,
        order_products=order_products_from_orm_to_entity(order),
    )


def order_product_from_orm_to_entity(order_product: OrderProductOrm) -> OrderProduct:
    product = order_product.product

    return OrderProduct(
        id=product.id,
        name=product.name,
        quantity=order_product.quantity,
        size=order_product.size,
        image=from_orm_to_image(product.images[0]),
        description=product.description,
        price=product.price,
    )
