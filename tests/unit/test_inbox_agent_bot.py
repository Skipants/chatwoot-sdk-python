"""Tests for inboxes.get_agent_bot and inboxes.set_agent_bot."""

import pytest
from unittest.mock import AsyncMock

from chatwoot.resources.inboxes import InboxesResource, AsyncInboxesResource


AGENT_BOT = {
    "id": 2,
    "name": "Support Bot",
    "description": "Automated support agent",
    "outgoing_url": "https://bot.example.com/webhook",
    "bot_type": "agent_bot",
    "account_id": 1,
    "system_bot": False,
}


# ---------------------------------------------------------------------------
# get_agent_bot
# ---------------------------------------------------------------------------


def test_get_agent_bot(mock_http):
    """Test retrieving the agent bot for an inbox."""
    mock_http.get.return_value = AGENT_BOT

    resource = InboxesResource(mock_http)
    bot = resource.get_agent_bot(account_id=1, inbox_id=5)

    mock_http.get.assert_called_once_with(
        "/api/v1/accounts/1/inboxes/5/agent_bot"
    )
    assert isinstance(bot, dict)
    assert bot["id"] == 2
    assert bot["name"] == "Support Bot"


def test_get_agent_bot_returns_none_when_no_bot(mock_http):
    """Test get_agent_bot returns None when no bot is set."""
    mock_http.get.return_value = None

    resource = InboxesResource(mock_http)
    bot = resource.get_agent_bot(account_id=1, inbox_id=5)

    assert bot is None


@pytest.mark.asyncio
async def test_async_get_agent_bot(mock_async_http):
    """Test async retrieving the agent bot for an inbox."""
    mock_async_http.get = AsyncMock(return_value=AGENT_BOT)

    resource = AsyncInboxesResource(mock_async_http)
    bot = await resource.get_agent_bot(account_id=1, inbox_id=5)

    mock_async_http.get.assert_called_once_with(
        "/api/v1/accounts/1/inboxes/5/agent_bot"
    )
    assert bot["id"] == 2


# ---------------------------------------------------------------------------
# set_agent_bot
# ---------------------------------------------------------------------------


def test_set_agent_bot(mock_http):
    """Test assigning an agent bot to an inbox."""
    mock_http.post.return_value = {}

    resource = InboxesResource(mock_http)
    resource.set_agent_bot(account_id=1, inbox_id=5, agent_bot_id=2)

    mock_http.post.assert_called_once_with(
        "/api/v1/accounts/1/inboxes/5/set_agent_bot",
        json={"agent_bot": 2},
    )


def test_set_agent_bot_remove(mock_http):
    """Test removing an agent bot by passing None."""
    mock_http.post.return_value = {}

    resource = InboxesResource(mock_http)
    resource.set_agent_bot(account_id=1, inbox_id=5, agent_bot_id=None)

    mock_http.post.assert_called_once_with(
        "/api/v1/accounts/1/inboxes/5/set_agent_bot",
        json={"agent_bot": None},
    )


@pytest.mark.asyncio
async def test_async_set_agent_bot(mock_async_http):
    """Test async assigning an agent bot."""
    mock_async_http.post = AsyncMock(return_value={})

    resource = AsyncInboxesResource(mock_async_http)
    await resource.set_agent_bot(account_id=1, inbox_id=5, agent_bot_id=2)

    mock_async_http.post.assert_called_once_with(
        "/api/v1/accounts/1/inboxes/5/set_agent_bot",
        json={"agent_bot": 2},
    )


@pytest.mark.asyncio
async def test_async_set_agent_bot_remove(mock_async_http):
    """Test async removing an agent bot by passing None."""
    mock_async_http.post = AsyncMock(return_value={})

    resource = AsyncInboxesResource(mock_async_http)
    await resource.set_agent_bot(account_id=1, inbox_id=5, agent_bot_id=None)

    mock_async_http.post.assert_called_once_with(
        "/api/v1/accounts/1/inboxes/5/set_agent_bot",
        json={"agent_bot": None},
    )
