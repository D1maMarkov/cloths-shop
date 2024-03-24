from repositories.order_repository import OrderRepository
from repositories.products_repository import ProductRepository
from schemas.cart import CreateOrderForm, SOrder, SOrderProduct
from session.cart import Cart


class OrderService:
    def __init__(self, repository: OrderRepository, product_repository: ProductRepository) -> None:
        self.repository = repository
        self.product_repository = product_repository

    async def create_order(self, request, user, order_form: CreateOrderForm):
        order_id = await self.repository.create_order(user=user, order_form=order_form)

        cart = Cart(request)
        for product in cart:
            await self.repository.create_order_product(order_id=order_id, cart_product=product)

        return {"message": "success"}

    async def get_order_products(self, order_model) -> list[SOrderProduct]:
        products = []
        for order_product in order_model.order_products:
            product_model = await self.product_repository.get_product(id=order_product.product_model_id)

            serialized_product = product_model.__dict__

            serialized_product["size"] = order_product.size
            serialized_product["quantity"] = order_product.quantity

            serialized_product = SOrderProduct(**serialized_product, image=product_model.images[0])

            products.append(serialized_product)

        return products

    async def get_orders(self, user) -> list[SOrder]:
        order_models = await self.repository.get_orders(user=user)

        orders = []
        for order_model in order_models:
            products = await self.get_order_products(order_model)

            order_dict = order_model.__dict__
            del order_dict["order_products"]

            order = SOrder(**order_dict, order_products=products)

            orders.append(order)

        return orders
