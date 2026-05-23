from decimal import Decimal

from pydantic import BaseModel


class OrderCreate(BaseModel):
    reference: str
    amount: Decimal


class OrderRead(OrderCreate):
    id: str
    status: str = "pending"
