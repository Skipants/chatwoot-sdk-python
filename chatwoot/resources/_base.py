"""Base classes for API resources."""

from chatwoot._http import AsyncHTTPClient, HTTPClient


class BaseResource:
    """Base class for all synchronous resource implementations."""

    def __init__(self, http: HTTPClient):
        """Initialize base resource.

        Args:
            http: HTTP client instance
        """
        self._http = http


class AsyncBaseResource:
    """Base class for all asynchronous resource implementations."""

    def __init__(self, http: AsyncHTTPClient):
        """Initialize async base resource.

        Args:
            http: Async HTTP client instance
        """
        self._http = http
