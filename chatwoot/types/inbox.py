"""Type definitions for inboxes."""

from datetime import datetime

from pydantic import BaseModel

from chatwoot.types.common import ChannelType


class Inbox(BaseModel):
    """Inbox information."""

    id: int
    channel_id: int
    name: str
    channel_type: ChannelType
    greeting_enabled: bool = False
    greeting_message: str | None = None
    working_hours_enabled: bool = False
    enable_email_collect: bool = True
    csat_survey_enabled: bool = False
    allow_messages_after_resolved: bool = True
    avatar_url: str | None = None
    widget_color: str | None = None
    website_url: str | None = None
    welcome_title: str | None = None
    welcome_tagline: str | None = None
    webhook_url: str | None = None
    enable_auto_assignment: bool = True
    web_widget_script: str | None = None
    forward_to_email: str | None = None
    phone_number: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
