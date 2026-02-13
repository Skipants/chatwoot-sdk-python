"""Type definitions for contacts."""

from datetime import datetime

from pydantic import BaseModel, Field


class ContactInbox(BaseModel):
    """Contact's inbox association."""

    source_id: str
    inbox_id: int | None = None


class Contact(BaseModel):
    """Contact information."""

    id: int
    name: str | None = None
    email: str | None = None
    phone_number: str | None = None
    identifier: str | None = None
    thumbnail: str | None = None
    avatar_url: str | None = None
    additional_attributes: dict = Field(default_factory=dict)
    custom_attributes: dict = Field(default_factory=dict)
    contact_inboxes: list[ContactInbox] = Field(default_factory=list)
    last_activity_at: datetime | None = None
    created_at: datetime | None = None
    availability_status: str | None = None
    blocked: bool = False


class ContactCreateResponse(BaseModel):
    """Response from creating a contact."""

    contact: Contact
    contact_inbox: ContactInbox
