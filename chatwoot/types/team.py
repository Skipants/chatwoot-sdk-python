"""Type definitions for teams."""

from datetime import datetime

from pydantic import BaseModel


class Team(BaseModel):
    """Team information."""

    id: int
    name: str
    description: str | None = None
    allow_auto_assign: bool = True
    account_id: int
    is_member: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None
