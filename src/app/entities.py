from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AbstractEntity(BaseModel):
    id: Optional[int]


class TodoEntry(AbstractEntity):
    summary: str
    detail: Optional[str]
    created_at: datetime
