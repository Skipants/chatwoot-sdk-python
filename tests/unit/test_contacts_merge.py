"""Tests for contacts.merge."""

import pytest
from unittest.mock import AsyncMock

from chatwoot.resources.contacts import ContactsResource, AsyncContactsResource
from chatwoot.types.contact import Contact


MERGED_CONTACT = {
    "id": 100,
    "name": "John Doe",
    "email": "john@example.com",
    "phone_number": "+1234567890",
    "account_id": 1,
    "identifier": None,
    "additional_attributes": {},
    "custom_attributes": {},
    "availability_status": "offline",
    "blocked": False,
    "contact_inboxes": [],
}


def test_merge_contacts(mock_http):
    """Test merging two contacts."""
    mock_http.post.return_value = MERGED_CONTACT

    resource = ContactsResource(mock_http)
    contact = resource.merge(
        account_id=1,
        base_contact_id=100,
        mergee_contact_id=200,
    )

    mock_http.post.assert_called_once_with(
        "/api/v1/accounts/1/actions/contact_merge",
        json={"base_contact_id": 100, "mergee_contact_id": 200},
    )
    assert isinstance(contact, Contact)
    assert contact.id == 100
    assert contact.name == "John Doe"
    assert contact.email == "john@example.com"


@pytest.mark.asyncio
async def test_async_merge_contacts(mock_async_http):
    """Test async merging two contacts."""
    mock_async_http.post = AsyncMock(return_value=MERGED_CONTACT)

    resource = AsyncContactsResource(mock_async_http)
    contact = await resource.merge(
        account_id=1,
        base_contact_id=100,
        mergee_contact_id=200,
    )

    mock_async_http.post.assert_called_once_with(
        "/api/v1/accounts/1/actions/contact_merge",
        json={"base_contact_id": 100, "mergee_contact_id": 200},
    )
    assert isinstance(contact, Contact)
    assert contact.id == 100
