from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Payment:
    id: str
    transaction_id: str
    amount: Decimal
    phone_number: str | None = None
    status: str = "received"
