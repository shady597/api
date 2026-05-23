from decimal import Decimal

from pydantic import BaseModel


class PaymentRead(BaseModel):
    id: str
    transaction_id: str
    amount: Decimal
    status: str
