"""Custom exceptions for the Chatwoot SDK."""

from __future__ import annotations


class ChatwootError(Exception):
    """Base exception for all Chatwoot SDK errors."""


class ChatwootAPIError(ChatwootError):
    """API returned an error response."""

    def __init__(
        self,
        status_code: int,
        description: str,
        errors: list[dict] | None = None,
    ):
        """Initialize API error.

        Args:
            status_code: HTTP status code
            description: Error description from API
            errors: List of detailed error objects with field, message, code
        """
        self.status_code = status_code
        self.description = description
        self.errors = errors or []

        error_details = ""
        if self.errors:
            error_messages = [
                f"{err.get('field', 'unknown')}: {err.get('message', 'unknown error')}"
                for err in self.errors
            ]
            error_details = f" - {', '.join(error_messages)}"

        super().__init__(f"[{status_code}] {description}{error_details}")


class ChatwootAuthError(ChatwootAPIError):
    """Authentication failed (401)."""

    def __init__(
        self,
        description: str = "Authentication failed",
        errors: list[dict] | None = None,
    ):
        super().__init__(401, description, errors)


class ChatwootPermissionError(ChatwootAPIError):
    """Permission denied (403)."""

    def __init__(
        self, description: str = "Permission denied", errors: list[dict] | None = None
    ):
        super().__init__(403, description, errors)


class ChatwootNotFoundError(ChatwootAPIError):
    """Resource not found (404)."""

    def __init__(
        self, description: str = "Resource not found", errors: list[dict] | None = None
    ):
        super().__init__(404, description, errors)


class ChatwootValidationError(ChatwootAPIError):
    """Request validation failed (400)."""

    def __init__(
        self, description: str = "Validation failed", errors: list[dict] | None = None
    ):
        super().__init__(400, description, errors)
