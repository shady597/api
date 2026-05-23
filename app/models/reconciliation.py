from dataclasses import dataclass


@dataclass
class ReconciliationResult:
    order_id: str | None
    payment_id: str
    status: str
