"""Type definitions for conversations."""

from pydantic import BaseModel, Field

from chatwoot.types.common import ConversationStatus


class ConversationContact(BaseModel):
    """Contact information in a conversation."""

    id: int
    name: str | None = None
    email: str | None = None
    phone_number: str | None = None
    identifier: str | None = None
    thumbnail: str | None = None
    avatar_url: str | None = None
    additional_attributes: dict = Field(default_factory=dict)
    custom_attributes: dict = Field(default_factory=dict)


class ConversationInbox(BaseModel):
    """Inbox information in a conversation."""

    id: int
    name: str
    channel_id: int | None = None
    channel_type: str | None = None


class ConversationAssignee(BaseModel):
    """Assignee information in a conversation."""

    id: int
    name: str
    email: str | None = None
    avatar_url: str | None = None
    available_name: str | None = None
    type: str | None = None


class ConversationTeam(BaseModel):
    """Team information in a conversation."""

    id: int
    name: str
    description: str | None = None


class ConversationMeta(BaseModel):
    """Metadata for conversation."""

    sender: ConversationContact | None = None
    assignee: ConversationAssignee | None = None
    team: ConversationTeam | None = None
    hmac_verified: bool | None = None


class Conversation(BaseModel):
    """Conversation information."""

    id: int
    account_id: int
    inbox_id: int
    status: ConversationStatus
    assignee_id: int | None = None
    contact_id: int | None = None
    display_id: int | None = None
    additional_attributes: dict = Field(default_factory=dict)
    custom_attributes: dict = Field(default_factory=dict)
    agent_last_seen_at: int | None = None  # Unix timestamp
    contact_last_seen_at: int | None = None  # Unix timestamp
    timestamp: int | None = None  # Unix timestamp
    created_at: int | None = None  # Unix timestamp
    unread_count: int = 0
    first_reply_created_at: int | None = None  # Unix timestamp
    priority: str | None = None
    waiting_since: int | None = None  # Unix timestamp
    snoozed_until: int | None = None  # Unix timestamp
    can_reply: bool = True
    muted: bool = False
    labels: list[str] = Field(default_factory=list)
    meta: ConversationMeta | None = None

    # Optional nested objects (may not always be present)
    messages: list = Field(default_factory=list)
    contact: ConversationContact | None = None
    inbox: ConversationInbox | None = None
