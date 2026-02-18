"""HTTP client wrapper for Chatwoot API."""

from __future__ import annotations

from typing import Any

import httpx

from chatwoot.exceptions import (
    ChatwootAPIError,
    ChatwootAuthError,
    ChatwootNotFoundError,
    ChatwootPermissionError,
    ChatwootValidationError,
)


class HTTPClient:
    """Synchronous HTTP client for Chatwoot API."""

    def __init__(self, base_url: str, api_token: str, timeout: float = 30.0):
        """Initialize HTTP client.

        Args:
            base_url: Chatwoot instance URL (e.g., "https://app.chatwoot.com")
            api_token: User API access token from profile settings
            timeout: Request timeout in seconds (default: 30.0)
        """
        self._client = httpx.Client(
            base_url=base_url.rstrip("/"),
            headers={"api_access_token": api_token, "Content-Type": "application/json"},
            timeout=timeout,
        )

    def _unwrap_response(self, data: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """Unwrap API response to extract actual data.

        Chatwoot API returns data in various formats:
        - {payload: []} - list response
        - {data: {payload: []}} - nested list response
        - {id: 1, } - single object response
        """
        if not isinstance(data, dict):
            return data

        # {data: {payload: []}} or {data: }
        if "data" in data:
            nested_data = data["data"]
            if isinstance(nested_data, dict) and "payload" in nested_data:
                return nested_data["payload"]
            return nested_data

        # {payload: }
        if "payload" in data:
            return data["payload"]

        return data

    def _handle_error(self, response: httpx.Response) -> None:
        """Handle error responses and raise appropriate exceptions."""
        try:
            error_data = response.json()
            description = error_data.get(
                "description", error_data.get("message", "Unknown error")
            )
            errors = error_data.get("errors")
        except Exception:
            description = response.text or "Unknown error"
            errors = None

        status_code = response.status_code

        if status_code == 401:
            raise ChatwootAuthError(description, errors)
        elif status_code == 403:
            raise ChatwootPermissionError(description, errors)
        elif status_code == 404:
            raise ChatwootNotFoundError(description, errors)
        elif status_code == 400:
            raise ChatwootValidationError(description, errors)
        else:
            raise ChatwootAPIError(status_code, description, errors)

    def request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> dict[str, Any] | list[Any]:
        """Make HTTP request and handle errors.

        Args:
            method: HTTP method (GET, POST, PUT, PATCH, DELETE)
            path: Request path
            **kwargs: Additional arguments to pass to httpx

        Returns:
            Parsed JSON response

        Raises:
            ChatwootAPIError: If the API returns an error
        """
        response = self._client.request(method, path, **kwargs)

        if not response.is_success:
            self._handle_error(response)

        # Handle empty response body (204 No Content or empty 200)
        if response.status_code == 204 or not response.content:
            return {}

        data = response.json()
        return self._unwrap_response(data)

    def get(self, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        """Make GET request.

        Args:
            path: Request path
            **kwargs: Additional arguments (params, headers, etc.)

        Returns:
            Response data
        """
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        """Make POST request.

        Args:
            path: Request path
            **kwargs: Additional arguments (json, data, files, etc.)

        Returns:
            Response data
        """
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        """Make PUT request.

        Args:
            path: Request path
            **kwargs: Additional arguments (json, data, etc.)

        Returns:
            Response data
        """
        return self.request("PUT", path, **kwargs)

    def patch(self, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        """Make PATCH request.

        Args:
            path: Request path
            **kwargs: Additional arguments (json, data, etc.)

        Returns:
            Response data
        """
        return self.request("PATCH", path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        """Make DELETE request.

        Args:
            path: Request path
            **kwargs: Additional arguments

        Returns:
            Response data (usually empty)
        """
        return self.request("DELETE", path, **kwargs)

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def __enter__(self) -> "HTTPClient":
        """Context manager entry."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Context manager exit."""
        self.close()


class AsyncHTTPClient:
    """Asynchronous HTTP client for Chatwoot API."""

    def __init__(self, base_url: str, api_token: str, timeout: float = 30.0):
        """Initialize async HTTP client.

        Args:
            base_url: Chatwoot instance URL (e.g., "https://app.chatwoot.com")
            api_token: User API access token from profile settings
            timeout: Request timeout in seconds (default: 30.0)
        """
        self._client = httpx.AsyncClient(
            base_url=base_url.rstrip("/"),
            headers={"api_access_token": api_token, "Content-Type": "application/json"},
            timeout=timeout,
        )

    def _unwrap_response(self, data: dict[str, Any]) -> dict[str, Any] | list[Any]:
        """Unwrap API response to extract actual data.

        Chatwoot API returns data in various formats:
        - {payload: []} - list response
        - {data: {payload: []}} - nested list response
        - {id: 1, } - single object response
        """
        if not isinstance(data, dict):
            return data

        # {data: {payload: []}} or {data: }
        if "data" in data:
            nested_data = data["data"]
            if isinstance(nested_data, dict) and "payload" in nested_data:
                return nested_data["payload"]
            return nested_data

        # {payload: }
        if "payload" in data:
            return data["payload"]

        return data

    def _handle_error(self, response: httpx.Response) -> None:
        """Handle error responses and raise appropriate exceptions."""
        try:
            error_data = response.json()
            description = error_data.get(
                "description", error_data.get("message", "Unknown error")
            )
            errors = error_data.get("errors")
        except Exception:
            description = response.text or "Unknown error"
            errors = None

        status_code = response.status_code

        if status_code == 401:
            raise ChatwootAuthError(description, errors)
        elif status_code == 403:
            raise ChatwootPermissionError(description, errors)
        elif status_code == 404:
            raise ChatwootNotFoundError(description, errors)
        elif status_code == 400:
            raise ChatwootValidationError(description, errors)
        else:
            raise ChatwootAPIError(status_code, description, errors)

    async def request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> dict[str, Any] | list[Any]:
        """Make async HTTP request and handle errors.

        Args:
            method: HTTP method (GET, POST, PUT, PATCH, DELETE)
            path: Request path
            **kwargs: Additional arguments to pass to httpx

        Returns:
            Parsed JSON response

        Raises:
            ChatwootAPIError: If the API returns an error
        """
        response = await self._client.request(method, path, **kwargs)

        if not response.is_success:
            self._handle_error(response)

        # Handle empty response body (204 No Content or empty 200)
        if response.status_code == 204 or not response.content:
            return {}

        data = response.json()
        return self._unwrap_response(data)

    async def get(self, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        """Make async GET request."""
        return await self.request("GET", path, **kwargs)

    async def post(self, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        """Make async POST request."""
        return await self.request("POST", path, **kwargs)

    async def put(self, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        """Make async PUT request."""
        return await self.request("PUT", path, **kwargs)

    async def patch(self, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        """Make async PATCH request."""
        return await self.request("PATCH", path, **kwargs)

    async def delete(self, path: str, **kwargs: Any) -> dict[str, Any] | list[Any]:
        """Make async DELETE request."""
        return await self.request("DELETE", path, **kwargs)

    async def aclose(self) -> None:
        """Close the async HTTP client."""
        await self._client.aclose()

    async def __aenter__(self) -> "AsyncHTTPClient":
        """Async context manager entry."""
        return self

    async def __aexit__(self, *args: Any) -> None:
        """Async context manager exit."""
        await self.aclose()
