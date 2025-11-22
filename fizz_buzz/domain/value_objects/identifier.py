from __future__ import annotations

from pydantic import BaseModel


class Identifier(BaseModel):
    value: str | None
