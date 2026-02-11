"""Tests for profile resource."""

from chatwoot.resources.profile import ProfileResource
from chatwoot.types.profile import Profile


def test_get_profile(mock_http):
    """Test fetching profile."""
    # Setup mock response
    mock_http.get.return_value = {
        "id": 123,
        "name": "John Doe",
        "email": "john@example.com",
        "account_id": 1,
        "role": "administrator",
        "confirmed": True,
        "custom_attributes": {},
        "accounts": [],
    }

    # Create resource and call method
    resource = ProfileResource(mock_http)
    profile = resource.get()

    # Assertions
    mock_http.get.assert_called_once_with("/api/v1/profile")
    assert isinstance(profile, Profile)
    assert profile.id == 123
    assert profile.name == "John Doe"
    assert profile.email == "john@example.com"
    assert profile.account_id == 1
    assert profile.role == "administrator"
    assert profile.confirmed is True


def test_profile_with_accounts(mock_http):
    """Test profile with multiple accounts."""
    mock_http.get.return_value = {
        "id": 123,
        "name": "John Doe",
        "email": "john@example.com",
        "account_id": 1,
        "role": "agent",
        "confirmed": True,
        "custom_attributes": {"timezone": "UTC"},
        "accounts": [
            {"id": 1, "name": "Account 1", "role": "agent", "active_at": None},
            {"id": 2, "name": "Account 2", "role": "administrator", "active_at": None},
        ],
    }

    resource = ProfileResource(mock_http)
    profile = resource.get()

    assert len(profile.accounts) == 2
    assert profile.accounts[0].id == 1
    assert profile.accounts[0].name == "Account 1"
    assert profile.accounts[1].role == "administrator"
    assert profile.custom_attributes == {"timezone": "UTC"}
