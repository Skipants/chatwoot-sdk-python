"""Type definitions for agents."""

from pydantic import BaseModel, Field

from chatwoot.types.common import AgentRole, AvailabilityStatus


class Agent(BaseModel):
    """Agent information."""

    id: int
    uid: str | None = None
    name: str
    display_name: str | None = None
    available_name: str | None = None
    avatar_url: str | None = None
    type: str | None = None
    availability_status: AvailabilityStatus | None = None
    email: str
    account_id: int
    role: AgentRole
    confirmed: bool = False
    custom_attributes: dict = Field(default_factory=dict)
