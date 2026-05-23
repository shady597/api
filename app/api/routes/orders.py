from fastapi import APIRouter

from app.schemas.order import OrderCreate, OrderRead
from app.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["orders"])
service = OrderService()


@router.post("", response_model=OrderRead)
async def create_order(order: OrderCreate) -> OrderRead:
    return service.create_order(order)


@router.get("/{order_id}", response_model=OrderRead)
async def get_order(order_id: str) -> OrderRead:
    return service.get_order(order_id)
