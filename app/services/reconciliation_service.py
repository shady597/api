from app.integrations.mpesa.schemas import MpesaCallback
from app.schemas.reconciliation import ReconciliationRead


class ReconciliationService:
    def process_callback(self, callback: MpesaCallback) -> ReconciliationRead:
        return ReconciliationRead(
            order_id=None,
            payment_id="pending",
            status="manual_review",
        )
