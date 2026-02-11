"""Error handling example for the Chatwoot SDK."""

from chatwoot import (
    ChatwootAuthError,
    ChatwootClient,
    ChatwootNotFoundError,
    ChatwootPermissionError,
    ChatwootValidationError,
)

# Initialize client
client = ChatwootClient(
    base_url="https://app.chatwoot.com",
    api_token="your_api_token_here",
)

try:
    # This will fail if the token is invalid
    profile = client.profile.get()
    print(f"Authenticated as: {profile.name}")

except ChatwootAuthError as e:
    print(f"Authentication failed: {e}")
    print(f"Status code: {e.status_code}")
    print(f"Description: {e.description}")
    exit(1)

account_id = 1

# Example: Handle not found error
try:
    conversation = client.conversations.get(
        account_id=account_id,
        conversation_id=999999,  # Non-existent ID
    )
except ChatwootNotFoundError as e:
    print(f"\nResource not found: {e}")
    print(f"Status code: {e.status_code}")

# Example: Handle validation error
try:
    contact = client.contacts.create(
        account_id=account_id,
        inbox_id=0,  # Invalid inbox ID
        email="invalid-email",  # Invalid email format
    )
except ChatwootValidationError as e:
    print(f"\nValidation error: {e}")
    print(f"Status code: {e.status_code}")
    print(f"Description: {e.description}")
    if e.errors:
        print("Detailed errors:")
        for error in e.errors:
            print(f"  - {error.get('field')}: {error.get('message')}")

# Example: Handle permission error
try:
    # Try to perform an action without proper permissions
    agent = client.agents.add(
        account_id=account_id,
        name="New Agent",
        email="new@example.com",
        role="agent",
    )
except ChatwootPermissionError as e:
    print(f"\nPermission denied: {e}")
    print(f"Status code: {e.status_code}")

# Always close the client
client.close()

print("\nDone!")
