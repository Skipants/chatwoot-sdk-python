"""Main Chatwoot API client."""

from chatwoot._http import AsyncHTTPClient, HTTPClient
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


class ChatwootClient:
    """Synchronous Chatwoot API client.

    This is the main entry point for interacting with the Chatwoot API.
    All API operations are organized into resource-specific namespaces.

    Examples:
        >>> client = ChatwootClient(
        ...     base_url="https://app.chatwoot.com",
        ...     api_token="your_api_token_here"
        ... )
        ...
        >>> # Fetch user profile
        >>> profile = client.profile.get()
        >>> print(profile.name)
        ...
        >>> # List conversations
        >>> conversations = client.conversations.list(account_id=1, status="open")
        ...
        >>> # Send a message
        >>> message = client.messages.create(
        ...     account_id=1,
        ...     conversation_id=42,
        ...     content="Hello from SDK!"
        ... )
        ...
        >>> # Use as context manager for automatic cleanup
        >>> with ChatwootClient(base_url="", api_token="") as client:
        ...     profile = client.profile.get()
    """

    def __init__(self, base_url: str, api_token: str, timeout: float = 30.0):
        """Initialize Chatwoot client.

        Args:
            base_url: Chatwoot instance URL (e.g., "https://app.chatwoot.com")
            api_token: User API access token from profile settings.
                      Get it from: Settings → Profile Settings → Access Token
            timeout: Request timeout in seconds (default: 30.0)

        Raises:
            ChatwootAuthError: If authentication fails on first request
        """
        self._http = HTTPClient(base_url, api_token, timeout)

        # Initialize all resource namespaces
        self.profile = ProfileResource(self._http)
        self.conversations = ConversationsResource(self._http)
        self.messages = MessagesResource(self._http)
        self.contacts = ContactsResource(self._http)
        self.inboxes = InboxesResource(self._http)
        self.teams = TeamsResource(self._http)
        self.agents = AgentsResource(self._http)

    def close(self) -> None:
        """Close the HTTP client and release resources.

        Call this when you're done with the client to properly
        clean up connections.
        """
        self._http.close()

    def __enter__(self) -> "ChatwootClient":
        """Context manager entry."""
        return self

    def __exit__(self, *args) -> None:
        """Context manager exit."""
        self.close()


class AsyncChatwootClient:
    """Asynchronous Chatwoot API client.

    This is the async version of the Chatwoot client, using async/await
    patterns for non-blocking I/O operations.

    Examples:
        >>> import asyncio
        >>>
        >>> async def main():
        ...     client = AsyncChatwootClient(
        ...         base_url="https://app.chatwoot.com",
        ...         api_token="your_api_token_here"
        ...     )
        ...
        ...     # Fetch user profile
        ...     profile = await client.profile.get()
        ...     print(profile.name)
        ...
        ...     # List conversations
        ...     conversations = await client.conversations.list(
        ...         account_id=1,
        ...         status="open"
        ...     )
        ...
        ...     await client.aclose()
        ...
        >>> # Or use as async context manager
        >>> async def main():
        ...     async with AsyncChatwootClient(base_url="", api_token="") as client:
        ...         profile = await client.profile.get()
    """

    def __init__(self, base_url: str, api_token: str, timeout: float = 30.0):
        """Initialize async Chatwoot client.

        Args:
            base_url: Chatwoot instance URL (e.g., "https://app.chatwoot.com")
            api_token: User API access token from profile settings
            timeout: Request timeout in seconds (default: 30.0)
        """
        self._http = AsyncHTTPClient(base_url, api_token, timeout)

        # Initialize all async resource namespaces
        self.profile = AsyncProfileResource(self._http)
        self.conversations = AsyncConversationsResource(self._http)
        self.messages = AsyncMessagesResource(self._http)
        self.contacts = AsyncContactsResource(self._http)
        self.inboxes = AsyncInboxesResource(self._http)
        self.teams = AsyncTeamsResource(self._http)
        self.agents = AsyncAgentsResource(self._http)

    async def aclose(self) -> None:
        """Close the async HTTP client and release resources.

        Call this when you're done with the client to properly
        clean up connections.
        """
        await self._http.aclose()

    async def __aenter__(self) -> "AsyncChatwootClient":
        """Async context manager entry."""
        return self

    async def __aexit__(self, *args) -> None:
        """Async context manager exit."""
        await self.aclose()
