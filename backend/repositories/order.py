from schemas.cart import CreateOrderForm, SOrder, SCartProduct
from models.products import ProductOrm, ProductImageOrm
from models.orders import OrderOrm, OrderProductOrm
from sqlalchemy.orm import joinedload
from database import new_session
from models.models import User
from sqlalchemy import select
from session.cart import Cart
from settings import Settings


class OrderRepository:
    @classmethod
    async def create_order(cls, request, user, order_form: CreateOrderForm):
        async with new_session() as session:
            user_model = await session.get(User, user["id"])

            order_form_dict = order_form.model_dump()
            order_form_dict["user_id"] = user_model.id
            order_form_dict["user"] = user_model

            order = OrderOrm(**order_form_dict)

            session.add(order)
            await session.flush()

            cart = Cart(request)
            for cart_product in cart:
                order_product_dict = {
                    "product_model_id": cart_product["id"],
                    "order_id": order.id,
                    "quantity": cart_product["quantity"],
                    "size": cart_product["size"]
                }

                product = await session.get(ProductOrm, cart_product["id"])
                product.quantity_sold = product.quantity_sold + cart_product["quantity"]
                await session.commit()

                await session.refresh(product)

                order_product = OrderProductOrm(**order_product_dict)
                session.add(order_product)

            await session.commit()

            return {"message": "success"}

    @classmethod
    async def get_orders(cls, user) -> list[SOrder]:
        async with new_session() as session:
            query = select(OrderOrm).order_by(OrderOrm.created.desc()).filter(OrderOrm.user_id==user["id"]).join(OrderProductOrm)
            query = query.options(joinedload(OrderOrm.order_products))

            result = await session.execute(query)
            orders = result.unique().scalars().all()

            serialized_orders = []
            for order in orders:
                order_dict = order.__dict__

                serialized_products = []
                for order_product in order.order_products:
                    query = select(ProductOrm).join(ProductImageOrm)
                    query = query.filter(ProductOrm.id==order_product.product_model_id)
                    query = query.options(joinedload(ProductOrm.images))

                    result = await session.execute(query)
                    product = result.unique().scalars().first()
            
                    serialized_product = product.__dict__
                    serialized_product["size"] = order_product.size
                    serialized_product["quantity"] = order_product.quantity
                    serialized_product["image"] = f"{Settings.HOST}/products/image/{product.images[0].id}"

                    serialized_product = SCartProduct(**serialized_product)
                    
                    serialized_products.append(serialized_product)     

                order_dict["order_products"] = serialized_products

                serialized_orders.append(order_dict)

            await session.commit()
            return serialized_orders
        
    @classmethod
    async def get_products(cls) -> SOrder:
        async with new_session() as session:
            query = select(OrderProductOrm)
            result = await session.execute(query)
            products = result.scalars().all()
            
            return products