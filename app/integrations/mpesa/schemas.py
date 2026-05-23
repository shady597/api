from typing import Any

from pydantic import BaseModel, Field


class MpesaCallback(BaseModel):
    raw_payload: dict[str, Any] = Field(default_factory=dict)
