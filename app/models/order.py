from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Order:
    id: str
    reference: str
    amount: Decimal
    status: str = "pending"
