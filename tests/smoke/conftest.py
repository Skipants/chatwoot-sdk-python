"""Smoke test configuration: CLI options and fixtures."""

from __future__ import annotations

from urllib.parse import urlparse

import pytest

from chatwoot import ChatwootClient


def pytest_addoption(parser: pytest.Parser) -> None:
    group = parser.getgroup("chatwoot", "Chatwoot smoke test options")
    group.addoption("--url", default=None, help="Chatwoot instance URL (must be localhost)")
    group.addoption("--account-id", default=None, type=int, help="Chatwoot account ID")
    group.addoption("--token", default=None, help="Chatwoot API access token")


@pytest.fixture(scope="module")
def client(request: pytest.FixtureRequest):
    url: str | None = request.config.getoption("--url")
    token: str | None = request.config.getoption("--token")

    if not url or not token:
        pytest.skip("Smoke tests require --url, --account-id, and --token")

    parsed = urlparse(url)
    if parsed.hostname not in ("localhost", "127.0.0.1"):
        pytest.skip(
            f"Safety guard: --url must point to localhost, got {parsed.hostname!r}. "
            "Smoke tests create and delete resources and must not run against production."
        )

    with ChatwootClient(base_url=url, api_token=token) as c:
        yield c


@pytest.fixture(scope="module")
def account_id(request: pytest.FixtureRequest) -> int:
    val: int | None = request.config.getoption("--account-id")
    if val is None:
        pytest.skip("Smoke tests require --account-id")
    return val


@pytest.fixture(scope="module")
def state() -> dict:
    """Shared mutable state dict so sequential tests can pass resource IDs forward."""
    return {}
