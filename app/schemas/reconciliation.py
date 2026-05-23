from pydantic import BaseModel


class ReconciliationRead(BaseModel):
    order_id: str | None
    payment_id: str
    status: str
