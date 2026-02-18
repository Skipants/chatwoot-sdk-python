# Sync Contacts

Mirrors users from an external data source into Chatwoot — creates missing contacts, updates existing ones, and applies plan-based labels.

```python
"""Sync contacts from your application database into Chatwoot.

Looks up each user by email — creates the contact if missing, updates
custom_attributes and labels if it already exists.
"""

from chatwoot import ChatwootClient

BASE_URL = "http://localhost:3000"
API_TOKEN = "your-api-token"
ACCOUNT_ID = 1
INBOX_ID = 1  # Inbox to associate new contacts with

# Simulated application users — in practice, query your own database.
APP_USERS = [
    {"name": "Alice Park", "email": "alice@example.com", "plan": "enterprise"},
    {"name": "Bob Chen", "email": "bob@example.com", "plan": "pro"},
    {"name": "Carol Singh", "email": "carol@example.com", "plan": "free"},
]

PLAN_LABELS = {
    "enterprise": ["enterprise", "priority-support"],
    "pro": ["pro"],
    "free": ["free-tier"],
}


def sync_contact(client: ChatwootClient, user: dict) -> None:
    """Create or update a single contact from application data."""
    email = user["email"]
    plan = user["plan"]
    custom_attrs = {"plan": plan, "synced_from": "app-db"}

    # Search for existing contact
    matches = client.contacts.search(ACCOUNT_ID, query=email)
    existing = next((c for c in matches if c.email == email), None)

    if existing:
        # Update existing contact
        client.contacts.update(
            ACCOUNT_ID,
            existing.id,
            name=user["name"],
            custom_attributes=custom_attrs,
        )
        client.contacts.labels.add(
            ACCOUNT_ID, existing.id, labels=PLAN_LABELS.get(plan, [])
        )
        print(f"  Updated: {email} (id={existing.id})")
    else:
        # Create new contact
        result = client.contacts.create(
            ACCOUNT_ID,
            inbox_id=INBOX_ID,
            name=user["name"],
            email=email,
            custom_attributes=custom_attrs,
        )
        client.contacts.labels.add(
            ACCOUNT_ID, result.contact.id, labels=PLAN_LABELS.get(plan, [])
        )
        print(f"  Created: {email} (id={result.contact.id})")


def main() -> None:
    with ChatwootClient(base_url=BASE_URL, api_token=API_TOKEN) as client:
        print(f"Syncing {len(APP_USERS)} contacts")
        for user in APP_USERS:
            try:
                sync_contact(client, user)
            except Exception as e:
                print(f"  Failed: {user['email']} — {e}")

        print("Done.")


if __name__ == "__main__":
    main()
```

## What it covers

- `client.contacts.search` — look up a contact by email before creating
- `client.contacts.update` — update name and `custom_attributes` on an existing contact
- `client.contacts.create` — create a new contact with inbox association
- `client.contacts.labels.add` — apply plan-tier labels after create or update
