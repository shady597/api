from fastapi import APIRouter

from app.schemas.payment import PaymentRead
from app.services.payment_service import PaymentService

router = APIRouter(prefix="/payments", tags=["payments"])
service = PaymentService()


@router.get("/{payment_id}", response_model=PaymentRead)
async def get_payment(payment_id: str) -> PaymentRead:
    return service.get_payment(payment_id)
