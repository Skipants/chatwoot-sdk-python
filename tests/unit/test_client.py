"""Tests for client initialization."""

import pytest

from chatwoot import AsyncChatwootClient, ChatwootClient
from chatwoot.resources.profile import AsyncProfileResource, ProfileResource
from chatwoot.resources.conversations import (
    AsyncConversationsResource,
    ConversationsResource,
)
from chatwoot.resources.messages import AsyncMessagesResource, MessagesResource


def test_client_initialization(base_url, api_token):
    """Test synchronous client initialization."""
    client = ChatwootClient(base_url=base_url, api_token=api_token)

    # Check that all resources are initialized
    assert isinstance(client.profile, ProfileResource)
    assert isinstance(client.conversations, ConversationsResource)
    assert isinstance(client.messages, MessagesResource)

    # Check nested resources
    assert hasattr(client.conversations, "labels")
    assert hasattr(client.contacts, "labels")
    assert hasattr(client.teams, "agents")

    client.close()


def test_client_context_manager(base_url, api_token):
    """Test client context manager."""
    with ChatwootClient(base_url=base_url, api_token=api_token) as client:
        assert isinstance(client.profile, ProfileResource)

    # Client should be closed after exiting context


def test_async_client_initialization(base_url, api_token):
    """Test asynchronous client initialization."""
    client = AsyncChatwootClient(base_url=base_url, api_token=api_token)

    # Check that all async resources are initialized
    assert isinstance(client.profile, AsyncProfileResource)
    assert isinstance(client.conversations, AsyncConversationsResource)
    assert isinstance(client.messages, AsyncMessagesResource)

    # Check nested resources
    assert hasattr(client.conversations, "labels")
    assert hasattr(client.contacts, "labels")
    assert hasattr(client.teams, "agents")


@pytest.mark.asyncio
async def test_async_client_context_manager(base_url, api_token):
    """Test async client context manager."""
    async with AsyncChatwootClient(base_url=base_url, api_token=api_token) as client:
        assert isinstance(client.profile, AsyncProfileResource)

    # Client should be closed after exiting context
