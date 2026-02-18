"""Type definitions for messages."""

from pydantic import BaseModel, Field

from chatwoot.types.common import MessageContentType


class MessageAttachment(BaseModel):
    """Message attachment information."""

    id: int
    message_id: int
    file_type: str
    account_id: int
    extension: str | None = None
    data_url: str
    thumb_url: str | None = None
    file_size: int | None = None


class MessageSender(BaseModel):
    """Message sender information."""

    id: int
    name: str | None = None
    avatar_url: str | None = None
    type: str | None = None
    thumbnail: str | None = None
    email: str | None = None


class Message(BaseModel):
    """Message information."""

    id: int
    content: str | None = None
    content_type: MessageContentType | None = None
    content_attributes: dict = Field(default_factory=dict)
    message_type: int | str
    created_at: int  # Unix timestamp
    private: bool = False
    attachment: MessageAttachment | None = None
    attachments: list[MessageAttachment] = Field(default_factory=list)
    sender: MessageSender | None = None
    conversation_id: int
    inbox_id: int | None = None
    account_id: int | None = None
    source_id: str | None = None
    status: str | None = None
    external_source_ids: dict = Field(default_factory=dict)
