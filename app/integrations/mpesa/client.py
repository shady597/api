import httpx

from app.core.config import Settings, get_settings


class MpesaClient:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()

    async def get_access_token(self) -> str:
        raise NotImplementedError("Implement Daraja OAuth token retrieval.")

    async def query_transaction_status(self, transaction_id: str) -> dict:
        raise NotImplementedError("Implement Daraja transaction status lookup.")

    def build_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(base_url=self.settings.mpesa_base_url)
