"""Type definitions for user profile."""

from datetime import datetime

from pydantic import BaseModel, Field

from chatwoot.types.common import AgentRole, AvailabilityStatus


class ProfileAccount(BaseModel):
    """Account associated with user profile."""

    id: int
    name: str
    role: AgentRole
    active_at: datetime | None = None


class Profile(BaseModel):
    """User profile information."""

    id: int
    provider: str | None = None
    uid: str | None = None
    name: str
    display_name: str | None = None
    email: str
    account_id: int
    role: AgentRole
    confirmed: bool = False
    custom_attributes: dict = Field(default_factory=dict)
    accounts: list[ProfileAccount] = Field(default_factory=list)
    availability_status: AvailabilityStatus | None = None
    available_name: str | None = None
    avatar_url: str | None = None
    type: str | None = None
