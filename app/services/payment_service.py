from app.schemas.payment import PaymentRead


class PaymentService:
    def get_payment(self, payment_id: str) -> PaymentRead:
        return PaymentRead(
            id=payment_id,
            transaction_id="sample-transaction",
            amount=0,
            status="received",
        )
