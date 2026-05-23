from functools import lru_cache
from os import getenv

from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "M-Pesa Reconciliation API"
    mpesa_consumer_key: str | None = None
    mpesa_consumer_secret: str | None = None
    mpesa_base_url: str = "https://sandbox.safaricom.co.ke"


@lru_cache
def get_settings() -> Settings:
    return Settings(
        mpesa_consumer_key=getenv("MPESA_CONSUMER_KEY"),
        mpesa_consumer_secret=getenv("MPESA_CONSUMER_SECRET"),
        mpesa_base_url=getenv("MPESA_BASE_URL", "https://sandbox.safaricom.co.ke"),
    )
