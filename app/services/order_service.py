from uuid import uuid4

from app.schemas.order import OrderCreate, OrderRead


class OrderService:
    def create_order(self, order: OrderCreate) -> OrderRead:
        return OrderRead(id=str(uuid4()), status="pending", **order.model_dump())

    def get_order(self, order_id: str) -> OrderRead:
        return OrderRead(id=order_id, reference="sample-order", amount=0, status="pending")
