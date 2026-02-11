"""Tests for exception classes."""

from chatwoot.exceptions import (
    ChatwootAPIError,
    ChatwootAuthError,
    ChatwootError,
    ChatwootNotFoundError,
    ChatwootPermissionError,
    ChatwootValidationError,
)


def test_base_exception():
    """Test base ChatwootError exception."""
    error = ChatwootError("Test error")
    assert str(error) == "Test error"
    assert isinstance(error, Exception)


def test_api_error_basic():
    """Test ChatwootAPIError with basic info."""
    error = ChatwootAPIError(500, "Internal server error")
    assert error.status_code == 500
    assert error.description == "Internal server error"
    assert error.errors == []
    assert str(error) == "[500] Internal server error"


def test_api_error_with_errors():
    """Test ChatwootAPIError with detailed errors."""
    errors = [
        {"field": "email", "message": "is invalid", "code": "invalid"},
        {"field": "name", "message": "can't be blank", "code": "blank"},
    ]
    error = ChatwootAPIError(400, "Validation failed", errors)
    assert error.status_code == 400
    assert error.description == "Validation failed"
    assert error.errors == errors
    assert "email: is invalid" in str(error)
    assert "name: can't be blank" in str(error)


def test_auth_error():
    """Test ChatwootAuthError."""
    error = ChatwootAuthError()
    assert error.status_code == 401
    assert error.description == "Authentication failed"
    assert isinstance(error, ChatwootAPIError)


def test_auth_error_custom():
    """Test ChatwootAuthError with custom message."""
    error = ChatwootAuthError("Invalid token")
    assert error.status_code == 401
    assert error.description == "Invalid token"


def test_permission_error():
    """Test ChatwootPermissionError."""
    error = ChatwootPermissionError()
    assert error.status_code == 403
    assert error.description == "Permission denied"
    assert isinstance(error, ChatwootAPIError)


def test_not_found_error():
    """Test ChatwootNotFoundError."""
    error = ChatwootNotFoundError()
    assert error.status_code == 404
    assert error.description == "Resource not found"
    assert isinstance(error, ChatwootAPIError)


def test_validation_error():
    """Test ChatwootValidationError."""
    error = ChatwootValidationError()
    assert error.status_code == 400
    assert error.description == "Validation failed"
    assert isinstance(error, ChatwootAPIError)


def test_validation_error_with_details():
    """Test ChatwootValidationError with field errors."""
    errors = [{"field": "email", "message": "is required"}]
    error = ChatwootValidationError("Invalid input", errors)
    assert error.status_code == 400
    assert error.description == "Invalid input"
    assert error.errors == errors
