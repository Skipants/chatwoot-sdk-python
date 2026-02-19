"""Profile resource for fetching user profile information."""

from __future__ import annotations

from chatwoot.resources._base import AsyncBaseResource, BaseResource
from chatwoot.types.profile import Profile


class ProfileResource(BaseResource):
    """Synchronous profile resource."""

    def get(self) -> Profile:
        """Fetch current user profile.

        Returns:
            Profile object containing user information

        Raises:
            ChatwootAuthError: If authentication fails

        Examples:
            >>> client = ChatwootClient(base_url="", api_token="")
            ... profile = client.profile.get()
            ... print(profile.name)
        """
        response = self._http.get("/api/v1/profile")
        return Profile(**response)


class AsyncProfileResource(AsyncBaseResource):
    """Asynchronous profile resource."""

    async def get(self) -> Profile:
        """Fetch current user profile (async).

        Returns:
            Profile object containing user information

        Raises:
            ChatwootAuthError: If authentication fails

        Examples:
            >>> client = AsyncChatwootClient(base_url="", api_token="")
            ... profile = await client.profile.get()
            ... print(profile.name)
        """
        response = await self._http.get("/api/v1/profile")
        return Profile(**response)
