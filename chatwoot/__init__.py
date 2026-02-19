"""Chatwoot SDK for Python.

A modern, type-safe Python SDK for the Chatwoot API.

Examples:
    >>> from chatwoot import ChatwootClient
    >>>
    >>> client = ChatwootClient(
    ...     base_url="https://app.chatwoot.com",
    ...     api_token="your_api_token_here"
    ... )
    ...
    >>> # Fetch your profile
    >>> profile = client.profile.get()
    >>> print(f"Logged in as: {profile.name}")
    ...
    >>> # List open conversations
    >>> conversations = client.conversations.list(
    ...     account_id=1,
    ...     status="open"
    ... )
    >>> print(f"Open conversations: {len(conversations)}")
    ...
    >>> # Send a message
    >>> message = client.messages.create(
    ...     account_id=1,
    ...     conversation_id=42,
    ...     content="Hello from the Python SDK!"
    ... )
    ...
    >>> client.close()
"""

from chatwoot.client import AsyncChatwootClient, ChatwootClient
from chatwoot.exceptions import (
    ChatwootAPIError,
    ChatwootAuthError,
    ChatwootError,
    ChatwootNotFoundError,
    ChatwootPermissionError,
    ChatwootValidationError,
)

__version__ = "0.1.0"

__all__ = [
    # Client classes
    "ChatwootClient",
    "AsyncChatwootClient",
    # Exception classes
    "ChatwootError",
    "ChatwootAPIError",
    "ChatwootAuthError",
    "ChatwootNotFoundError",
    "ChatwootPermissionError",
    "ChatwootValidationError",
]
