from domain.order.repository import OrderRepositoryInterface
from infrastructure.persistence.models.order import OrderOrm, OrderProductOrm
from infrastructure.persistence.models.product_models import ProductImageOrm, ProductOrm
from infrastructure.persistence.repositories.repository import BaseRepository
from sqlalchemy import select
from sqlalchemy.orm import joinedload


class OrderRepository(OrderRepositoryInterface, BaseRepository):
    async def create_order(self, order_form: dict) -> int:
        order = OrderOrm(**order_form)

        self.db.add(order)
        await self.db.flush()
        await self.db.commit()
        return order.id

    async def create_order_product(self, order_product_dict: dict) -> None:
        order_product = OrderProductOrm(**order_product_dict)
        self.db.add(order_product)

        await self.db.commit()

    async def update_product_quantity_sold(self, product_id: int, quantity: int) -> None:
        product = await self.db.get(ProductOrm, product_id)
        product.quantity_sold = product.quantity_sold + quantity
        await self.db.commit()

        await self.db.refresh(product)

    async def get_orders(self, user_id: int) -> list[OrderOrm]:
        query = (
            select(OrderOrm)
            .order_by(OrderOrm.created.desc())
            .filter(OrderOrm.user_id == user_id)
            .join(OrderProductOrm)
            .join(ProductOrm)
            .join(ProductImageOrm)
        )

        query = query.options(joinedload(OrderOrm.order_products))

        result = await self.db.execute(query)
        order_models = result.unique().scalars().all()

        return order_models
