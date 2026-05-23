from fastapi import APIRouter, Request

from app.integrations.mpesa.schemas import MpesaCallback
from app.services.reconciliation_service import ReconciliationService

router = APIRouter(prefix="/webhooks", tags=["webhooks"])
service = ReconciliationService()


@router.post("/mpesa")
async def receive_mpesa_callback(request: Request) -> dict[str, str]:
    payload = await request.json()
    callback = MpesaCallback(raw_payload=payload)
    service.process_callback(callback)
    return {"status": "accepted"}
