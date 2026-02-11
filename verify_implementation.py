#!/usr/bin/env python3
"""Verification script to test the Chatwoot SDK implementation."""

import sys


def test_imports():
    """Test that all main components can be imported."""
    print("Testing imports...")
    try:
        from chatwoot import (
            AsyncChatwootClient,
            ChatwootAPIError,
            ChatwootAuthError,
            ChatwootClient,
            ChatwootError,
            ChatwootNotFoundError,
            ChatwootPermissionError,
            ChatwootValidationError,
        )

        print("✓ Main imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False


def test_client_initialization():
    """Test client initialization."""
    print("\nTesting client initialization...")
    try:
        from chatwoot import AsyncChatwootClient, ChatwootClient

        # Test sync client
        client = ChatwootClient(base_url="https://example.com", api_token="test")
        assert hasattr(client, "profile")
        assert hasattr(client, "conversations")
        assert hasattr(client, "messages")
        assert hasattr(client, "contacts")
        assert hasattr(client, "inboxes")
        assert hasattr(client, "teams")
        assert hasattr(client, "agents")
        client.close()

        # Test async client
        async_client = AsyncChatwootClient(
            base_url="https://example.com", api_token="test"
        )
        assert hasattr(async_client, "profile")
        assert hasattr(async_client, "conversations")
        assert hasattr(async_client, "messages")

        print("✓ Client initialization successful")
        return True
    except Exception as e:
        print(f"✗ Client initialization failed: {e}")
        return False


def test_nested_resources():
    """Test nested resources."""
    print("\nTesting nested resources...")
    try:
        from chatwoot import ChatwootClient

        client = ChatwootClient(base_url="https://example.com", api_token="test")

        # Test nested labels resources
        assert hasattr(client.conversations, "labels")
        assert hasattr(client.contacts, "labels")

        # Test nested teams.agents resource
        assert hasattr(client.teams, "agents")

        client.close()

        print("✓ Nested resources successful")
        return True
    except Exception as e:
        print(f"✗ Nested resources failed: {e}")
        return False


def test_type_models():
    """Test type models."""
    print("\nTesting type models...")
    try:
        from chatwoot.types.profile import Profile
        from chatwoot.types.conversation import Conversation
        from chatwoot.types.message import Message
        from chatwoot.types.contact import Contact
        from chatwoot.types.agent import Agent
        from chatwoot.types.team import Team
        from chatwoot.types.inbox import Inbox

        # Test model creation
        profile = Profile(
            id=1,
            name="Test User",
            email="test@example.com",
            account_id=1,
            role="agent",
        )
        assert profile.id == 1
        assert profile.name == "Test User"

        print("✓ Type models successful")
        return True
    except Exception as e:
        print(f"✗ Type models failed: {e}")
        return False


def test_exceptions():
    """Test exception classes."""
    print("\nTesting exceptions...")
    try:
        from chatwoot.exceptions import (
            ChatwootAPIError,
            ChatwootAuthError,
            ChatwootNotFoundError,
            ChatwootValidationError,
        )

        # Test exception creation
        error = ChatwootAPIError(500, "Test error")
        assert error.status_code == 500
        assert error.description == "Test error"

        auth_error = ChatwootAuthError()
        assert auth_error.status_code == 401

        print("✓ Exceptions successful")
        return True
    except Exception as e:
        print(f"✗ Exceptions failed: {e}")
        return False


def main():
    """Run all verification tests."""
    print("=" * 60)
    print("Chatwoot SDK Implementation Verification")
    print("=" * 60)

    tests = [
        test_imports,
        test_client_initialization,
        test_nested_resources,
        test_type_models,
        test_exceptions,
    ]

    results = [test() for test in tests]

    print("\n" + "=" * 60)
    print(f"Results: {sum(results)}/{len(results)} tests passed")
    print("=" * 60)

    if all(results):
        print("\n✓ All verification tests passed!")
        return 0
    else:
        print("\n✗ Some verification tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
