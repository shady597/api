from app.integrations.mpesa.client import MpesaClient


async def retry_failed_mpesa_requests(client: MpesaClient | None = None) -> None:
    client = client or MpesaClient()
    _ = client
