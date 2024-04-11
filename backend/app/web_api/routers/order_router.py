from application.contracts.order.create_order_request import CreateOrderRequest
from application.usecases.order.create_order import CreateOrder
from application.usecases.order.get_orders import GetOrders
from domain.order.order import Order
from fastapi import APIRouter, Depends, status
from web_api.depends.auth.get_current_user import user_dependency
from web_api.depends.order.create_order import get_create_interactor
from web_api.depends.order.get_orders import get_find_interactor

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_order(
    user: user_dependency,
    order_form: CreateOrderRequest,
    create_order_interactor: CreateOrder = Depends(get_create_interactor),
) -> None:
    return await create_order_interactor(order_form, user)


@router.get("/", response_model=list[Order])
async def get_orders(
    user: user_dependency, get_orders_interactor: GetOrders = Depends(get_find_interactor)
) -> list[Order]:
    return await get_orders_interactor(user["id"])
