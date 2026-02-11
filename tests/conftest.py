"""Pytest configuration and fixtures."""

import pytest
from unittest.mock import Mock

from chatwoot._http import HTTPClient, AsyncHTTPClient


@pytest.fixture
def mock_http():
    """Mock synchronous HTTP client."""
    http = Mock(spec=HTTPClient)
    http.get.return_value = {"id": 1, "name": "Test"}
    http.post.return_value = {"id": 1, "name": "Created"}
    http.patch.return_value = {"id": 1, "name": "Updated"}
    http.put.return_value = {"id": 1, "name": "Updated"}
    http.delete.return_value = {}
    return http


@pytest.fixture
def mock_async_http():
    """Mock asynchronous HTTP client."""
    http = Mock(spec=AsyncHTTPClient)
    http.get.return_value = {"id": 1, "name": "Test"}
    http.post.return_value = {"id": 1, "name": "Created"}
    http.patch.return_value = {"id": 1, "name": "Updated"}
    http.put.return_value = {"id": 1, "name": "Updated"}
    http.delete.return_value = {}
    return http


@pytest.fixture
def base_url():
    """Test base URL."""
    return "https://app.chatwoot.com"


@pytest.fixture
def api_token():
    """Test API token."""
    return "test-api-token-123"


@pytest.fixture
def account_id():
    """Test account ID."""
    return 1
