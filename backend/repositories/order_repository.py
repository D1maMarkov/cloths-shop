from database import new_session
from models.models import User
from models.orders import OrderOrm, OrderProductOrm
from models.products import ProductOrm
from schemas.cart import CreateOrderForm
from sqlalchemy import select
from sqlalchemy.orm import joinedload


class OrderRepository:
    @classmethod
    async def create_order(cls, user, order_form: CreateOrderForm) -> int:
        async with new_session() as session:
            user_model = await session.get(User, user["id"])

            order_form_dict = order_form.model_dump()
            order_form_dict["user_id"] = user_model.id
            order_form_dict["user"] = user_model

            order = OrderOrm(**order_form_dict)

            session.add(order)
            await session.flush()
            await session.commit()
            return order.id

    @classmethod
    async def create_order_product(cls, order_id, cart_product):
        async with new_session() as session:
            await cls.update_product_quantity_sold(product_id=cart_product["id"], quantity=cart_product["quantity"])

            order_product_dict = {
                "product_model_id": cart_product["id"],
                "order_id": order_id,
                "quantity": cart_product["quantity"],
                "size": cart_product["size"],
            }

            order_product = OrderProductOrm(**order_product_dict)
            session.add(order_product)

            await session.commit()

    @classmethod
    async def update_product_quantity_sold(cls, product_id: int, quantity: int):
        async with new_session() as session:
            product = await session.get(ProductOrm, product_id)
            product.quantity_sold = product.quantity_sold + quantity
            await session.commit()

            await session.refresh(product)

    @classmethod
    async def get_orders(cls, user):
        async with new_session() as session:
            query = (
                select(OrderOrm)
                .order_by(OrderOrm.created.desc())
                .filter(OrderOrm.user_id == user["id"])
                .join(OrderProductOrm)
            )
            query = query.options(joinedload(OrderOrm.order_products))

            result = await session.execute(query)
            order_models = result.unique().scalars().all()

            return order_models
