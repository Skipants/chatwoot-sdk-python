"""API resource implementations."""

from chatwoot.resources.agents import AgentsResource, AsyncAgentsResource
from chatwoot.resources.contacts import AsyncContactsResource, ContactsResource
from chatwoot.resources.conversations import (
    AsyncConversationsResource,
    ConversationsResource,
)
from chatwoot.resources.inboxes import AsyncInboxesResource, InboxesResource
from chatwoot.resources.messages import AsyncMessagesResource, MessagesResource
from chatwoot.resources.profile import AsyncProfileResource, ProfileResource
from chatwoot.resources.teams import AsyncTeamsResource, TeamsResource

__all__ = [
    # Profile
    "ProfileResource",
    "AsyncProfileResource",
    # Conversations
    "ConversationsResource",
    "AsyncConversationsResource",
    # Messages
    "MessagesResource",
    "AsyncMessagesResource",
    # Contacts
    "ContactsResource",
    "AsyncContactsResource",
    # Inboxes
    "InboxesResource",
    "AsyncInboxesResource",
    # Teams
    "TeamsResource",
    "AsyncTeamsResource",
    # Agents
    "AgentsResource",
    "AsyncAgentsResource",
]
